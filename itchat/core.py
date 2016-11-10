import requests

from . import config, storage, utils, log
from .components import load_components

class Core(object):
    def __init__(self):
        self.alive = False
        self.storageClass = storage.Storage()
        self.memberList = self.storageClass.memberList
        self.mpList = self.storageClass.mpList
        self.chatroomList = self.storageClass.chatroomList
        self.msgList = self.storageClass.msgList
        self.loginInfo = {}
        self.s = requests.Session()
        self.uuid = None
        self.debug = False
        self.functionDict = {'FriendChat': {}, 'GroupChat': {}, 'MpChat': {}}
        self.useHotReload, self.hotReloadDir = False, 'itchat.pkl'
        self.receivingRetryCount = 5
    def dump_login_status(self, fileDir):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def load_login_status(self, fileDir):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def auto_login(self, enableCmdQR=False, picDir=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_QRuuid(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_QR(self, uuid=None, enableCmdQR=False, picDir=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def check_login(self, uuid=None, picDir=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def web_init(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def update_chatroom(self, userName, detailedMember=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_contact(self, update=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_friends(self, update=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_chatrooms(self, update=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_mps(self, update=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def show_mobile_login(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def start_receiving(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __sync_check(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __get_msg(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __update_chatrooms(self, l):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __get_download_fn(self, url, msgId):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __produce_msg(self, l):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __produce_group_chat(self, msg):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def send_raw_msg(self, msgType, content, toUserName):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def send_msg(self, msg='Test Message', toUserName=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def __upload_file(self, fileDir, isPicture = False, isVideo = False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def send_file(self, fileDir, toUserName=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def send_image(self, fileDir, toUserName=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def send_video(self, fileDir, toUserName = None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def set_alias(self, userName, alias):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def add_friend(self, userName, status=2, ticket='', userInfo={}):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def get_head_img(self, userName=None, chatroomUserName=None, picDir=None):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def create_chatroom(self, memberList, topic = ''):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def set_chatroom_name(self, chatroomUserName, name):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def delete_member_from_chatroom(self, chatroomUserName, memberList):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def add_member_into_chatroom(self, chatroomUserName, memberList,
            useInvitation=False):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def configured_reply():
        ''' determine the type of message and reply if its method is defined
            however, I use a strange way to determine whether a msg is from massive platform
            I haven't found a better solution here
            The main problem I'm worrying about is the mismatching of new friends added on phone
            If you have any good idea, pleeeease report an issue. I will be more than grateful.
        '''
        raise NotImplementedError()
    def msg_register(msgType, isFriendChat=False, isGroupChat=False, isMpChat=False):
        ''' a decorator constructor
            return a specific decorator based on information given
        '''
        raise NotImplementedError()
    def run(debug=True):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def set_logging(self, showOnCmd=True, loggingFile=None, loggingLevel=10):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def log_out(self):
        ''' place for docs
         * will be initialized in messages
        '''
        raise NotImplementedError()
    def search_friends(self, name=None, userName=None, remarkName=None, nickName=None,
            wechatAccount=None):
        return self.storageClass.search_friends(name, userName, remarkName,
            nickName, wechatAccount)
    def search_chatrooms(self, name=None, userName=None):
        return self.storageClass.search_chatrooms(name, userName)
    def search_mps(self, name=None, userName=None):
        return self.storageClass.search_mps(name, userName)

load_components(Core)
