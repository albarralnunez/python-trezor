# Automatically generated by pb2py
from trezorlib import protobuf as p
t = p.MessageType('PinMatrixAck')
t.wire_type = 19
t.add_field(1, 'pin', p.UnicodeType, flags=p.FLAG_REQUIRED)
PinMatrixAck = t