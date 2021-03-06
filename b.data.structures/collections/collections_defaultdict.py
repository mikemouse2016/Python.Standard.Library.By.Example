#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Initializing a defaultdict.
"""

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='hello world')
print 'd:', d
print 'foo =>', d['foo']
print 'bar =>', d['bar']
