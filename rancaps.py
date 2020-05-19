#!/bin/env python3

# Create a string with RanDoM cAPiTaliZation
# This script has many shortcomings that idc enough to solve
# For example:
#   There's probably zero need to use regex
#       and I just wanted to try it out then
#   I probably used more loops than needed,
#       or could've done two things in one loop
#   I put everything in one big function which is a big nono
#   Arrays are fundamentally flawed for this job -- as they
#       have mutable numeric indexes that change according to
#       The size of the array. so when replacing, first found
#       is also first replaced.
#       The correct thing to do is to use dictionaries.

import os
from random import randint
from re import findall
from subprocess import call
from sys import platform
from time import sleep


### Defines
def rancaps(s):
    """Random Capitalization function"""
    
    sArray = findall(r"[a-zA-Z]",s) # characters only without spaces
    sMainArray = list(s) # characters with spaces/punc
    capnum = len(sArray)//3 # number of desired caps is ~30% of total
    indexset = set()
    
    # choose your capped letters
    while capnum > 0:
        choice = randint(0,len(sArray)-1) 
        # -1 because len - last index in the list = 1
        
        if choice in indexset:
            continue
        else:
            indexset.add(choice)
            capnum -= 1

    # cap em (or lower if they're caps)
    for ind in indexset:
        sArray[ind] = sArray[ind].swapcase()

    # change old array with the new one
    for item in range(len(sMainArray)-1):
        if not sArray: 
            # in case sArray was depleted before sMainArray is.
            break
        elif sMainArray[item].casefold() == sArray[0].casefold():
            # This is wrong. I should've used a dict and a sub-dict of it
            sMainArray[item] = sArray.pop(0)
    
    # join and return the new atring array
    return "".join(sMainArray)


def allcaps(s):
    return s.upper()


def inputcheck(fname = "input.txt"):
    try:
        with open(fname,encoding="UTF-8") as f:
            # note: open defaults to mode 'r' or 'r+'
            # I don't remember which.
            inp = f.read()
    except OSError:
        return None
    return inp

### Prog

if __name__ == '__main__':

    print("all caps = 1\nrandom caps = 2")
    print(
        """
        [hint: having an input.txt file in your current working directory
        will save you time writing/pasting the string in terminal]
        """
    )

    # This will break if user attempts to input something else. I'm not
    # gonna do anything about it.

    choice = input("choose your method: ")
    s = inputcheck()

    if not inputcheck():
        print("input.txt not found, falling back to manual input")
        s = input("string: ")

    if choice == "1":
        s = allcaps(s)
    elif choice == "2":
        s = rancaps(s)
    else: # TODO: turn this into something actually useful
        print("Am I a joke to you? Quitting.")
        sleep(2)
        quit()
    print("done! writing output.txt in your cwd...")

    ### I/O
    
    # Give user the option to not have their output written in a file
    # Or don't. who cares. You're the only user anyway.
    written = False
    while not written:
        print("cwd: ", os.getcwd())

        try:
            with open('output.txt','x',encoding="UTF-8") as out:
                out.write(f'{s}\n')
                out.truncate()
                written = True
                print("done!")
                print("output: (will also be in output.txt)")

        except: 
            ans = input("file output.txt already exists, remove? [y/N]: ")
            if ans.casefold() == "y":
                os.remove('output.txt')
                print("removed!")
                written = False
                continue
            elif ans.casefold() in {"n",""}:
                print("please check output.txt\nQuitting...")
                break
            else: # TODO: add a cat file option
                print("Am I a joke to you? Quitting.")
                sleep(2)
                quit()
        
        try:
            if platform == 'win32':
                call(['type','output.txt'])
                os.startfile("output.txt")
            else:
                call(['cat','output.txt'])
            written = True
        except:
            print('couldn\'t open the file, sorry!')
    input("press RETURN to quit")
