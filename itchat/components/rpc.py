import base64
import io
import json
import logging
import threading
import types

import itchat.returnvalues as rv
import itchat.storage.templates as tpl
import six.moves.xmlrpc_client as cli
import six.moves.xmlrpc_server as rpc

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
    'recv',
]


def dump_obj(marshaller, value, write, escape=cli.escape):
    if isinstance(value, io.BytesIO):
        write('<value><base64>')
        encoded = base64.encodebytes(value.getvalue())
        write(encoded.decode('ascii'))
        write('</base64></value>')
    elif isinstance(value, int):
        write('<value><i8>')
        write('%d' % value)
        write('</i8></value>')
    else:
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
    cli.Marshaller.dispatch[io.BytesIO] = dump_obj
    cli.Marshaller.dispatch[int] = dump_obj


def load_rpc(core):
    core.start_rpc_server = start_rpc_server


def start_rpc_server(self, host, port):
    server = rpc.SimpleXMLRPCServer((host, port), logRequests=False, allow_none=True)
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
