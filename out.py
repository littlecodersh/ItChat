import sys
import config

def ErrorIgnore(fn, *args, **kwargs):
    def wrapped(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            return result
        except:
            print 'Encode Fail'
        return None
    return wrapped

@ErrorIgnore
def print_line(msg, oneLine = False):
    if oneLine:
        sys.stdout.write(' '*40 + '\r')
        sys.stdout.flush()
    else:
        sys.stdout.write('\n')
    sys.stdout.write(msg)
    sys.stdout.flush()
