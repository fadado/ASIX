#!/usr/bin/python

'''Test CGI script.

Can be executed as a standalone script or imported into the other modules.
'''

__all__ = ["dump_all_data"]

import os
import sys

def dump_all_data(banner=''):
    '''Dump all CGI data as HTTP text response'''

    write = sys.stdout.write
    environ = os.environ

    write("Content-Type: text/plain; charset=%s\r\n" % (get_encoding()))
    write("\r\n")

    # print banner
    if banner: 
        write("%s\nENVIRONMENT\n%s\n" % (banner, banner))

    # dump environment
    for k in sorted(environ.keys()):
        write("%s=%s\n" % (k, environ[k].rstrip()))

    # dump input
    if environ['REQUEST_METHOD'] == 'POST':
        if banner: 
            write("%s\nBODY\n%s\n" % (banner, banner))
        nbytes = int(environ['CONTENT_LENGTH'])     # n. of bytes to read
        write("%s\n" % (sys.stdin.read(nbytes)))    # read stdin

def get_encoding():
    try:
        lang = os.environ['LANG']
        encoding = lang[lang.index('.') + 1 :]
    except:
        encoding = 'UTF-8'
    return encoding

if __name__ == '__main__':
    dump_all_data('-' * 60)
    sys.exit(0)

# vim:sw=4:ts=4:ai:et
