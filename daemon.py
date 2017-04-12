#coding=utf-8

# The daemon for ItChat
# By yyfleo

# Usage:
# Before running the program,you should change
# the command which in the dict called str.
# And then,you can run it like other python scripts.

import platform,os
sys=platform.system()

# In general,replace bot.py with your script file name
# and it will work.
str={"Windows":"bot.py","Linux":".\bot.py"}

try:
	while(1):os.system(str[sys])
except KeyError:
	print("Your operating system isn't suitable for the program.")
	exit(-1)
except KeyboardInterrupt:
	print("Bye~")
	exit(0)
