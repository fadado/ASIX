#!/usr/bin/python
#
# Transform tag names to lowercase

import sys
import xml.etree.ElementTree as ET

# load
tree = ET.parse(sys.stdin)

# transform
for element in tree.iter():
    element.tag = element.tag.lower()

# save
tree.write(sys.stdout)

sys.exit(0)

# vim:sw=4:ts=4:ai:et
