#coding=utf8
import sys

TRANSLATE = 'Chinese'
TRANSLATION = {}

class ReturnValue(dict):
    def __init__(self, returnValueDict={}):
        for k, v in returnValueDict.items(): self[k] = v
        if TRANSLATE:
            self['rawmsg'] = self.get('errmsg', '')
            self['errmsg'] = \
                TRANSLATION[TRANSLATE].get(self.get('errcode', '')) \
                or self.get('errmsg', u'没有errmsg')
            if not self['rawmsg']: self['rawmsg'] = self['errmsg']
    def __nonzero__(self):
        return self.get('errcode', -1) == 0
    def __bool__(self):
        return self.__nonzero__()
    def __str__(self):
        return '{%s}' % ', '.join(
            ['%s: %s' % (repr(k),repr(v)) for k,v in self.items()])
    def __repr__(self):
        return '<ItchatmpReturnValue: %s>' % self.__str__()

TRANSLATION = {
    'Chinese': {
        0: u'请求成功',
    },
}
