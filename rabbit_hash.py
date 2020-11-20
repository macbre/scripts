#!/usr/bin/env python3

# rabbitMQ password hashing algo as laid out in:
# http://lists.rabbitmq.com/pipermail/rabbitmq-discuss/2011-May/012765.html
#
# ./rabbit_hash.py MmMzMTc3MmQ5YjBhM2
# WghyhorCPOZZP1A2lx+BRhfmbx547YG1OWH3A7+zGstvtsO9

import base64
import os
import hashlib
import struct
import sys

# This is the password we wish to encode
password = sys.argv[1]

# 1.Generate a random 32 bit salt:
# This will generate 32 bits of random data:
salt = os.urandom(4)

# 2.Concatenate that with the UTF-8 representation of the plaintext password
tmp0 = salt + password.encode('utf-8')

# 3. Take the SHA256 hash and get the bytes back
tmp1 = hashlib.sha256(tmp0).digest()

# 4. Concatenate the salt again:
salted_hash = salt + tmp1

# 5. convert to base64 encoding:
pass_hash = base64.b64encode(salted_hash)

print(pass_hash.decode("utf-8"))
