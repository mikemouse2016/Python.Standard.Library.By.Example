#!/usr/bin/env python
# -*- coding: utf-8 -*-

import compileall
import sys

sys.path[:] = ['examples', 'notthere']
print 'sys.path =', sys.path
compileall.compile_path()
