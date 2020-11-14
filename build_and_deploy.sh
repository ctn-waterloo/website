#!/bin/bash

# This script is used to buid the website in the CI system. It replaces
# the old .travis.yml.
#
# The basic idea is the following: The build system is split into two
# phases. The "first stage" immutably resides on the build server. It
# simply downloads the Git repository with the website into a temporary
# directory and then proceeds to execute the "second stage" build script
# inside a disposable Docker sandbox.
#
# The second stage installs Python dependencies and performs the actual
# build. Once that is done, the first stage resumes and uploads the
# website to the webserver.
#
# This way the code in this repository is completely isolated from the rest of
# the build server. This is less meant as a security measure, and more to
# prevent the website code from accidentially breaking something.
#
# Note that changes to the "first stage" of the build script are not
# automatically reflected on the build server. The build script (as well as the
# webhook server) need to be manually updated by logging into the build
# server.
#
# Authors:
# 	Andreas Stöckel, 2020

# Exit if a command errors out
set -e

# Handy function for printing messages
msg() {
	echo -e "[build_and_deploy.sh:$STAGE]" $*
}

# cd into the directory this script resides in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

# Fetch the stage from the command line arguments. Default to "first".
STAGE=${1:-first}
if [ $STAGE = "first" ]; then
	# IMPORTANT: Changes to the first stage require manually updating
	#            the build script on the build server! They will NOT
	#            be reflected in the next CI run. This section just
	#            sets up the CI environment.
	msg "==> Entering first-stage build"

	# Create a random temporary directory
	TMP=$(mktemp -d -t cnrg_website_build_XXXXXXXXXX)

	# Make sure that the temporary directory is deleted when
	# this script exists, no matter what the reason is.
	trap 'rm -rf "$TMP"' EXIT

	# Create the directories used by pip. The PIP_CACHE
	# directory is kept at a separate, permanent location,
	# so the second stage doesn't need to re-download and
	# re-compile the pip dependencies all the time.
	PIP_CACHE=/tmp/docker_pip_cache
	if [ ! -d "$PIP_CACHE" ]; then
		msg "Creating pip cache directory"
		mkdir -p "$PIP_CACHE"
		chmod 700 "$PIP_CACHE"
	fi
	mkdir "$TMP/local"
	chmod 700 "$TMP/local"


	# Clone the website into the directory
	msg "Setting up website repository in $TMP"
	#rsync -a . "$TMP/repo"
	git clone https://github.com/ctn-waterloo/website "$TMP/repo" --depth 1

	# Launch the second stage script inside a Docker container
	msg "Launching Docker container with the second stage build script"
	docker run \
		-u "$(id -u):$(id -g)" \
		-v "$TMP/repo":/repo:z \
		-v "$TMP/local":/.local:z \
		-v "$PIP_CACHE":/.cache/pip:z \
		python:3.8-buster \
		/repo/build_and_deploy.sh second

	# Upload the compiled website
	msg "==> Re-entering first-stage build"
	if [ -d "$TMP/repo/ctn_waterloo/build" ]; then
		msg "Tunneling into the research network..."
		ssh ctnuser@ctn15.uwaterloo.ca -L 2223:compneuro.uwaterloo.ca:22 -N &
		SSH_PID=$!
		trap "kill $SSH_PID" EXIT
		sleep 2.0

		msg "Uploading website to the webserver"
		rsync -e "ssh -p 2223" -ahv --del "$TMP/repo/ctn_waterloo/build/" cnrglab@localhost:/home/cnrglab/public_html/
	else
		msg "Build directory not found!"
		exit 1
	fi
elif [ $STAGE = "second" ]; then
	# IMPORTANT: Changes in this section are immediately reflected in the
	#            next CI run.

	msg "==> Entering second-stage build"

	# XXX (2)
	exit 1

	# Install all requirements
	msg "Installing Python dependencies"
	pip install --user -r requirements.txt --progress-bar off --no-warn-script-location

	# Build the website and store the results in the "build" directory
	msg "Building the website"
	./manage.py freeze
fi
