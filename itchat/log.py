import logging

logger = logging.getLogger('itchat')

logger.setLevel(logging.DEBUG)

cmdHandler = logging.StreamHandler()
cmdHandler.setLevel(logging.DEBUG)

logger.addHandler(cmdHandler)
