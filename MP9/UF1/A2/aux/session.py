"""HTTP simple cookies utilities
"""

import os
import time

_DATE_FORMAT = "%a, %d-%b-%Y %H:%M:%S GMT"

########################################################################
# exported functions
########################################################################

def request_cookies():
    """Return HTTP request cookies as a dictionary."""

    s = os.environ.get("HTTP_COOKIE") # header string with 1 or more cookies
    return None if s is None else dict(c.split("=", 1) for c in s.split("; "))

def response_cookie(key, value, expires=None):
    """Return HTTP response header for a cookie."""

    if expires is None:     # session cookie (expires closing the browser)
        return "Set-Cookie: %s=%s\r\n" % (key, value)
    elif expires <= 0:      # clear cookie (explicit expiration)
        t = time.strftime(_DATE_FORMAT, time.gmtime(0))
        return "Set-Cookie: %s=%s; expires=%s\r\n" % (key, value, t)
    else:                   # set expiration time in the future
        t = time.strftime(_DATE_FORMAT, time.gmtime(time.time() + expires))
        return "Set-Cookie: %s=%s; expires=%s\r\n" % (key, value, t)

########################################################################
# test
########################################################################

if __name__ == "__main__":
    print(request_cookies())
    print(response_cookie("SID", 1234)),
    print(response_cookie("SID", 5678, 0)),
    SECONDS_30_DAYS = 60*60*24*30
    print(response_cookie("SID", 12345678, SECONDS_30_DAYS)),

# vim:sw=4:ts=4:ai:et
