import logging, traceback, sys, threading
try:
    import Queue
except ImportError:
    import queue as Queue

from ..log import set_logging
from ..utils import test_connect

logger = logging.getLogger('itchat')

def load_register(core):
    core.auto_login       = auto_login
    core.configured_reply = configured_reply
    core.msg_register     = msg_register
    core.run              = run

def auto_login(self, hotReload=False, statusStorageDir='itchat.pkl',
        enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):
    if not test_connect():
        logger.info("You don't have access to internet or wechat domain, so exit.")
        sys.exit()
    self.useHotReload = hotReload
    if hotReload:
        if self.load_login_status(statusStorageDir,
                loginCallback=loginCallback, exitCallback=exitCallback):
            return
        self.login(enableCmdQR=enableCmdQR, picDir=picDir, qrCallback=qrCallback,
            loginCallback=loginCallback, exitCallback=exitCallback)
        self.dump_login_status(statusStorageDir)
        self.hotReloadDir = statusStorageDir
    else:
        self.login(enableCmdQR=enableCmdQR, picDir=picDir, qrCallback=qrCallback,
            loginCallback=loginCallback, exitCallback=exitCallback)

def configured_reply(self):
    ''' determine the type of message and reply if its method is defined
        however, I use a strange way to determine whether a msg is from massive platform
        I haven't found a better solution here
        The main problem I'm worrying about is the mismatching of new friends added on phone
        If you have any good idea, pleeeease report an issue. I will be more than grateful.
    '''
    try:
        msg = self.msgList.get(timeout=1)
    except Queue.Empty:
        pass
    else:
        if msg['FromUserName'] == self.storageClass.userName:
            actualOpposite = msg['ToUserName']
        else:
            actualOpposite = msg['FromUserName']
        if '@@' in actualOpposite:
            replyFn = self.functionDict['GroupChat'].get(msg['Type'])
        elif self.search_mps(userName=msg['FromUserName']):
            replyFn = self.functionDict['MpChat'].get(msg['Type'])
        elif '@' in actualOpposite or \
                actualOpposite in ('filehelper', 'fmessage'):
            replyFn = self.functionDict['FriendChat'].get(msg['Type'])
        else:
            replyFn = self.functionDict['MpChat'].get(msg['Type'])
        if replyFn is None:
            r = None
        else:
            try:
                r = replyFn(msg)
                if r is not None: self.send(r, msg.get('FromUserName'))
            except:
                logger.debug(traceback.format_exc())

def msg_register(self, msgType, isFriendChat=False, isGroupChat=False, isMpChat=False):
    ''' a decorator constructor
        return a specific decorator based on information given '''
    if not isinstance(msgType, list): msgType = [msgType]
    def _msg_register(fn):
        for _msgType in msgType:
            if isFriendChat:
                self.functionDict['FriendChat'][_msgType] = fn
            if isGroupChat:
                self.functionDict['GroupChat'][_msgType] = fn
            if isMpChat:
                self.functionDict['MpChat'][_msgType] = fn
            if not any((isFriendChat, isGroupChat, isMpChat)):
                self.functionDict['FriendChat'][_msgType] = fn
    return _msg_register

def run(self, debug=False, blockThread=True):
    logger.info('Start auto replying.')
    if debug:
        set_logging(loggingLevel=logging.DEBUG)
    def reply_fn():
        try:
            while self.alive: self.configured_reply()
        except KeyboardInterrupt:
            if self.useHotReload: self.dump_login_status()
            self.alive = False
            logger.debug('itchat received an ^C and exit.')
            print('Bye~')
    if blockThread:
        reply_fn()
    else:
        replyThread = threading.Thread(target=reply_fn)
        replyThread.setDaemon(True)
        replyThread.start()
