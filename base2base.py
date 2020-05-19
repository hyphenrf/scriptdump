#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyleft © 2020 Hazem M. <h.taha@nu.edu.eg>
# Distributed under terms of the MIT license.

"""
Base2Base: 
a functional-style python program that converts any number from one
representation to another.

functional-style, liberally speaking, is either defining constants,
assigning variables within function scopes, or applying functions.

while procedures and loops are not part of a functional paradigm,
they are used here out of necessity where not doing so would be
fighting against the language itself. (for example, interactive loops)

PROGRAM STRUCTURE:
    Prompt user for a Number
        Number must be bin, oct, dec, or hex
    Prompt user for a Base
        Base must match Number
    Prompt user for an OutputBase

    Calculate the number and represents as OutputBase
    Print the output to console
"""



# globals --------------------------------------------------------------------

# two-way mapping for base<16 single-digit representations
HEXTABLE = dict(
    ( *map(lambda a: (str(a), a), range(0,10))
    , *map(lambda a: (chr(a+87), a), range(10,16))
    , *map(lambda a: (a,str(a)), range(0,10))
    , *map(lambda a: (a, chr(a+87)), range(10,16))))

# Largest number of digits for a fraction (to avoid infinite fractions)
MAX_FRACTION = 4



# primitive functions --------------------------------------------------------

# LISP-style pairs
# Pair = (a,b) where a,b can be value, Pair, List, or nil
# nil is ()
# A heterogenous List in LISP can be represented as recursively nested pairs
# It is thus a special-case of pairs

def nil():
    '''empty pair represents a null'''
    return ()

def cons(x: object, xs: "List" = nil()) -> "List":
    '''x:xs
    cons(a) -> (a,())
    cons(b, a) -> (b,(a,()))'''
    return x, xs

def car(xs: "List") -> object:
    '''car x:xs -> x'''
    return xs[0]

def cdr(xs: "List") -> "List":
    '''cdr x:xs -> xs'''
    return xs[1]
##

def flatten(xs: "List", rev: bool=False) -> str:
    '''
    xs is a pair created by a recursive cons. Like so (1,(2,()))
    Sometimes recursive calls are ran so that cons acts like xs:x or 
    in python terms (((),2),1)
    In those cases, flatten is ran with the rev flag as True to unpack
    properly.
    The output of flatten is a null-joined string of all elements.'''
    if xs != ():
        if rev:
            return flatten(car(xs),True) + str(cdr(xs))
        else:
            return str(car(xs)) + flatten(cdr(xs))
    else:
        return ""



# Calculations ---------------------------------------------------------------

# Recursive helpers:
def __d2B_w(number: float, base: int) -> "reversed List":
    '''__d2b_w(10.0, 2) -> (((((),1),0),1),0)'''
    if number > 0:
        return cons(
                __d2B_w(number // base, base),
                HEXTABLE[number % base])
    else:
        return nil()

def __d2B_f(number: float, base: int, a=0) -> "List":
    '''__d2b_f(0.625, 2) -> (1,(0,(1,(0,()))))'''
    if a < MAX_FRACTION:
        return cons(
                HEXTABLE[int(number * base)],
                __d2B_f(number * base % 1, base, a+1))
    else:
        return nil()

def __b2D_w(number: str, base:int) -> int:
    '''__b2D_w("1010", 2) -> 10 '''
    if number: 
        return HEXTABLE[number[0]]\
                * base ** (len(number)-1)\
                + __b2D_w(number[1:], base)
    else:
        return 0

def __b2D_f(number: str, base:int, a=1) -> float:
    '''__b2D_f("1010", 2) -> 0.625'''
    if number: 
        return HEXTABLE[number[0]]\
                * base ** -a\
                + __b2D_f(number[1:], base, a+1)
    else:
        return 0
##

# Converters
def _base2Dec(number: str, base: int, isfrac: bool=False) -> float:
    '''base2Dec takes a number and its base, and returns the correct decimal
    representation of it. 
    The way it's handled depends on the isfrac flag. 
    
    If the number is a fraction i.e. args are ("1010",2,True), 
    output will be 0.625
    If the same args were given but isfrac was set to False: ("1010",2,False),
    output will be a normal 10.0'''
    if isfrac:
        return __b2D_f(number, base)
    else:
        return float(__b2D_w(number, base))

def _dec2Base(number: float, base: int, isfrac: bool=False) -> str:
    '''dec2Base takes a decimal and the base it needs to be converted to, and 
    returns the number string representation in that base.
    The way it's handled depends on the isfrac flag.

    Sometimes in fractional base conversions, the fraction conversion algorithm
    can loop forever. To remedy that, we will only convert MAX_FRACTION number
    of places. MAX_FRACTION is defined as a constant in this module.'''
    if isfrac:
        return flatten(__d2B_f(number, base)).rstrip("0")
    else:
        return flatten(__d2B_w(number, base), rev=True)
##

# The calculation process: Basefrm -> Decimal(to calculate on) -> Baseto
def numTo(numStr: str, basefrm: int, baseto: int, isfrac: bool=False) -> str:
    '''numTo is the entry point to the in-module calculation algorithms. It is
    responsible for delegating the correct values to the correct inner function
    calls. To use:
    we want to convert a decimal 10.625 to binary.
    1- 10.625 should be separated to 10, 625. As numTo accepts ONLY a string of
    digits.
    2- numTo would be called twice: 
        * numTo(10, 10, 2, False) -> 1010
        * numTo(625, 10, 2, True) -> 101
    3- The output should then be reconnected to result in 1010.101

    NOTE: parse function in this module does these steps automatically for you.'''

    curry = lambda fn, *args: lambda x: fn(x, *args)
    chain = lambda a, b: lambda x: b(a(x))

    b2d = curry(_base2Dec, basefrm, isfrac)
    d2b = curry(_dec2Base, baseto, isfrac)

    if numStr:
        return chain(b2d, d2b)(numStr)
    else:
        return '0' 



# Parsing --------------------------------------------------------------------

def parse(numStr: str, basefrm: int, baseto: int) -> str:
    '''Parse the number string (for things like . and -)
    parse takes a number string like -10.625, and its base, it takes care of 
    the negatives and floating points, and returns a string representation of 
    the number in the base specified as the third arg.

    example: parse('-10.625', 10, 2) -> -1010.101
    '''
    whole, point, fract = numStr.partition(".")
    if whole.startswith("-"):
        neg = "-"
        whole = whole[1:]
    else:
        neg = ""

    whole = whole.lstrip("0")
    fract = fract.rstrip("0")

    calc = lambda a, isfrac: numTo(a, basefrm, baseto, isfrac)
    join = lambda *a: "".join(a)

    if not point:
        return join(neg, calc(whole, False))
    else:
        whole = join(neg, calc(whole, False))
        fract = calc(fract, True)
        return join(whole, point, fract)



# UI -------------------------------------------------------------------------

import os
import re

clear = lambda: os.system('cls || clear')

# TODO: implement fractional conversions
binre = re.compile(r"-?[01]+(.[01]+)?")
hexre = re.compile(r"-?[a-f\d]+(.[a-f\d]+)?")
decre = re.compile(r"-?\d+(.\d+)?")
octre = re.compile(r"-?[0-7]+(.[0-7]+)?")

basemap = dict(zip(['b','d','x','o'], [2,10,16,8]))
basematch = { 
    'b': lambda num: binre.fullmatch(num),
    'd': lambda num: decre.fullmatch(num),
    'x': lambda num: hexre.fullmatch(num),
    'o': lambda num: octre.fullmatch(num)
}

# The interactive templates
def interactive(
        info: "lambda: print", prompt: str,
        test: "lambda str: bool", error: str,
        retfn: "lambda str: str"
    ) -> str:
    
    while 1:
        info()
        strIn = input(prompt)
        if not test(strIn):
            print()
            print(error)
        else:
            return retfn(strIn)

modeerror = "Error: Please choose one of the present choices"
def modeprompt(fromto): 
    return lambda: print(
        f"Choose the base you want to convert {fromto}",
            "B) Binary",
            "D) Decimal", 
            "X) Hexadecimal",
            "O) Octal", sep="\n")
def modecheck(strIn): 
    return strIn.lower() in {"b", "d", "x", "o"}
def base(fromto): 
    return interactive(
        modeprompt(fromto), "Your choice: ", modecheck, 
        modeerror, lambda strIn: strIn.lower()
    )


# Interactive code

try:
    clear()
    print("Welcome to Base2Base, written by Hazem Elmasry",
    "This program is able to do *any* conversion between:",
    "- Binary",
    "- Decimal",
    "- Hexadecimal",
    "- Octal",
    "",
    "NOTE: If you enter float numbers, make sure they're in this format: 10.32",
    "      short-hand formats like '.67' or '192.' are not accepted.",
    "",
    "", sep="\n")
    input("Press Enter to continue...")

    clear()
    baseIn = base("from")

    print()
    number = interactive(
            lambda: print(
            "Enter a valid number within your representation of choice.."),
            "Your number: ", lambda strIn: basematch[baseIn](strIn),
            "Error: Your number did not match the base you chose..",
            lambda strIn: strIn
        )

    clear()
    baseOut = base("to")

except KeyboardInterrupt:
    print()
    print("Interrupted.. Exiting.")
    exit(0)

else:
    clear()
    print("Calculating...")
    print("\n\n", end="")
    print(f"{baseIn.upper()}[{number}] -> {baseOut.upper()}")
    print(
        f"Result: 0{baseOut}"
        f"{parse(number,basemap[baseIn],basemap[baseOut])}")
    exit(0)
