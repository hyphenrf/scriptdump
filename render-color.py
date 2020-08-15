#!/usr/bin/env python3

import sys

def rgb(col):
    col = col.strip("#\r\n\t \x0b\x0c")
    lc  = len(col)
    if not (lc == 6 or lc == 3):
        return None
    col = "".join([i*2 for i in col]) if lc == 3 else col
    try:
        col = int(col, 16)
    except ValueError:
        return None
    else:
        return (
            (col>>16) & 0xff, 
            (col>>8)  & 0xff, 
            (col>>0)  & 0xff
        )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        colors = sys.stdin.readlines()
    else:
        colors = sys.argv[1:]
    for i in colors:
        i = rgb(i)
        if not i: 
            continue
        sys.stdout.write("#%02X%02X%02X " % i)
        sys.stdout.write("\x1b[48;2;%d;%d;%dm   \x1b[0m\n" % i)
