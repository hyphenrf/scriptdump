#!/usr/bin/env python3

# cowsay or look and tell sequences are sequences of which you say
# what you're reading by grouping, then you proceed to write that
# down as the following entry.
#
# Here's how it's done:
# 1 is "one one"
# -> 11
# 11 is "two ones"
# -> 21
# 21 is "one two, one one"
# -> 1211
#
# and so on..

# this program will attempt to create an algorithm to generate this pattern

now = '1'

# fn read(now) = dict[num][rep]
# fn write(lsoftupl) = str( str(k)+v for v, k in ls)

def readnow(now):
    count = 1
    out = []

    for _ in range(len(now)):
        
        car = now[0]
        cdr = now[1:]
    
        if cdr.startswith(car):
            count += 1

        else:
            out.append((car,count))
            count = 1

            if not cdr: return out

        now = cdr
     
writenow = lambda readnow: "".join( str(m) + n for n, m in readnow ) 

for _ in range(30):
    st = writenow(readnow(now))
    now = st
    print(now)

print(len(st))
