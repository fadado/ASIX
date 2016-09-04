#!/usr/bin/python
# encoding: utf-8

"""Test CGI script with session.
"""

import os
import sys
import time
import session

import cgitb; cgitb.enable()

write = sys.stdout.write

# received cookies
cookies = session.request_cookies()
# load session
data = session.load()

# HTTP headers
if cookies is None or 'SID' not in cookies:
    write(session.response_cookie('SID', data['SID']))
write("Content-Type: text/html\r\n")
write("\r\n")

# response body
write("<html>\n<head><title>Cookie test</title></head>\n<body>\n")
if cookies is None or 'SID' not in cookies:
    write("<p>First visit or cookies disabled.</p>\n")
    data['VISITS'] = 1
else:
    if 'VISITS' not in data:    # file deleted?
        data['VISITS'] = 0
    data['VISITS'] += 1
    write("<p>Visit nº %s.</p>\n" % (data['VISITS']))
write("</body></html>\n")

sys.exit()

# vim:sw=4:ts=4:ai:et
