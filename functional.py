#!/usr/bin/env python3


seq = 'abcd'
fn = lambda c: chr(ord(c)+2)

map(fn, seq)
# is equal to (fn(c) for c in seq)


fn = lambda c: True if ord(c)>98 else False

filter(fn, seq)
# is equal to (c for c in seq if fn(c))


from functools import reduce

seq = (1,2,3,4)
initial = 1
fn = lambda a, b: a+b

reduce(fn, seq, initial)
# is equal to
# a = initial
# for b in seq:
#   a = fn(a, b)
# 
# visual representation:
# fn(*, x) -> **
# inputs: *, [x,x,x,x,x]
# reduce does this:
# fn(*, x) -> ** [x,x,x,x]
# fn(**, x) -> *** [x,x,x]
# fn(***, x) -> **** [x,x]
# ...
# until -> ******
# aka iterator reduced to len = 0


