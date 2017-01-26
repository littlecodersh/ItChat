# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:34:36 2017

@author: Quantum Liu
"""
import random
import time
import itchat#需要安装itchat包，可直接 pip install itchat

from itchat.content import *
 
itchat.auto_login(True)
friendList = itchat.get_friends(update=True)[1:]
terms=[0]*len(friendList)
uns=[]
for f in friendList:
    uns.append(f['UserName'])
def autoreply():
    wishlist=[u'鸡年大吉!',u'[鸡]',u'财源滚滚!',u'[微笑]',u'[红包]',u'谢谢,',u'[强]',u'[呲牙]']
    @itchat.msg_register(TEXT)
    def text_reply(msg):
        if terms[uns.index(msg['FromUserName'])]==0:#第一轮对话
            print 'term 0'
            terms[uns.index(msg['FromUserName'])]=1
            time.sleep(random.randint(5,30))
            text=u'谢谢![呲牙][强]'#第一轮对话回复文本
            return text
        elif  terms[uns.index(msg['FromUserName'])]==1:#第二轮对话
            print 'term 1'
            terms[uns.index(msg['FromUserName'])]=2
            time.sleep(random.randint(5,30))
            text=u'[福][红包][鸡]'#第一轮对话回复文本
            return text
        elif terms[uns.index(msg['FromUserName'])]>=2 and terms[uns.index(msg['FromUserName'])]<=4:#第n轮对话，根据wishlist随机组合回复内容,大于5轮就闭嘴
            terms[uns.index(msg['FromUserName'])]=terms[uns.index(msg['FromUserName'])]+1
            print 'term N'
            wish=u''
            for i in range(random.randint(0,5)):#长度随机
                wish=wish+wishlist[random.randint(0,7)]
            print  wish
            time.sleep(random.randint(5,30))            
            return wish
    
autoreply()
itchat.run()                
            
            