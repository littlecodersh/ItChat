import os, platform

DIR = os.getcwd()
QR_DIR = 'log'
LOG_DIR = 'log'
PIC_DIR = os.path.join('storage', 'picture')
VID_DIR = os.path.join('storage', 'video')
REC_DIR = os.path.join('storage', 'recording')
ATT_DIR = os.path.join('storage', 'attachment')
ACC_DIR = os.path.join('storage', 'account')
for d in [QR_DIR, LOG_DIR, PIC_DIR, VID_DIR, REC_DIR, ATT_DIR, ACC_DIR]:
    if not os.path.exists(os.path.join(DIR, d)): os.makedirs(os.path.join(DIR, d))
BASE_URL = 'https://login.weixin.qq.com'
OS = platform.system() #Windows, Linux, Darwin

WELCOME_WORDS = 'Hello World!'
