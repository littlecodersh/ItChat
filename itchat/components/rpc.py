import logging
import six.moves.xmlrpc_server as rpc
import six.moves.xmlrpc_client as cli
import itchat.storage.templates as tpl
import itchat.returnvalues as rv
import threading
import types
import base64
import json

logger = logging.getLogger('itchat')

exported_functions = [
    # components.login
	'login',
	'get_QRuuid',
	'get_QR',
	'check_login',
	'web_init',
	'show_mobile_login',
	'start_receiving',
	'get_msg',
	'logout',

    # components.contact
    'update_chatroom',
    'update_friend',
    'get_contacts',
    'get_friends',
    'get_chatrooms',
    'get_mps',
	'set_alias',
	'set_pinned',
	'add_friend',
	'get_head_img',
	'create_chatroom',
	'set_chatroom_name',
	'delete_member_from_chatroom',
	'add_member_into_chatroom',

# components.messages
	'send_raw_msg',
	'send_msg',
	'upload_file',
	'send_file',
	'send_image',
	'send_video',
	'send',
	'revoke',

# components.hotreload
	'dump_login_status',
	'load_login_status',

# components.register
	'auto_login',
	'configured_reply',
	'msg_register',
	'run',

# other functions
	'search_friends',
	'search_chatrooms',
	'search_mps',
    'set_logging',
]


def dump_obj(marshaller, value, write, escape=cli.escape):
    write('<value><string>')
    write(escape(json.dumps(value)))
    write('</string></value>')


def register_types():
    cli.Marshaller.dispatch[tpl.Chatroom] = dump_obj
    cli.Marshaller.dispatch[tpl.ContactList] = dump_obj
    cli.Marshaller.dispatch[tpl.User] = dump_obj
    cli.Marshaller.dispatch[tpl.ChatroomMember] = dump_obj
    cli.Marshaller.dispatch[tpl.MassivePlatform] = dump_obj
    cli.Marshaller.dispatch[rv.ReturnValue] = dump_obj


def load_rpc(core):
    core.start_rpc_server = start_rpc_server


def start_rpc_server(self):
    server = rpc.SimpleXMLRPCServer(('localhost', 9000), allow_none=True)
    server.register_introspection_functions()
    for i in exported_functions:
        if hasattr(self, i):
            server.register_function(getattr(self, i))
    rpc_thread = threading.Thread(target=server.serve_forever, args=())
    rpc_thread.daemon = True
    logger.info('Starting RPC server')
    register_types()
    rpc_thread.start()
    self.rpc = server