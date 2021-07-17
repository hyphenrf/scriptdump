#!/usr/bin/env python3
from time import process_time as timestamp
from functools import partial
from pprint import pprint


STEPS = 0

# most expensive algo; time complexity = O(2^n)
# it becomes nearly useless around the 40th fib number
def fib_rec(n):
    global STEPS 
    STEPS +=1
    return n if n in {1, 0} else fib_rec(n-1) + fib_rec(n-2)

# Memoization; time complexity = O(n) -- i think?
# Problem would be with space complexity = O(n) too
# Due to python limitations on recursion, only useful for ~1000 calls
# it's also a bit less efficient, less readable, and more code than iter
# advantage: doesn't affect state. See STEPS in output: each call uses the
# initial 0 steps value.
ncache = dict()
def fib_memo_rec(n):
    if n in ncache: return ncache[n]
    if n in {1, 0}: 
        value = n
    else: 
        global STEPS
        STEPS +=1
        value = fib_memo_rec(n-1) + fib_memo_rec(n-2)
    
    ncache[n] = value
    return value

# Normal looping; time complexity = O(n)
#                 space complexity = O(1)
# Always werks
# disadvantage: mutability, STEPS are for each call the sum of this call's
# steps + the previous calls. i.e. this function uses a STEPS variable it
# modified every time it gets called. (This is because while recursion is
# handled all at once, normal style functions are handled.. Normally.)
def fib_iter(n):
    if n in {1, 0, 5}: return n
    if n in {2, 3, 4}: return n-1
    else:
        a, b = 5, 8
        for i in range(5, n-1):
            global STEPS
            STEPS +=1
            print(STEPS, "step")
            a, b = b, a+b
        return b # because that's one step less (hence n-1 in range)

# Linear operation; time complexity = O(1) :P
# this is a higher order function that returns another function. The function
# is timed and can return time taken to execute any function that is casted
# inside of it.
def timecast(fn):
    def timed(*args):
        start = timestamp()
        fn(*args)
        end = timestamp()
        return end-start
    return timed

# This one works in the logic of my program, but it isn't as elegant of
# a solution.
def timeit(fn, x):
    start = timestamp()
    fn(x)
    end = timestamp()
    return end-start

# Nested looping; time complexity = O(n^2) :PP
def test(fn_tup, x_tup):
    d = dict()
    for fn in fn_tup:
        global STEPS
        STEPS = 0
        d[fn.__name__] = list()
        for x in x_tup:
            d[fn.__name__]+=[(f'{x}th', timeit(fn, x))]
            d[fn.__name__]+=[STEPS]
    return d


if __name__ == '__main__':
    pprint(test(
            (fib_iter, 
             #fib_rec, 
             fib_memo_rec),
            (2, 5, 10, 50, 500, 1000)))
