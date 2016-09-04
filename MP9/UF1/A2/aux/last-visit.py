#!/usr/bin/python

"""Test CGI script with one cookie.
"""

import os
import sys
import time
import session

write = sys.stdout.write

# HTTP headers
now = time.time()
write(session.response_cookie("LAST-VISIT", str(now)))
write("Content-Type: text/html\r\n")
write("\r\n")

# received cookies
cookies = session.request_cookies()

# response body
write("<html>\n<head><title>Cookie test</title></head>\n<body>\n")
write("<p>Current time: %f</p>" % (now))
if cookies is None:
    write("<p>First visit or cookies disabled.</p>\n")
else:
    write("<p>Received HTTP header: %s</p>\n" % (os.environ["HTTP_COOKIE"]))
    write("<dl\n")
    for (k, v) in cookies.iteritems():
        write("<dt>%s</dt><dd>%s</dd>\n" % (k, v))
    write("</dl\n")
write("</body></html>\n")

# vim:sw=4:ts=4:ai:et
