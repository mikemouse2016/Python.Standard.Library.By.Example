#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bz2

lorem = open('lorem.txt', 'rt').read()
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print 'Decompressed matches lorem:', decompressed_matches

unused_matches = decompressor.unused_data == lorem
print 'Unused data matches lorem :', unused_matches
