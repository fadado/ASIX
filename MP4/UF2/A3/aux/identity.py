#!/usr/bin/python
#
# Identity transform

import sys
import xml.etree.ElementTree as ET

# load
tree = ET.parse(sys.stdin)

# do nothing...

# save
tree.write(sys.stdout)

sys.exit(0)

# vim:sw=4:ts=4:ai:et
