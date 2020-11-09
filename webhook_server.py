#!/usr/bin/env python3

#   GitHub Web Hook Server
#   Copyright (C) 2020  Andreas Stöckel
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Most of the webserver code in this file is adapted from Tivua, licensed under
# the AGPL. See https://github.com/astoeckel/tivua for more information.

# IMPORTANT: Updating this file in the Git repository will not automatically
#            reinstall an updated version of the webhook server. You will need
#            to manually log onto the corresponding machine, download this
#            file, and restart the service.

import argparse
import collections
import datetime
import hmac
import http.server
import http.client
import json
import os
import re
import subprocess
import sys
import time

from tempfile import TemporaryDirectory as TmpDir
from tempfile import NamedTemporaryFile as TmpFile

################################################################################
# Logger                                                                       #
################################################################################

import logging
logger = logging.getLogger(__name__)

################################################################################
# Helper functions                                                             #
################################################################################


def ntpl(**kwargs):
    return collections.namedtuple("ntpl", kwargs.keys())(**kwargs)


def escape(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace(
        '>', '&gt;').replace('"', '&quot;').replace("'", '&#39;'))


# Removes ansi escape sequences --- see https://stackoverflow.com/a/14693789
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


def remove_ansi(s):
    return ANSI_ESCAPE.sub("", s)


################################################################################
# HTTP request handlers                                                        #
################################################################################


def _handle_error(code, msg=None):
    ERROR_PAGE = '''<!doctype html>
<head><title>{code} {msg}</title></head>
<body><center><h1>{code} {msg}</h1></center>
<hr><center>webhook_server.py</center></body>'''

    # If no message is given, try to lookup the correct status code
    if msg is None:
        msg = http.client.responses[code]

    def _handler(req, query=None, match=None, head=False):
        # Send the header
        req.send_response(code)
        req.send_header("Content-type", "text/html; charset=utf-8")
        req.end_headers()
        if head:
            return True

        # Generate the actual HTML
        req.wfile.write(
            ERROR_PAGE.format(code=code, msg=escape(msg)).encode('utf-8'))
        return True

    return _handler


def _handle_webhook(args, runner, secret=None):
    MAX_POST_BODY_LENGTH = (1 << 16)
    RESPONSE = '''{}: {}\n'''

    def _handler(req, query=None, match=None, head=False):
        # Read the JSON request
        payload = bytes()
        if "Content-Length" in req.headers:
            length = int(req.headers.get("Content-Length"))
            if (length < 0) or (length > MAX_POST_BODY_LENGTH):
                return _handle_error(400, "Request Body Too Large")(req)
            if length > 0:
                try:
                    payload = req.rfile.read(length)
                    body = json.loads(payload)
                except json.decoder.JSONDecodeError:
                    return _handle_error(400, "Invalid Request Body")(req)

        # Try to verify the request
        if not secret is None:
            if not "X-Hub-Signature-256" in req.headers:
                return _handle_error(400, "Signature Required")(req)
            sig = req.headers["X-Hub-Signature-256"]
            if (len(sig) != 71) or (not sig.startswith("sha256=")):
                return _handle_error(400, "Invalid Signature")(req)
            sig_in = bytes.fromhex(sig[7:])
            sig_ref = hmac.digest(secret, payload, "sha256")
            if not hmac.compare_digest(sig_in, sig_ref):
                return _handle_error(400, "Signature Verification Failed")(req)

        # Read information from the request
        try:
            # If args.branch is set, check whether the push request is for the
            # specified branch
            matches = True
            if (not "X-GitHub-Event" in req.headers) or (
                    req.headers["X-GitHub-Event"] != "push"):
                logger.info(
                    "Received webhook event with unknown or missing webhook event type"
                )
                matches = False
            if args.branch and (body["ref"] != "refs/heads/" + args.branch):
                logger.info("Received webhook event for unmonitored branch")
                matches = False

            # Fetch some information about the push request
            repository_name = body["repository"]["full_name"]
            commit_id = body["after"][:7]
            email = None
            if "email" in body["head_commit"]["committer"]:
                email = body["head_commit"]["committer"]["email"]
            if (not email) and ("email" in body["head_commit"]["author"]):
                email = body["head_commit"]["author"]["email"]
        except Exception as e:
            logger.exception(e)
            return _handle_error(400, "Invalid Request Body")(req)

        # Send the response header
        if head:
            req.send_response(200)
            req.send_header('Content-type', 'text/plain')
            req.end_headers()
            return True

        # If the request matches our filter settings, queue a build job!
        if matches:
            try:
                logger.info("Received webhook event, triggering build")
                runner.queue_job(args=[args.script],
                                 commit_id=commit_id,
                                 repository_name=repository_name,
                                 url=args.url,
                                 email_to=[email] if email else [])
                runner.check_queue_and_spawn()
            except Exception as e:
                logger.exception(e)
                return _handle_error(500, "Internal Server Error")(req)

        # Write the response header and payload
        req.send_response(200)
        req.send_header('Content-type', 'text/plain')
        req.end_headers()
        req.wfile.write(RESPONSE.format(200, "OK").encode("utf-8"))
        return True

    return _handler


################################################################################
# Status page                                                                  #
################################################################################

STATUS_CSS = '''
html { height: 100%; }
body {
    font-family: sans-serif;
    position: relative;
    max-width: 60rem;
    min-height: 100%;
    padding: 1em 1em 5em 1em;
    margin: 0 auto;
    box-sizing: border-box; }

h1 {
    padding: 0.5rem 0;
    border-bottom: 4px solid black; }

p {
    margin: 2em 0;
    line-height: 1.25em; }

p.status { font-size: 150%; }

span.status {
    display: inline-block;
    float: right;
    min-width: calc(9rem + 0.125em); }

span.status span.indicator {
    position: relative;
    top: 0.125em;
    display: inline-block;
    background-color: gray;
    border-radius: 100%;
    width: 1em;
    height: 1em;
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover; }

span.status.success {
    color: green; }

span.status.failure,
span.status.timeout {
    color: crimson;
}

span.status.running {
    color: dodgerblue;
}

span.status.unknown,
span.status.queued {
    color: gray;
}

@keyframes running {
    0% {background-color: dodgerblue}
    50% {background-color: white}
    100% {background-color: dodgerblue} }

span.status.success span.indicator {
    background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMTZtbSIgaGVpZ2h0PSIxNm1tIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNiAxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im00LjYyIDguOTEgMi44IDIuMTggMy45Ny02LjE5IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjUiLz4KPC9zdmc+Cg==");
    background-color: green; }


span.status.failure span.indicator,
span.status.timeout span.indicator {
    background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMTZtbSIgaGVpZ2h0PSIxNm1tIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNiAxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxnIHRyYW5zZm9ybT0ibWF0cml4KC42NSAwIDAgLjY1IDIuOCAyLjgpIiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIzLjkiPgogIDxwYXRoIGQ9Im0xMiAxMi04LjctOC43Ii8+CiAgPHBhdGggZD0ibTMuNyAxMiA4LjctOC43Ii8+CiA8L2c+Cjwvc3ZnPgo=");
    background-color: crimson; }

span.status.running span.indicator {
    background-color: dodgerblue;
    animation-name: running;
    animation-duration: 1s;
    animation-iteration-count: infinite; }

span.status.unknown span.indicator,
span.status.queued span.indicator { background-color: gray; }


div.build { border-top: 2px solid black; }

div.build:last-child { border-bottom: 2px solid black; }

div.build pre {
    margin: 0;
    overflow: hidden;
    padding: 1rem;
    background-color: black;
    color: white;
    white-space: pre-wrap; }

div.header span.number {
    font-weight: bold;
    flex: 0 0 auto;
    padding-right: 1em;
}

div.header span.title {
    flex: 1 1 auto;
}

div.header span.status {
    flex: 0 0 auto;
}

div.header {
    display: flex;
    cursor: pointer;
    padding: 1rem 0 1rem 1rem;
    font-size: 125%; }

div.header:hover {
    background-color: #fce94f; }

div.header:hover > * {
    color: black; }

div.build.opened div.header,
div.build:focus div.header {
    background-color: black; }

div.build.opened div.header > *,
div.build:focus div.header > * {
    color: white; }

div.build pre { display: none; }

div.build,
div.build:focus pre,
div.build.opened pre { display: block; }

footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 1rem;
    font-size: 75%;
    color: gray; }

footer > a:link { color: gray; }
'''

STATUS_JS = '''
document.addEventListener("DOMContentLoaded", function() {
    "use strict";
    const builds = document.querySelectorAll("div.build");
    for (let elem of builds) {
        elem.addEventListener("mousedown", function () {
            for (let elem of builds) {
                elem.classList.toggle("opened", false);
            }
            this.focus();
            this.classList.toggle("opened", true);
            let name = this.getAttribute("name");
            if (name) {
                let url = new URL(window.location);
                url.hash = "#" + name;
                history.replaceState(null, "", url);
            }
        });
    }
});
window.addEventListener("load", function() {
    if (window.location.hash) {
        window.setTimeout(function() {
            let name = window.location.hash.substr(1)
            let elem = document.querySelector(`div.build[name=\"${name}\"]`);
            if (elem) {
                elem.focus();
                elem.classList.add("opened");
                let r = elem.getBoundingClientRect();
                window.scrollTo(r.left, r.bottom);
            }
        }, 100.0);
    }
});
'''

STATUS_HTML = '''<!doctype html>
<html>
    <head>
        <title>Status: {repository_name}</title>
        <style type="text/css">{css}</style>
        <meta name="robots" content="noindex,nofollow">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Build status of “{repository_name}”</h1>
        <p class="status"><span>Current status:</span><span class="status {status_class}"><span class="indicator"></span> {status_name}</span></p>
        <p>Click any of the headers in the list below for the complete build-log. Manually reload the page for updates. This page will only show the ten latest builds.</p>
        <div class="build_container">
            {builds}
        </div>
        <script type="text/javascript">{js}</script>
        <footer>
            Minimalistic GitHub Webhook and CI Server. (c) Andreas Stöckel, 2020. Licensed under the AGPL.
            <a href="https://github.com/ctn-waterloo/website/blob/master/webhook_server.py">Source code</a>
        </footer>
    </body>
</html>
'''

STATUS_BUILD_BLOCK_HTML = """<div class="build" tabindex="{tab_index}" name="{id}">
    <div class="header">
        <span class="number">#{build_index}</span>
        <span class="title">{header}</span>
        <span class="status {status_class}"><span class="indicator"></span> {status_name}</span>
    </div>
    <pre>{output}</pre>
</div>
"""


def _handle_status(args, runner):
    def _handler(req, query=None, match=None, head=False):
        # Send the response header
        req.send_response(200)
        req.send_header('Content-type', 'text/html; charset=utf-8')
        req.end_headers()
        if head:
            return True

        # List all jobs and builds, reverse the list and select the last ten
        # entries
        def status_name(status):
            return "" if len(status) == 0 else status[0].upper() + status[1:]

        builds = sorted(runner.aggregate_jobs_and_builds().values(),
                        key=lambda o: -o.time)
        builds_html = "<p>No builds found since the server was last restarted!</p>" if len(
            builds) == 0 else ""
        global_status = "unknown"
        for i, build in enumerate(builds[:10]):
            # Read the build output
            try:
                output = ""
                if not build.output is None:
                    with open(build.output, 'r') as f:
                        output = remove_ansi(f.read())
            except OSError as e:
                logger.error(e)

            # Assemble the header
            header = "Build queued on {} UTC".format(
                datetime.datetime.utcfromtimestamp(
                    build.time * 1e-9).strftime("%Y-%m-%d %H:%M:%S"))

            # Update the global status
            if (global_status == "unknown") and (build.status != "queued"):
                global_status = build.status

            # Assemble the HTML
            builds_html += STATUS_BUILD_BLOCK_HTML.format(
                tab_index=i,
                id=build.id,
                build_index=len(builds) - i,
                header=header,
                status_class=build.status,
                status_name=status_name(build.status),
                output=escape(output))

        # Write the response code
        html = STATUS_HTML.format(css=STATUS_CSS,
                                  js=STATUS_JS,
                                  repository_name=args.repository,
                                  status_class=global_status,
                                  status_name=status_name(global_status),
                                  builds=builds_html)
        req.wfile.write(html.encode("utf-8"))
        return True

    return _handler


################################################################################
# Request Router                                                               #
################################################################################


class Route:
    def __init__(self, method, path, callback):
        self.method = method.upper()
        self.path = re.compile(path)
        self.callback = callback

    def exec_on_match(self, req, method, head, path, query):
        if (self.method == "*") or (method == self.method) or head:
            match = self.path.match(path)
            if match:
                return self.callback(req, query, match, head)
        return False


class Router:
    def __init__(self, routes):
        self.routes = routes

    @staticmethod
    def _parse_path(path):
        from urllib.parse import parse_qs

        # Reject malicious paths
        if (len(path) == 0) or (path[0] != '/') or (".." in path):
            return None, None

        # Parse the query string
        query = {}
        if "?" in path:
            path, query = path.split("?", 1)
            query = parse_qs(query)

        return path, query

    def exec(self, req):
        # Fetch the method and the path, reject malformed paths
        method = req.command.upper()
        head = method == "HEAD"
        path, query = self._parse_path(req.path)
        if path is None:
            _handle_error(404)(req, None, head)
            return False
        logger.debug("Router request for path=%s, query=%s", path, repr(query))

        # Try to execute the request
        for route in self.routes:
            if route is None:
                continue
            res = route.exec_on_match(req, method, head, path, query)
            if res or (res is None):
                return True

        # No route matched, issue a 404 error
        _handle_error(404)(req, None, head)
        return False


def _construct_http_server_class(args, runner, secret):
    router = Router([
        Route("POST", r"^/webhook$", _handle_webhook(args, runner, secret)),
        Route("GET", r"^/status$", _handle_status(args, runner)),
    ])

    class Server(http.server.BaseHTTPRequestHandler):
        def do_HEAD(self):
            router.exec(self)

        def do_POST(self):
            router.exec(self)

        def do_GET(self):
            router.exec(self)

    return Server


###############################################################################
# Job Runner                                                                  #
###############################################################################


class JobRunner:
    JOB_FILE_REGEX = re.compile(r"^job_([0-9a-fA-F]+)\.json")
    BUILD_FILE_REGEX = re.compile(r"^out_([0-9a-fA-F]+)\.([a-z]+)\.txt")

    def __init__(self,
                 job_dir=None,
                 out_dir=None,
                 timeout=600.0,
                 verbose=False):
        self._proc = None
        self._job_dir = TmpDir() if job_dir is None else ntpl(name=job_dir)
        self._out_dir = TmpDir() if out_dir is None else ntpl(name=out_dir)
        self._timeout = timeout
        self._verbose = verbose

        # Make sure that the output directories exist, and that only the current
        # user has access to these directories
        def mk_secure_dir(dir):
            if not os.path.isdir(dir):
                os.makedirs(dir, exist_ok=True, mode=0o700)
            os.chmod(dir, 0o700)
        mk_secure_dir(self._job_dir.name)
        mk_secure_dir(self._out_dir.name)

    def __enter__(self):
        if isinstance(self._job_dir, TmpDir):
            self._job_dir.__enter__()
        if isinstance(self._out_dir, TmpDir):
            self._out_dir.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        if isinstance(self._job_dir, TmpDir):
            self._job_dir.__exit__(type, value, traceback)
        if isinstance(self._out_dir, TmpDir):
            self._out_dir.__exit__(type, value, traceback)
        if self.is_child_running():
            logger.info("Waiting for child process to exit...")
            try:
                self._proc.terminate()
                self._proc.wait(timeout=10.0)
            except subprocess.TimeoutExpired:
                logger.info("Timeout expired, killing child process...")
                self._proc.kill()
            self._proc = None

    def list_jobs(self):
        jobs = []
        for job_file in os.listdir(self._job_dir.name):
            path = os.path.join(self._job_dir.name, job_file)
            if not os.path.isfile(path):
                continue
            match = self.JOB_FILE_REGEX.match(job_file)
            if match:
                jobs.append(ntpl(suffix=match.groups(1)[0], path=path))
        return sorted(jobs)

    def list_builds(self):
        builds = []
        for build_file in os.listdir(self._out_dir.name):
            path = os.path.join(self._out_dir.name, build_file)
            if not os.path.isfile(path):
                continue
            match = self.BUILD_FILE_REGEX.match(build_file)
            if match:
                builds.append(
                    ntpl(suffix=match.groups(1)[0],
                         status=match.groups(1)[1],
                         path=path))
        return builds

    def aggregate_jobs_and_builds(self):
        jobs, builds, res = self.list_jobs(), self.list_builds(), {}
        for job in jobs:
            res[job.suffix] = ntpl(status="queued",
                                   id=job.suffix,
                                   time=int(job.suffix, base=16),
                                   output=None)
        for build in builds:
            res[build.suffix] = ntpl(status=build.status,
                                     id=build.suffix,
                                     time=int(build.suffix, base=16),
                                     output=build.path)
        return res

    def delete_job_file(self, job_file_path):
        # Deletes the job file at the given path
        try:
            logger.debug("Deleting job file %s", job_file_path)
            os.unlink(job_file_path)
        except OSError as e:
            logger.error(str(e))

    def fetch_newest_job(self, jobs=None, skip_obsolete=True):
        # Fetch the job files
        jobs = self.list_jobs() if jobs is None else jobs

        # If so desired, skip obsolete jobs and mark obsolete jobs for deletion
        obsolete_jobs, data, res = [], None, None
        for i in range(len(jobs)):
            try:
                with open(jobs[i].path, 'r') as f:
                    data = json.load(f)
                if not res is None:
                    obsolete_jobs.append(res.path)
                res = ntpl(data=data, path=jobs[i].path, suffix=jobs[i].suffix)
                if not skip_obsolete:
                    break
            except (json.JSONDecodeError, OSError, KeyError) as e:
                logger.error(str(e))
                obsolete_jobs.append(jobs[i].path)

        # Delete all the obsolete jobs
        for path in obsolete_jobs:
            self.delete_job_file(path)

        return res

    def execute_job(self, job):
        import select

        # Function used to generate the possible output file names
        mk_out_file = lambda x: os.path.join(
            self._out_dir.name, "out_" + job.suffix + ".{}.txt".format(x))
        proc, out_file = None, None

        # Create a pipe for stdout/stderr redirection.
        p_rd, p_wr = os.pipe()
        try:
            # Assemble the target environment. Discard all variables but "PATH".
            # This will make sure that none of the secrets stored in environment
            # variables are visible to the launched subprocess.
            environ = {}
            if "PATH" in os.environ:
                environ["PATH"] = os.environ["PATH"]

            # Open the target file, as well as a pip to which we redirect stdout
            # and stderr. Then open a process connected to that file.
            output, out_file = [bytes()], mk_out_file("running")
            logger.debug("Executing subprocess [%s], writing to \"%s\"",
                         ", ".join(job.data["args"]), out_file)
            t0, has_timeout = time.time(), False
            with open(out_file, "wb") as f, \
                 subprocess.Popen(job.data["args"],
                                  env=environ,
                                  stdout=p_wr,
                                  stderr=p_wr,
                                  stdin=subprocess.DEVNULL) as proc:

                # Helper function used to write to both the output buffer and
                # the output file
                def append_to_output(buf):
                    output[0] += buf
                    f.write(buf)
                    f.flush()

                # Try to read output until both the process is dead and there is
                # no more data to read
                had_data_last_time = False
                while (proc.poll() is None) or had_data_last_time:
                    had_data_last_time = False

                    # Time-out after ten minutes
                    if time.time() - t0 > self._timeout:
                        proc.kill()
                        has_timeout = True
                        append_to_output(b"\n\nTimeout.\n")
                        break

                    # Wait for the output pipe to become readable. Check whether the
                    # subprocess still exists at least every 0.1 seconds.
                    rds, _, _ = select.select([p_rd], [], [], 0.1)
                    if len(rds) == 0:
                        continue

                    # Load all available data from the output pipe
                    buf = os.read(p_rd, 8192)
                    if len(buf) > 0:
                        append_to_output(buf)
                        had_data_last_time = True

                if not has_timeout:
                    append_to_output(
                        "\n\nExecution took {:0.1f}s, exit code {}\n".format(
                            time.time() - t0, proc.returncode).encode("utf-8"))

            return proc.returncode, output[0]

        except KeyError as e:
            logger.error("Invalid job descriptor: " + str(e))
        except OSError as e:
            logger.error("Error while executing the task: " + str(e))
        finally:
            # Make sure that the pipe is closed
            os.close(p_rd)
            os.close(p_wr)

            # Make sure that the output file is either deleted, or, based on
            # the process output, renamed to a file name indicating either
            # success or failure
            if (not out_file is None) and os.path.isfile(out_file):
                if proc is None:
                    logger.debug("Failure while executing the subprocess.")
                    os.unlink(out_file)
                elif (has_timeout) or (proc.poll() is None):
                    logger.debug("Timeout while executing the subprocess.")
                    os.rename(out_file, mk_out_file("timeout"))
                elif proc.returncode == 0:
                    logger.debug("Subprocess exited successfully")
                    os.rename(out_file, mk_out_file("success"))
                else:
                    logger.debug("Subprocess with an error code")
                    os.rename(out_file, mk_out_file("failure"))

    def queue_job(self,
                  args,
                  commit_id="",
                  repository_name="",
                  url="",
                  email_to=[]):
        # Generate the output file
        job_file_path = os.path.join(self._job_dir.name,
                                     "job_{:020x}.json".format(time.time_ns()))

        # Create a temporary file in the job directory and write the job
        # descriptor to that file. Then, in a last (atomic) step rename that
        # file to a valid job file that can be picked up by the job runner.
        can_delete_tmp_file, f = True, None
        try:
            # Write to the temporary job file
            with TmpFile(mode="w", dir=self._job_dir.name, delete=False) as f:
                json.dump(
                    {
                        "args": args,
                        "commit_id": commit_id,
                        "repository_name": repository_name,
                        "url": url,
                        "email_to": email_to
                    }, f)

            # Once writing has finished, expose the job file at the final
            # location.
            os.rename(f.name, job_file_path)
            can_delete_tmp_file = False
        except OSError as e:
            logger.error(e)
        finally:
            # If something goes wrong, delete the created temporary file
            if (not f is None) and can_delete_tmp_file:
                os.unlink(f.name)

    def is_child_running(self):
        return (not self._proc is None) and (self._proc.poll() is None)

    def check_queue_and_spawn(self):
        if (len(self.list_jobs()) > 0) and not self.is_child_running():
            args = list(
                filter(bool, [
                    sys.executable, __file__, "child", self._job_dir.name,
                    self._out_dir.name, "--verbose" if self._verbose else None,
                    "--timeout",
                    str(self._timeout)
                ]))
            logger.debug("Spawning child process: [%s]", ", ".join(args))
            self._proc = subprocess.Popen(args, stdin=subprocess.DEVNULL)


###############################################################################
# Server main program                                                         #
###############################################################################


def construct_argparse():
    parser = argparse.ArgumentParser(
        description="GitHub webhook endpoint server. Runs a specified script "
        "when receiving a push web hook request and provides a simple web "
        "interface.")
    parser.add_argument(
        "--bind",
        default="127.0.0.1",
        type=str,
        required=False,
        help="Network address to bind the server to. This script should only "
        "be used in conjunction with a reverse proxy such as NGINX.")
    parser.add_argument("--port",
                        default=22472,
                        required=False,
                        help="Network port to bind the server to.")
    parser.add_argument(
        "--job_dir",
        default=None,
        required=False,
        help="Directory in which queued job descriptors are stored")
    parser.add_argument("--out_dir",
                        default=None,
                        required=False,
                        help="Directory in which job outputs are stored")
    parser.add_argument(
        "--repository",
        default="?",
        required=False,
        help="Repository name to be displayed on the status page")
    parser.add_argument(
        "--url",
        default="",
        type=str,
        required=False,
        help="Public base URL at which the webserver is located")
    parser.add_argument(
        "--branch",
        default="",
        type=str,
        required=False,
        help="If specified, only reacts to pushes to a specific branch.")
    parser.add_argument(
        "--no-secret",
        action="store_true",
        help="Must be set to confirm that request authentication is disabled.")
    parser.add_argument(
        "--script",
        default="/usr/bin/true",
        type=str,
        required=False,
        help=
        "Path pointing at the script that should be executed when a WebHook "
        "request is received. Leave empty to disable request auth")
    parser.add_argument(
        "--send_email",
        action="store_true",
        help="Send an email with the script output to the person initiating")
    parser.add_argument("--verbose",
                        action="store_true",
                        help="If specified, sets the log level to \"DEBUG\".")
    parser.add_argument("--timeout",
                        default=600.0,
                        type=float,
                        required=False,
                        help="Maximum sub-process execution time.")

    return parser


def main():
    # Make sure TCP servers can quickly reuse the port after the application
    # exits
    import socketserver
    socketserver.TCPServer.allow_reuse_address = True

    # Parse the command line
    args = construct_argparse().parse_args()

    # Increase the verbosity
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Assemble a URL if none is given
    if not args.url:
        args.url = "http://{}:{}".format(args.bind, args.port)
    while args.url.endswith("/"):
        args.url = args.url[:-1]

    # Make sure that the GitHub webhook secret is found in the environment
    # variables OR that "no_secret" is set
    secret = None
    if not "GITHUB_SECRET" in os.environ:
        if not args.no_secret:
            logger.error(
                "The GITHUB_SECRET environment variable is not set, but --no_secret was not specified."
            )
            return 1
    else:
        secret = os.environ["GITHUB_SECRET"].encode("utf-8")

    # Create a temporary directory for jobs and output files
    with JobRunner(job_dir=args.job_dir, out_dir=args.out_dir, timeout=args.timeout, verbose=args.verbose) as runner:
        logger.debug("Job directory: %s", runner._job_dir.name)
        logger.debug("Output directory: %s", runner._out_dir.name)

        # Construct the webserver
        Server = _construct_http_server_class(args, runner, secret)
        with socketserver.TCPServer((args.bind, args.port), Server) as httpd:
            # Setup a one second timeout -- if no requests are received, check
            # whether there are any outstanding requests. If yes, start the
            # job runner process. This is necessary because the parent may
            # decide that the job runner is still active, not spawning a new
            # job runner, when in fact the job runner was just exiting.
            httpd.timeout = 1.0
            httpd.handle_timeout = lambda: runner.check_queue_and_spawn()

            # Wait for the webserver to exit
            logger.info("Serving on http://{}:{}/".format(
                args.bind, args.port))
            try:
                while True:
                    httpd.handle_request()
            except KeyboardInterrupt:
                pass

    return 0


###############################################################################
# Task runner main program                                                    #
###############################################################################


def child_construct_argparse():
    parser = argparse.ArgumentParser(
        description="Task runner used internally by the webhook server.")
    parser.add_argument("job_dir", type=str)
    parser.add_argument("out_dir", type=str)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--timeout", type=float)

    return parser


EMAIL_SUBJECT = "Commit {commit_id} to {repository_name} failed"

EMAIL_BODY = """Hi!

One of your recent Git commits ({commit_id}) to the repository \"{repository_name}\" triggered an automated build job. Regrettably, that build job failed with return code {returncode}. For more information, please see the log below or visit

{url}/status

After you've identified and fixed the problem, simply push another revision to the \"{repository_name}\" Git repository.

Thank you!

---------------------------

{log}

"""


def child_send_failure_email(job, returncode, output):
    import textwrap
    import smtplib
    from email.message import EmailMessage

    # Read the mail-server configuration from the environment
    ok = True
    for var in ["SMTP_SERVER", "SMTP_USER", "SMTP_PASSWORD", "SMTP_PORT"]:
        if not var in os.environ:
            ok = False
            logger.error("Mail server configuration not found in environment; "
                         "missing environment variable \"{}\"".format(var))
    if not ok:
        return

    # Fetch the SMTP configuration options
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_user = os.environ["SMTP_USER"]
    smtp_password = os.environ["SMTP_PASSWORD"]
    smtp_port = int(os.environ["SMTP_PORT"])

    # Assemble the log message. Eliminate any ANSI escape sequences that
    # may be used by a program to format the terminal output.
    log = ""
    lines = remove_ansi(str(output, "utf-8")).split("\n")
    if len(lines) > 100:
        log += "[...]\n"
    for i, line in enumerate(lines):
        if i > len(lines) - 100:
            line = "{:>4d}: ".format(i + 1) + line
            log += line + "\n"

    # Fill the individual components into the email body.
    email_body = EMAIL_BODY.format(repository_name=job.data["repository_name"],
                                   commit_id=job.data["commit_id"],
                                   url=job.data["url"],
                                   log=log,
                                   returncode=returncode)

    # Assemble the email message
    msgs = []
    for receiver in job.data["email_to"]:
        msg = EmailMessage()
        msg.set_content(email_body)
        msg["To"] = receiver
        msg["From"] = smtp_user
        msg["Subject"] = EMAIL_SUBJECT.format(
            repository_name=job.data["repository_name"],
            commit_id=job.data["commit_id"])
        msgs.append((receiver, msg))

    # Actually send the email via SMTP
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            # Connect to the server via TLS
            smtp.starttls()
            logger.debug("Logging into SMTP server...")
            smtp.login(smtp_user, smtp_password)

            # Send the actual emails
            for i, (receiver, msg) in enumerate(msgs):
                # Do some rate-limiting when sending multiple emails
                if i > 0:
                    time.sleep(1.0)

                # Send the actual message
                logger.info("Sending email to %s", receiver)
                smtp.send_message(msg)
        logger.debug("Sucessfully closed SMTP session.")
    except smtplib.SMTPException as e:
        logger.error("SMTP error: " + str(e))


def child_main():
    # Parse the command line arguments
    args = child_construct_argparse().parse_args(sys.argv[2:])

    # Increase the verbosity
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Construct the JobRunner instance -- this will essentially be identical
    # to the JobRunner instance used in the main process
    with JobRunner(args.job_dir, args.out_dir, args.timeout) as runner:
        # Iterate over the job directory and fetch the newest job, where "newest"
        # corresponds to the job file with the highest hexadecimal suffix.
        while True:
            job = runner.fetch_newest_job()
            if not job:
                break
            try:
                logger.debug("Processing job {}".format(job.path))
                returncode, output = runner.execute_job(job)
                if (returncode != 0) and ("email_to" in job.data) and (len(
                        job.data["email_to"]) > 0):
                    logger.debug("Sending failure emails...")
                    child_send_failure_email(job, returncode, output)
            finally:
                # No matter what, make sure the job file is deleted. Otherwise
                # the job runner may be caught in an infinite loop.
                runner.delete_job_file(job.path)

    return 0


###############################################################################
# Main entry point                                                            #
###############################################################################

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(format='[%(levelname)s] %(message)s',
                        level=logging.INFO)

    # Continue as a child process if "child" is given as a second argument
    if (len(sys.argv) >= 2) and (sys.argv[1] == "child"):
        sys.exit(child_main())
    else:
        sys.exit(main())

