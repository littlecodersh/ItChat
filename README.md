As itchat is multi-threaded, it's impossible to catch the internet errors it has produced. So I added some callbacks.

In core.functionDict, I added the key "Error" whose value is a list, where we may store error-handling functions.

Use '@itchat.error_register(True)' to register your error-handling function.

这玩意多线程导致我没法捕捉错误，所以搞了个回调。用@itchat.error_register(True)来注册你的错误处理函数。
