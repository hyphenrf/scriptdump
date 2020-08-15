#!/usr/bin/env python3


# BITWISE REFERENCE

def get(data, position):
    '''get the bit at position
    position starts from 0, right to left'''
    return data& (1<<position)
    # alternatively to only get 1 or 0 
    # (data & (1<<position)) >> position

def set(data, position):
    '''set the bit at position to 1
    position starts from 0, right to left'''
    return data| (1<<position)

def tes(data, position):
    '''set the bit at position to 0, clearing it
    position starts from 0, right to left'''
    return data& ~(1<<position)

def tog(data, position):
    '''toggle the bit at position
    position starts from 0, right to left'''
    return data^ (1<<position)

def circular_right(data: bytes, position):
    '''how to do a circular shift to the right
    Python ints are arbitrary percision.
    so we need to use something more predictable'''
    assert len(data) == 1, "Too many, or too little characters in input"
    shift = position % 8
    return [(data[0] >> shift) | (data[0] << (8 - shift)) % 256]

