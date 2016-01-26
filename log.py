import time
import config

LOG_DIR = config.LOG_DIR

def OpenLog(fn, *args, **kwargs):
	def wrapped(*args, **kwargs):
		with open('run.log', 'a') as f:
			result = fn(f, *args, **kwargs)
		return result
	return wrapped

@OpenLog
def log(f, msg, succeed = True):
	f.write('[%s]%s: %s\n'%(('SUCC' if succeed else 'FAIL'), time.ctime(), msg))
