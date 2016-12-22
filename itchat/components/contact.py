import os, time, re, io
import json, copy
import traceback, logging

import requests

from .. import config, utils
from ..returnvalues import ReturnValue

logger = logging.getLogger('itchat')

def load_contact(core):
    core.update_chatroom             = update_chatroom
    core.update_friend               = update_friend
    core.get_contact                 = get_contact
    core.get_friends                 = get_friends
    core.get_chatrooms               = get_chatrooms
    core.get_mps                     = get_mps
    core.set_alias                   = set_alias
    core.set_pinned                  = set_pinned
    core.add_friend                  = add_friend
    core.get_head_img                = get_head_img
    core.create_chatroom             = create_chatroom
    core.set_chatroom_name           = set_chatroom_name
    core.delete_member_from_chatroom = delete_member_from_chatroom
    core.add_member_into_chatroom    = add_member_into_chatroom

def update_chatroom(self, userName, detailedMember=False):
    if not isinstance(userName, list):
        userName = [userName]
    url = '%s/webwxbatchgetcontact?type=ex&r=%s' % (
        self.loginInfo['url'], int(time.time()))
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Count': len(userName),
        'List': [{
            'UserName': u,
            'ChatRoomId': '', } for u in userName], }
    chatroomList = json.loads(self.s.post(url, data=json.dumps(data), headers=headers
            ).content.decode('utf8', 'replace')).get('ContactList')
    if not chatroomList:
        return ReturnValue({'BaseResponse': {
                'ErrMsg': 'No chatroom found',
                'Ret': -1001, }})

    if detailedMember:
        def get_detailed_member_info(encryChatroomId, memberList):
            url = '%s/webwxbatchgetcontact?type=ex&r=%s' % (
                self.loginInfo['url'], int(time.time()))
            headers = {
                'ContentType': 'application/json; charset=UTF-8',
                'User-Agent' : config.USER_AGENT, }
            data = {
                'BaseRequest': self.loginInfo['BaseRequest'],
                'Count': len(memberList),
                'List': [{
                    'UserName': member['UserName'],
                    'EncryChatRoomId': encryChatroomId} \
                        for member in memberList], }
            return json.loads(self.s.post(url, data=json.dumps(data), headers=headers
                    ).content.decode('utf8', 'replace'))['ContactList']
        MAX_GET_NUMBER = 50
        for chatroom in chatroomList:
            totalMemberList = []
            for i in range(int(len(chatroom['MemberList']) / MAX_GET_NUMBER + 1)):
                memberList = chatroom['MemberList'][i*MAX_GET_NUMBER: (i+1)*MAX_GET_NUMBER]
                totalMemberList += get_detailed_member_info(chatroom['EncryChatRoomId'], memberList)
            chatroom['MemberList'] = totalMemberList

    update_local_chatrooms(self, chatroomList)
    r = [self.storageClass.search_chatrooms(userName=c['UserName'])
        for c in chatroomList]
    return r if 1 < len(r) else r[0]

def update_friend(self, userName):
    if not isinstance(userName, list):
        userName = [userName]
    url = '%s/webwxbatchgetcontact?type=ex&r=%s' % (
        self.loginInfo['url'], int(time.time()))
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Count': len(userName),
        'List': [{
            'UserName': u,
            'EncryChatRoomId': '', } for u in userName], }
    friendList = json.loads(self.s.post(url, data=json.dumps(data), headers=headers
            ).content.decode('utf8', 'replace')).get('ContactList')

    update_local_friends(self, friendList)
    r = [self.storageClass.search_friends(userName=f['UserName'])
        for f in friendList]
    return r if len(r) != 1 else r[0]

def update_info_dict(oldInfoDict, newInfoDict):
    '''
        only normal values will be updated here
    '''
    for k, v in newInfoDict.items():
        if any((isinstance(v, t) for t in (tuple, list, dict))):
            pass # these values will be updated somewhere else
        elif oldInfoDict.get(k) is None or v not in (None, '', '0', 0):
            oldInfoDict[k] = v

def update_local_chatrooms(core, l):
    '''
        get a list of chatrooms for updating local chatrooms
        return a list of given chatrooms with updated info
    '''
    for chatroom in l:
        # format new chatrooms
        utils.emoji_formatter(chatroom, 'NickName')
        for member in chatroom['MemberList']:
            utils.emoji_formatter(member, 'NickName')
            utils.emoji_formatter(member, 'DisplayName')
        # update it to old chatrooms
        oldChatroom = utils.search_dict_list(
            core.chatroomList, 'UserName', chatroom['UserName'])
        if oldChatroom:
            update_info_dict(oldChatroom, chatroom)
            #  - update other values
            memberList, oldMemberList = (c.get('MemberList', [])
                    for c in (chatroom, oldChatroom))
            if memberList:
                for member in memberList:
                    oldMember = utils.search_dict_list(
                        oldMemberList, 'UserName', member['UserName'])
                    if oldMember:
                        update_info_dict(oldMember, member)
                    else:
                        oldMemberList.append(member)
        else:
            oldChatroom = chatroom
            core.chatroomList.append(chatroom)
        # delete useless members
        if len(chatroom['MemberList']) != len(oldChatroom['MemberList']) and \
                chatroom['MemberList']:
            existsUserNames = [member['UserName'] for member in chatroom['MemberList']]
            delList = []
            for i, member in enumerate(oldChatroom['MemberList']):
                if member['UserName'] not in existsUserNames: delList.append(i)
            delList.sort(reverse=True)
            for i in delList: del oldChatroom['MemberList'][i]
        #  - update OwnerUin
        if oldChatroom.get('ChatRoomOwner') and oldChatroom.get('MemberList'):
            oldChatroom['OwnerUin'] = utils.search_dict_list(oldChatroom['MemberList'],
                'UserName', oldChatroom['ChatRoomOwner']).get('Uin', 0)
        #  - update isAdmin
        if 'OwnerUin' in oldChatroom and oldChatroom['OwnerUin'] != 0:
            oldChatroom['isAdmin'] = \
                oldChatroom['OwnerUin'] == int(core.loginInfo['wxuin'])
        else:
            oldChatroom['isAdmin'] = None
        #  - update self
        newSelf = utils.search_dict_list(oldChatroom['MemberList'],
            'UserName', core.storageClass.userName)
        oldChatroom['self'] = newSelf or copy.deepcopy(core.loginInfo['User'])
    return {
        'Type'         : 'System',
        'Text'         : [chatroom['UserName'] for chatroom in l],
        'SystemInfo'   : 'chatrooms',
        'FromUserName' : core.storageClass.userName,
        'ToUserName'   : core.storageClass.userName, }

def update_local_friends(core, l):
    fullList = core.memberList + core.mpList
    for friend in l:
        utils.emoji_formatter(friend, 'NickName')
        utils.emoji_formatter(friend, 'DisplayName')
        oldInfoDict = utils.search_dict_list(
            fullList, 'UserName', friend['UserName'])
        if oldInfoDict is None:
            oldInfoDict = copy.deepcopy(friend)
            if oldInfoDict['VerifyFlag'] & 8 == 0:
                core.memberList.append(oldInfoDict)
            else:
                core.mpList.append(oldInfoDict)
        else:
            update_info_dict(oldInfoDict, friend)

def update_local_uin(core, msg):
    '''
        content contains uins and StatusNotifyUserName contains username
        they are in same order, so what I do is to pair them together

        I caught an exception in this method while not knowing why
        but don't worry, it won't cause any problem
    '''
    uins = re.search('<username>([^<]*?)<', msg['Content'])
    usernameChangedList = []
    r = {
        'Type': 'System',
        'Text': usernameChangedList,
        'SystemInfo': 'uins', }
    if uins:
        uins = uins.group(1).split(',')
        usernames = msg['StatusNotifyUserName'].split(',')
        if 0 < len(uins) == len(usernames):
            for uin, username in zip(uins, usernames):
                if not '@' in username: continue
                fullContact = core.memberList + core.chatroomList + core.mpList
                userDicts = utils.search_dict_list(fullContact,
                    'UserName', username)
                if userDicts:
                    if userDicts.get('Uin', 0) == 0:
                        userDicts['Uin'] = uin
                        usernameChangedList.append(username)
                        logger.debug('Uin fetched: %s, %s' % (username, uin))
                    else:
                        if userDicts['Uin'] != uin:
                            logger.debug('Uin changed: %s, %s' % (
                                userDicts['Uin'], uin))
                else:
                    if '@@' in username:
                        update_chatroom(core, username)
                        newChatroomDict = utils.search_dict_list(
                            core.chatroomList, 'UserName', username)
                        newChatroomDict['Uin'] = uin
                    elif '@' in username:
                        update_friend(core, username)
                        newFriendDict = utils.search_dict_list(
                            core.memberList, 'UserName', username)
                        newFriendDict['Uin'] = uin
                    usernameChangedList.append(username)
                    logger.debug('Uin fetched: %s, %s' % (username, uin))
        else:
            logger.debug('Wrong length of uins & usernames: %s, %s' % (
                len(uins), len(usernames)))
    else:
        logger.debug('No uins in 51 message')
        logger.debug(msg['Content'])
    return r

def get_contact(self, update=False):
    if not update: return copy.deepcopy(self.chatroomList)
    url = '%s/webwxgetcontact?r=%s&seq=0&skey=%s' % (self.loginInfo['url'],
        int(time.time()), self.loginInfo['skey'])
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT, }
    r = self.s.get(url, headers=headers)
    tempList = json.loads(r.content.decode('utf-8', 'replace'))['MemberList']
    chatroomList, otherList = [], []
    for m in tempList:
        if m['Sex'] != 0:
            otherList.append(m)
        elif '@@' in m['UserName']:
            chatroomList.append(m)
        elif '@' in m['UserName']:
            # mp will be dealt in update_local_friends as well
            otherList.append(m)
    if chatroomList: update_local_chatrooms(self, chatroomList)
    if otherList: update_local_friends(self, otherList)
    return copy.deepcopy(chatroomList)

def get_friends(self, update=False):
    if update: self.get_contact(update=True)
    return copy.deepcopy(self.memberList)

def get_chatrooms(self, update=False, contactOnly=False):
    if contactOnly:
        return self.get_contact(update=True)
    else:
        if update: self.get_contact(True)
        return copy.deepcopy(self.chatroomList)

def get_mps(self, update=False):
    if update: self.get_contact(update=True)
    return copy.deepcopy(self.mpList)

def set_alias(self, userName, alias):
    oldFriendInfo = utils.search_dict_list(
        self.memberList, 'UserName', userName)
    if oldFriendInfo is None:
        return ReturnValue({'BaseResponse': {
            'Ret': -1001, }})
    url = '%s/webwxoplog?lang=%s&pass_ticket=%s' % (
        self.loginInfo['url'], 'zh_CN', self.loginInfo['pass_ticket'])
    data = {
        'UserName'    : userName,
        'CmdId'       : 2,
        'RemarkName'  : alias,
        'BaseRequest' : self.loginInfo['BaseRequest'], }
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, json.dumps(data, ensure_ascii=False).encode('utf8'),
        headers=headers)
    r = ReturnValue(rawResponse=r)
    if r: oldFriendInfo['RemarkName'] = alias
    return r

def set_pinned(self, userName, isPinned=True):
    url = '%s/webwxoplog?pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'])
    data = {
        'UserName'    : userName,
        'CmdId'       : 3,
        'OP'          : int(isPinned),
        'BaseRequest' : self.loginInfo['BaseRequest'], }
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, json=data, headers=headers)
    return ReturnValue(rawResponse=r)

def add_friend(self, userName, status=2, verifyContent='', autoUpdate=True):
    ''' Add a friend or accept a friend
        * for adding status should be 2
        * for accepting status should be 3
    '''
    url = '%s/webwxverifyuser?r=%s&pass_ticket=%s' % (
        self.loginInfo['url'], int(time.time()), self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Opcode': status, # 3
        'VerifyUserListSize': 1,
        'VerifyUserList': [{
            'Value': userName,
            'VerifyUserTicket': '', }],
        'VerifyContent': verifyContent,
        'SceneListCount': 1,
        'SceneList': 33, # [33]
        'skey': self.loginInfo['skey'], }
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, data=json.dumps(data), headers=headers)
    if autoUpdate: self.update_friend(userName)
    return ReturnValue(rawResponse=r)

def get_head_img(self, userName=None, chatroomUserName=None, picDir=None):
    ''' get head image
     * if you want to get chatroom header: only set chatroomUserName
     * if you want to get friend header: only set userName
     * if you want to get chatroom member header: set both
    '''
    params = {
        'userName': userName or chatroomUserName or self.storageClass.userName,
        'skey': self.loginInfo['skey'], }
    url = '%s/webwxgeticon' % self.loginInfo['url']
    if chatroomUserName is None:
        infoDict = self.storageClass.search_friends(userName=userName)
        if infoDict is None:
            return ReturnValue({'BaseResponse': {
                'ErrMsg': 'No friend found',
                'Ret': -1001, }})
    else:
        if userName is None:
            url = '%s/webwxgetheadimg' % self.loginInfo['url']
        else:
            chatroom = self.storageClass.search_chatrooms(userName=chatroomUserName)
            if chatroomUserName is None:
                return ReturnValue({'BaseResponse': {
                    'ErrMsg': 'No chatroom found',
                    'Ret': -1001, }})
            if chatroom['EncryChatRoomId'] == '':
                chatroom = self.update_chatroom(chatroomUserName)
            params['chatroomid'] = chatroom['EncryChatRoomId']
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.get(url, params=params, stream=True, headers=headers)
    tempStorage = io.BytesIO()
    for block in r.iter_content(1024):
        tempStorage.write(block)
    if picDir is None:
        return tempStorage.getvalue()
    with open(picDir, 'wb') as f: f.write(tempStorage.getvalue())
    return ReturnValue({'BaseResponse': {
        'ErrMsg': 'Successfully downloaded',
        'Ret': 0, }})

def create_chatroom(self, memberList, topic=''):
    url = '%s/webwxcreatechatroom?pass_ticket=%s&r=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'], int(time.time()))
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'MemberCount': len(memberList),
        'MemberList': [{'UserName': member['UserName']} for member in memberList],
        'Topic': topic, }
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, headers=headers,
        data=json.dumps(data, ensure_ascii=False).encode('utf8', 'ignore'))
    return ReturnValue(rawResponse=r)

def set_chatroom_name(self, chatroomUserName, name):
    url = '%s/webwxupdatechatroom?fun=modtopic&pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'ChatRoomName': chatroomUserName,
        'NewTopic': name, }
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, headers=headers,
        data=json.dumps(data, ensure_ascii=False).encode('utf8', 'ignore'))
    return ReturnValue(rawResponse=r)

def delete_member_from_chatroom(self, chatroomUserName, memberList):
    url = '%s/webwxupdatechatroom?fun=delmember&pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'ChatRoomName': chatroomUserName,
        'DelMemberList': ','.join([member['UserName'] for member in memberList]), }
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT}
    r = self.s.post(url, data=json.dumps(data),headers=headers)
    return ReturnValue(rawResponse=r)

def add_member_into_chatroom(self, chatroomUserName, memberList,
        useInvitation=False):
    ''' add or invite member into chatroom
     * there are two ways to get members into chatroom: invite or directly add
     * but for chatrooms with more than 40 users, you can only use invite
     * but don't worry we will auto-force userInvitation for you when necessary
    '''
    if not useInvitation:
        chatroom = self.storageClass.search_chatrooms(userName=chatroomUserName)
        if not chatroom: chatroom = self.update_chatroom(chatroomUserName)
        if len(chatroom['MemberList']) > self.loginInfo['InviteStartCount']:
            useInvitation = True
    if useInvitation:
        fun, memberKeyName = 'invitemember', 'InviteMemberList'
    else:
        fun, memberKeyName = 'addmember', 'AddMemberList'
    url = '%s/webwxupdatechatroom?fun=%s&pass_ticket=%s' % (
        self.loginInfo['url'], fun, self.loginInfo['pass_ticket'])
    params = {
        'BaseRequest'  : self.loginInfo['BaseRequest'],
        'ChatRoomName' : chatroomUserName,
        memberKeyName  : ','.join([member['UserName'] for member in memberList]), }
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT}
    r = self.s.post(url, data=json.dumps(params),headers=headers)
    return ReturnValue(rawResponse=r)
