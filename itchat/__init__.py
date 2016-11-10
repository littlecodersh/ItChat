from .core import Core
from . import content

__version__ = '1.1.21'

instanceList = []

def new_instance():
    newInstance = Core()
    instanceList.append(newInstance)
    return newInstance

originInstance = new_instance()

# I really want to use sys.modules[__name__] = originInstance
# but it makes auto-fill a real mess, so forgive me for my following **

import sys
sys.modules[__name__] = originInstance
