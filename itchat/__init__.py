from . import content
from .core import Core
from .config import VERSION
from .log import set_logging

__version__ = VERSION

instanceList = []

def new_instance():
    newInstance = Core()
    instanceList.append(newInstance)
    return newInstance

originInstance = new_instance()

# I really want to use sys.modules[__name__] = originInstance
# but it makes auto-fill a real mess, so forgive me for my following **
# actually it toke me less than 30 seconds, god bless Uganda

# components.login
login                       = originInstance.login
get_QRuuid                  = originInstance.get_QRuuid
get_QR                      = originInstance.get_QR
check_login                 = originInstance.check_login
web_init                    = originInstance.web_init
show_mobile_login           = originInstance.show_mobile_login
start_receiving             = originInstance.start_receiving
get_msg                     = originInstance.get_msg
logout                      = originInstance.logout
# components.contact
update_chatroom             = originInstance.update_chatroom
update_friend               = originInstance.update_friend
get_contact                 = originInstance.get_contact
get_friends                 = originInstance.get_friends
get_chatrooms               = originInstance.get_chatrooms
get_mps                     = originInstance.get_mps
set_alias                   = originInstance.set_alias
set_pinned                  = originInstance.set_pinned
add_friend                  = originInstance.add_friend
get_head_img                = originInstance.get_head_img
create_chatroom             = originInstance.create_chatroom
set_chatroom_name           = originInstance.set_chatroom_name
delete_member_from_chatroom = originInstance.delete_member_from_chatroom
add_member_into_chatroom    = originInstance.add_member_into_chatroom
# components.messages
send_raw_msg                = originInstance.send_raw_msg
send_msg                    = originInstance.send_msg
upload_file                 = originInstance.upload_file
send_file                   = originInstance.send_file
send_image                  = originInstance.send_image
send_video                  = originInstance.send_video
send                        = originInstance.send
revoke                      = originInstance.revoke
# components.hotreload
dump_login_status           = originInstance.dump_login_status
load_login_status           = originInstance.load_login_status
# components.register
auto_login                  = originInstance.auto_login
configured_reply            = originInstance.configured_reply
msg_register                = originInstance.msg_register
run                         = originInstance.run
# other functions
search_friends              = originInstance.search_friends
search_chatrooms            = originInstance.search_chatrooms
search_mps                  = originInstance.search_mps
set_logging                 = set_logging
