#!/usr/bin/env python3

import sys
import re

hexcolor = re.compile(r'#([a-fA-F0-9]{3,6})\b')

def render(col):
    old = col
    lc  = len(col)
    col = "".join([i*2 for i in col]) if lc == 3 else col
    try:
        col = int(col, 16)
    except ValueError:
        return '#'+ old
    else:
        return '#'+ old +\
        '\x1b[38;2;%d;%d;%dm🔴\x1b[0m' % (
            (col>>16) & 0xff, 
            (col>>8)  & 0xff, 
            (col>>0)  & 0xff)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sys.stdin
    else:
        lines = sys.argv[1:]
    for line in lines:
        line = re.sub(hexcolor, lambda match: render(match[1]), line)
        sys.stdout.write(line)
