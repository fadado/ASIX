#!/usr/bin/python

'''Test CGI script.
'''

import sys
import cgi

# Debug
#import cgitb; cgitb.enable()

write = sys.stdout.write

form = cgi.FieldStorage()

# headers
write("Content-Type: text/plain; charset=UTF-8\r\n") # or "text/html"...
write("\r\n")

# body
for k in form:
    print k, "==>", form.getvalue(k)

sys.exit(0)

# vim:sw=4:ts=4:ai:et
