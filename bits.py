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
