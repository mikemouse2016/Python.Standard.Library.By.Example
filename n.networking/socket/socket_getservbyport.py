#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Look up a service name by its port number.
"""

import socket
import urlparse

for port in [ 80, 443, 21, 70, 25, 143, 993, 110, 995 ]:
    print urlparse.urlunparse(
        (socket.getservbyport(port), 'example.com', '/', '', '', '')
        )