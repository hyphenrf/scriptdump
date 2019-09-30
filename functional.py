#!/usr/bin/env python3


seq = 'abcd'
fn = lambda c: chr(ord(c)+2)

map(fn, seq)
# is equal to (fn(c) for c in seq) -> generators and comprehension
# is also equal to normal code:
# newlist = []
# for c in seq:
#   c = fn(c)
#   newlist.append(c)


fn = lambda c: True if ord(c)>98 else False

filter(fn, seq)
# is equal to (c for c in seq if fn(c)) -> generators and comprehension
# is also equal to:
# newlist = []
# for c in seq:
#   if fn(c):
#       newlist.append(c)


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
# 
# fn(*, x) -> **
# inputs: *, [x,x,x,x,x]
# reduce does this:
# fn(*, x) -> ** [x,x,x,x]
# fn(**, x) -> *** [x,x,x]
# fn(***, x) -> **** [x,x]
# ...
# until -> ******
#
# aka iterator reduced to len = 0
#
# reduce takes a function with two inputs, a sequence of data, and a starting
# value.



# Notes:

# You can use methods as functions in higher order functions
map(str.upper, ['boi', 'man', 'jojo'])
# You can even use instance methods the same way
map([1,2,3,4,5,5].count, (0, 'boy', 5, 1)) # counts the occurrences of tuple 
                                           # items in the number list

# similar to (filter, reduce) are (groupby, accumulate)
# they have similar use pattern but return ALL data instead of the final result
#
# if a higher order function is the drilling machine and normal ones are drill
# heads, then we can partially evaluate/ curry a drill by sticking both
# together and putting them in a contrainer (variable) waiting to be used
# later.
# this is called lazy eval

shift = lambda fn, c, n: chr(ord(fn(c))+n)
upper = str.upper
lazy_shifted_upper = lambda c, n: shift(upper, c, n)

lazy_shifted_upper('a',5)

# I can even make this more powerful by using my lazy function in a higher
# order one

lazy_shifted_upper_5 = lambda c: lazy_shifted_upper(c, 5)
m = map(lazy_shifted_upper_5, ['a', 'b', 'c', 'd'])


# instead of using lambdas we can use partial from functools
# partial takes two functions and returns a partially evaluated one

from functools import partial

lazy_shifted_upper_5 = partial(shift, upper, n=5)

# partially applying a function is more or less this:
fn = lambda a, b: a+b
fn_2 = lambda a: fn(a, 2)
# So you don't rlly need to import partial if your application of it wasn't 
# more complicated than what a lambda can do.
# You can always still use def then, for clarity.



# CURRYING
# oh boy how exciting

# so the concept of currying is to turn a bunch of nested functions into
# a chain of function pipelines.
# Hy does this awesomely with the -> atomic operator(?)
# Check out Hy's documentation.

# We can kinda do it in python. Here's the how:
fsummed = lambda f: lambda a, b: sum(map(f, range(a, b))) # currying. abstracts 
                                                        # the need for nesting.
multiply = lambda a, b: a*b
mutiply_by2 = lambda a: multiply(2, a)
sumtiply = fsummed(multiply_by2) # takes a range, returns its multiplied sum
sumtiply(1, 11)
# another way:
fsummed(multiply_by2)(1, 11) # without giving the hybrid function a name.

# This is equiv to:
sum(map(lambda a: multiply(a, 2), range(1,11)))
# or
reduce(lambda a, b: a+b, map(lambda a: multiply(a, 2), range(1, 11)))

# Python's lambdas are ugly when it comes to readability so it's better to
# define your stuff outside then map it later
add = lambda a, b: a+b
mby2 = partial(multiply, 2)
itrr = range(1, 11)

reduce(add, map(mby2, itrr))

# Ah, much cleaner.
