import subprocess

from flask_script import Manager, Server

from . import app
from .freezer import freezer


manager = Manager(app, with_default_commands=False)

manager.add_command('run', Server(host="0.0.0.0"))


@manager.command
def freeze(serve=False):
    """Freezes the static version of the website."""
    if serve:
        freezer.run(debug=True)
    else:
        print("Writing files to {}".format(freezer.root))
        n_urls = 0
        for entity in freezer.freeze_yield():
            n_urls += 1
            print("Processing {}".format(entity.url))
        print('Done. Built {} files.'.format(n_urls))


@manager.command
def up(destination):
    print ('### Freezing')
    freeze()
    print('### Uploading to', destination)
    subprocess.call(['rsync', '-Pah', '--del', freezer.root + '/', destination])


@manager.shell
def shell_context():
    from . import app, pages
    from .freezer import freezer
    return locals()


if __name__ == '__main__':
    manager.run()
