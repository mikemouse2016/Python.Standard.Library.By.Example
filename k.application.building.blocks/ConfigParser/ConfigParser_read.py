#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reading a configuration file.
"""

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

print parser.get('bug_tracker', 'url')



