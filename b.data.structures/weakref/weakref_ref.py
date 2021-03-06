#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example using weakref.ref to manage a reference to an object.
"""

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

obj = ExpensiveObject()
r = weakref.ref(obj)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'deleting obj'
del obj
print 'r():', r()
