import time
from .client import client

__version__ = '0.1b'

__client = client()


def auto_login():
    return __client.auto_login()


# The following method are all included in auto_login >>>
def get_QRuuid():
    return __client.get_QRuuid()


def get_QR(uuid=None):
    return __client.get_QR(uuid)


def check_login(uuid=None):
    return __client.check_login(uuid)


def web_init():
    return __client.web_init()


def get_batch_contract(groupUserName):
    return __client.get_batch_contract(groupUserName)


def get_contract(update=False):
    return __client.get_contract(update)


def get_chatrooms(update=False):
    return __client.get_chatrooms(update)


def get_username(contract=None, remarkname=None, alias=None, nickname=None):
    """通过备注/微信号/昵称找到对应的username
    """
    return __client.get_username(contract, remarkname, alias, nickname)


def get_alias(contract=None, username=None):
    """通过username寻找微信号/备注/昵称/username,优先级一次递减
    """
    return __client.get_alias(contract, username)


def is_contract(username, contract=None):
    """判断username是否是好友
    """
    return __client.is_contract(username, contract)


def get_chatroom_contract(username):
    """获取群聊的联系人列表
    """
    return __client.get_chatroom_contract(username)


def set_oplog(username, rename):
    """设置备注
    """
    return __client.set_oplog(username, rename)


def show_mobile_login():
    return __client.show_mobile_login()


def start_receiving():
    return __client.start_receiving()
# <<<


# if toUserName is set to None, msg will be sent to yourself
def send_msg(msg='Test Message', toUserName=None):
    return __client.send_msg(msg, toUserName)


def send_file(fileDir, toUserName):
    return __client.send_file(fileDir, toUserName)


def send_img(fileDir, toUserName):
    return __client.send_image(fileDir, toUserName)


def add_friend(Status, UserName, Ticket):
    return __client.add_friend(Status, UserName, Ticket)


def create_chatroom(memberList, topic=''):
    return __client.create_chatroom(memberList, topic)


def delete_member_from_chatroom(chatRoomUserName, memberList):
    return __client.delete_member_from_chatroom(chatRoomUserName, memberList)


def add_member_into_chatroom(chatRoomUserName, memberList):
    return __client.add_member_into_chatroom(chatRoomUserName, memberList)


def send(msg, toUserName = None):
    if msg is None:
        return False
    elif msg[:5] == '@fil@':
        return __client.send_file(msg[5:], toUserName)
    elif msg[:5] == '@img@':
        return __client.send_image(msg[5:], toUserName)
    elif msg[:5] == '@msg@':
        return __client.send_msg(msg[5:], toUserName)
    else:
        return __client.send_msg(msg, toUserName)


# decorations
__functionDict = {'GroupChat': {}, 'GeneralReply': None}


def configured_reply():
    try:
        msg = __client.storageClass.msgList.pop()
        if msg.get('FromUserName') == msg.get('ToUserName'):
            pass  # 自己发消息忽略(IOS测试有安卓测试没有此BUG)
        else:
            if '@@' in msg.get('FromUserName'):
                replyFn = __functionDict['GroupChat'].get(msg['Type'], __functionDict['GeneralReply'])
                send(replyFn(msg), msg.get('FromUserName'))
            else:
                replyFn = __functionDict.get(msg['Type'], __functionDict['GeneralReply'])
                send(replyFn(msg), msg.get('FromUserName'))
    except IndexError:
        pass
    except TypeError:
        pass


def msg_register(_type = None, *args, **kwargs):
    if hasattr(_type, '__call__'):
        __functionDict['GeneralReply'] = _type
        return configured_reply
    elif _type is None:
        return configured_reply
    else:
        if not isinstance(_type, list):
            _type = [_type]
        def _msg_register(fn, *_args, **_kwargs):
            for msgType in _type:
                if kwargs.get('isGroupChat', False):
                    __functionDict['GroupChat'][msgType] = fn
                else:
                    __functionDict[msgType] = fn
        return _msg_register


# in-build run
def run():
    print('Start auto replying')
    while True:
        configured_reply()
        time.sleep(.3)

