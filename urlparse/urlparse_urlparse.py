#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parsing URLs
"""

from urlparse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print parsed
