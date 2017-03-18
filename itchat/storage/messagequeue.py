try:
    import Queue as queue
except ImportError:
    import queue

class Queue(queue.Queue):
    def put(self, message):
        queue.Queue.put(self, Message(message))

class Message(dict):
    def download(self, fileName):
        if hasattr(self.text, '__call__'):
            return self.text(fileName)
        else:
            return b''
    def __getattr__(self, value):
        value = value[0].upper() + value[1:]
        return self.get(value, '')
    def __str__(self):
        return '{%s}' % ', '.join(
            ['%s: %s' % (repr(k),repr(v)) for k,v in self.items()])
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__.split('.')[-1],
            self.__str__())
