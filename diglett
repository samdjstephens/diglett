#!/usr/bin/env python
"""
Diglett

Usage:
    diglett tunnel <name>
    diglett close <name>
    diglett add <name> <ip> <port> [<localport>]

Options:
    tunnel - create an SSH tunnel
    close - close an SSH tunnel by name
    add - add a new tunnel configuration
    name - name identifier for tunnel
    ip - remote host port
    port - port to tunnel to
"""


import subprocess
import psutil
import docopt


configs = {
    "jenkins": {
        "hostname": "jenkins",
        "user": "sam",
        "port": 8080,
        "localport": 8080,
        "uid": "90ebb79f8d9342248ac938cca31b67fe"
    }
}


def tunnel(name):
    conf = configs[name]
    proc = subprocess.Popen(['ssh',
                             '-f',
                             '{user}@{hostname}'.format(**conf),
                             '-L',
                             '{localport}:localhost:{port}'.format(**conf),
                             '-N',
                             conf['uid']])
    print proc
    return


def close(name):
    conf = configs[name]
    tunnel_proc = None
    for proc in psutil.process_iter():
        try:
            cmdline = proc.cmdline()
        except psutil.Error:
            continue
        if (isinstance(cmdline, list) and
                len(cmdline) and cmdline[-1] == conf['uid']):
            tunnel_proc = proc
    try:
        tunnel_proc.kill()
    except AttributeError:
        print "Tunnel {} not open".format(name)


def add():
    return

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    if args['tunnel']:
        tunnel(args['<name>'])
    elif args['close']:
        close(args['<name>'])
    elif args['add']:
        add()
    else:
        raise NotImplementedError("Mode not implemented")
