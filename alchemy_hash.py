# Base🜀 from Samuel Arbesman (2021)
# The function 'alchemy_hash' takes ASCII text and returns its SHA-256 hash using a subset of 32 alchemical symbols

import hashlib
from base64 import b32encode

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
alchemy_alphabet = '🜀🜁🜂🜹🜄🜅🜆🜇🜈🜉🜊🜋🝪🜍🜎🜏🝳🜑🜒🜓🜔🜕🜾🝈🜘🜲🜚🜛🜜🜝🜞🜟'

# creates a map from the Base32 alphabet to the alchemical one
alchemy_map = {}
for i,j in zip(alphabet,alchemy_alphabet):
  alchemy_map[i] = j
alchemy_map['='] = ''

def alchemy_hash(text):
  hashed = hashlib.sha256(text.encode('ascii')).hexdigest()
  b32 = b32encode(bytes.fromhex(hashed)).decode()
  alchemy_hash = ''.join(list(map(lambda x:alchemy_map[x],b32)))

  return alchemy_hash
