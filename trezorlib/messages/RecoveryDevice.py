# Automatically generated by pb2py
from trezorlib import protobuf as p
t = p.MessageType('RecoveryDevice')
t.wire_type = 45
t.add_field(1, 'word_count', p.UVarintType)
t.add_field(2, 'passphrase_protection', p.BoolType)
t.add_field(3, 'pin_protection', p.BoolType)
t.add_field(4, 'language', p.UnicodeType, default=u'english')
t.add_field(5, 'label', p.UnicodeType)
t.add_field(6, 'enforce_wordlist', p.BoolType)
RecoveryDevice = t