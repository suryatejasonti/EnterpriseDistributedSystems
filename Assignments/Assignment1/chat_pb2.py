# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='spartanchat',
  syntax='proto3',
  serialized_pb=_b('\n\nchat.proto\x12\x0bspartanchat\"\x07\n\x05\x45mpty\"%\n\x07Message\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04note\x18\x02 \x01(\t\"\x18\n\x08UserName\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x8c\x01\n\x05Group\x12!\n\x02me\x18\x01 \x01(\x0b\x32\x15.spartanchat.UserName\x12\x30\n\x07\x66riends\x18\x02 \x03(\x0b\x32\x1f.spartanchat.Group.FriendsEntry\x1a.\n\x0c\x46riendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x32}\n\nChatServer\x12:\n\nReceiveMsg\x12\x14.spartanchat.Message\x1a\x14.spartanchat.Message0\x01\x12\x33\n\x07SendMsg\x12\x14.spartanchat.Message\x1a\x12.spartanchat.Empty2\xe7\x01\n\x04User\x12\x34\n\x07\x41\x64\x64User\x12\x15.spartanchat.UserName\x1a\x12.spartanchat.Empty\x12\x37\n\nRemoveUser\x12\x15.spartanchat.UserName\x1a\x12.spartanchat.Empty\x12\x37\n\x08GetUsers\x12\x12.spartanchat.Empty\x1a\x15.spartanchat.UserName0\x01\x12\x37\n\rFriendRequest\x12\x12.spartanchat.Group\x1a\x12.spartanchat.Groupb\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='spartanchat.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=34,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='spartanchat.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spartanchat.Message.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='spartanchat.Message.note', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=73,
)


_USERNAME = _descriptor.Descriptor(
  name='UserName',
  full_name='spartanchat.UserName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spartanchat.UserName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=99,
)


_GROUP_FRIENDSENTRY = _descriptor.Descriptor(
  name='FriendsEntry',
  full_name='spartanchat.Group.FriendsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='spartanchat.Group.FriendsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='spartanchat.Group.FriendsEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=242,
)

_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='spartanchat.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='me', full_name='spartanchat.Group.me', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friends', full_name='spartanchat.Group.friends', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GROUP_FRIENDSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=242,
)

_GROUP_FRIENDSENTRY.containing_type = _GROUP
_GROUP.fields_by_name['me'].message_type = _USERNAME
_GROUP.fields_by_name['friends'].message_type = _GROUP_FRIENDSENTRY
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['UserName'] = _USERNAME
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:spartanchat.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:spartanchat.Message)
  ))
_sym_db.RegisterMessage(Message)

UserName = _reflection.GeneratedProtocolMessageType('UserName', (_message.Message,), dict(
  DESCRIPTOR = _USERNAME,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:spartanchat.UserName)
  ))
_sym_db.RegisterMessage(UserName)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), dict(

  FriendsEntry = _reflection.GeneratedProtocolMessageType('FriendsEntry', (_message.Message,), dict(
    DESCRIPTOR = _GROUP_FRIENDSENTRY,
    __module__ = 'chat_pb2'
    # @@protoc_insertion_point(class_scope:spartanchat.Group.FriendsEntry)
    ))
  ,
  DESCRIPTOR = _GROUP,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:spartanchat.Group)
  ))
_sym_db.RegisterMessage(Group)
_sym_db.RegisterMessage(Group.FriendsEntry)


_GROUP_FRIENDSENTRY.has_options = True
_GROUP_FRIENDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_CHATSERVER = _descriptor.ServiceDescriptor(
  name='ChatServer',
  full_name='spartanchat.ChatServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=244,
  serialized_end=369,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReceiveMsg',
    full_name='spartanchat.ChatServer.ReceiveMsg',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMsg',
    full_name='spartanchat.ChatServer.SendMsg',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATSERVER)

DESCRIPTOR.services_by_name['ChatServer'] = _CHATSERVER


_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='spartanchat.User',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=372,
  serialized_end=603,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddUser',
    full_name='spartanchat.User.AddUser',
    index=0,
    containing_service=None,
    input_type=_USERNAME,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveUser',
    full_name='spartanchat.User.RemoveUser',
    index=1,
    containing_service=None,
    input_type=_USERNAME,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUsers',
    full_name='spartanchat.User.GetUsers',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USERNAME,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FriendRequest',
    full_name='spartanchat.User.FriendRequest',
    index=3,
    containing_service=None,
    input_type=_GROUP,
    output_type=_GROUP,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
