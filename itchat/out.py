import sys

from . import config

def print_line(msg, oneLine = False):
    if oneLine:
        sys.stdout.write(' '*40 + '\r')
        sys.stdout.flush()
    else:
        sys.stdout.write('\n')
    sys.stdout.write(msg.encode(sys.stdin.encoding or 'utf8', 'replace'
        ).decode(sys.stdin.encoding or 'utf8', 'replace'))
    sys.stdout.flush()
