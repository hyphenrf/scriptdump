#!/usr/bin/env python3

import re


#reg = re.compile(r'(.)\1{2}[a-z]\1{3}') # matches 111c111
#reg = re.compile(r'(.{3})[a-z]\1') # matches 123c123
reg = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]') # matches cABCaABCc 
# but only shows a (this is python-specific behaviour); c doesn't matter.

with open('out','r') as a:
    text = a.read()

match = re.findall(reg, text)
print("".join(match))

