#!/usr/bin/python

"""Expand genshi templates.

Usage: env N=V... python ./render.py TEMPLATE
"""

import os
import sys

from genshi.template import TemplateLoader

TEMPLATE = sys.argv[1]

TPATH = ["./", "/templates"] # directoris on cercar plantilles

loader = TemplateLoader(TPATH)

template = loader.load(TEMPLATE)

stream = template.generate(**os.environ)

sys.stdout.write(stream.render(encoding="UTF-8"))

sys.exit(0)

# vim:sw=4:ts=4:ai
