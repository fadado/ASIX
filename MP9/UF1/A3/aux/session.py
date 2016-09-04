"""HTTP session management using cookies
"""

import atexit
import os
import time
import shelve
from uuid import uuid1

__all__ = (
        "request_cookies",
        "response_cookie",
        "load",
)

_DATE_FORMAT = "%a, %d-%b-%Y %H:%M:%S GMT"

# directory for file sessions
_SESSIONS = "/var/tmp/sessions"
# Recorda que apache per defecte usa /var/tmp privat!

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

def load():
    """Load a shelve dictionary for current session."""

    def uniqueID():
        """Return a unique universal ID."""
        return uuid1().hex

    if not os.path.exists(_SESSIONS):
        try:
            os.mkdir(_SESSIONS, 02770)
        # If the apache user can't create you must create it manualy
        except OSError, excpt:
            errmsg = "%s when trying to create the session directory. \
Create it as '%s'" % (excpt.strerror, os.path.abspath(_SESSIONS))
            raise OSError, errmsg
    #
    cookies = request_cookies()
    if cookies is not None and "SID" in cookies:
        file_name = _SESSIONS + "/" + cookies["SID"] + ".db"
        data = shelve.open(file_name, writeback=True)
        atexit.register(data.close)
        return data
    else:
        sid = uniqueID()
        file_name = _SESSIONS + "/" + sid + ".db"
        data = shelve.open(file_name, writeback=True)
        atexit.register(data.close)
        data["SID"] = sid
        return data

# vim:sw=4:ts=4:ai:et
