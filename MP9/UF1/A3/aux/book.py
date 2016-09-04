"""Guests book management
"""

import shelve
import time

__all__ = (
    "open",
    "close",
    "insert",
    "keys",
    "reversed",
    "record",
    "reccount",
)

_book = None

def open():
    """Open the guests book for reading and writing. Create if necessary."""

    global _book
    _book = shelve.open("/var/tmp/guests-book.db", writeback=False)
    # Recorda que apache per defecte usa /var/tmp privat!

def close():
    """Close the guests book."""

    _book.close()

def insert(user_name, user_email, text):
    """Insert a new record in the guests book."""

    assert user_name != ""
    assert "@" in user_email
    assert "." in user_email
    assert text != ""

    r = dict(
            TIME=time.time(),
            NAME=user_name,
            EMAIL=user_email,
            TEXT=text,
    )
    _book[str(len(_book))] = r

def keys(start=0, size=-1):
    """Return the guests book primary keys in order of record's creation."""

    assert start >= 0
    assert start < len(_book) if len(_book) != 0 else start == 0
    assert size == -1 or size > 0

    stop = len(_book) if size == -1 else min(start + size, len(_book))
    if start >= stop:
        return () # empty iterator
    # else
    return xrange(start, stop)

def reversed(start=-1, size=-1):
    """Return the guests book primary keys in reversed order."""

    assert size == -1 or size > 0

    if start == -1:
        start = len(_book) - 1

    assert start >= -1 and start < len(_book)

    stop = -1 if size == -1 else max(start - size, -1)
    if start <= stop:
        return () # empty iterator
    # else
    return xrange(start, stop, -1)

def record(key):
    """Return one record from the guests book as a read-only dictionary or None."""

    assert key >= 0 and key < len(_book)

    return _book[str(key)]

def reccount():
    """Return number of records in guests book database."""

    return len(_book)

########################################################################
# test
########################################################################

if __name__ == "__main__":
    import sys
    book = sys.modules[__name__]

    def as_tuple(k):
        r = book.record(k)
        return (r["TIME"], r["NAME"], r["EMAIL"], r["TEXT"])

    book.open()
    for k in book.keys(): pass

    book.insert('Joan', 'joan@gmail.com', 'Que <&> guay!!!')
    book.insert('Josep', 'josep@gmail.com', 'Que <&> guay!!!')

    for k in book.keys():
        r = book.record(k)
        assert r['TIME']        # item exists and is not None
        assert r['NAME']
        assert r['EMAIL']
        assert r['TEXT']

    for k in book.reversed():
        (t, n, e, x) = as_tuple(k)
        print 'TIME:', time.ctime(t)
        print 'NAME:', n
        print 'EMAIL:', e
        print 'TEXT:', x
        print

    book.close()

# vim:sw=4:ts=4:ai:et
