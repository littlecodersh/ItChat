from .core import Core
from . import content

__version__ = '1.1.21'

instanceList = []

def new_instance():
    newInstance = Core()
    instanceList.append(newInstance)
    return newInstance

originInstance = new_instance()
