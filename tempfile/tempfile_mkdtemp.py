#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tempfile

directory_name = tempfile.mkdtemp()
print directory_name
# Clean up the directory
os.removedirs(directory_name)
