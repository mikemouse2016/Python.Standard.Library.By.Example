#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate a base64 encoded HMAC signature.

"""

import base64
import hmac
import hashlib

with open('lorem.txt', 'rb') as f:
    body = f.read()

hash = hmac.new('secret-shared-key-goes-here', body, hashlib.sha1)
digest = hash.digest()
print base64.encodestring(digest)
