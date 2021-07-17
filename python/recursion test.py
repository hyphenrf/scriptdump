# Function recursion
import time as t
from math import factorial



def f(N):
    if N > 0 and type(N) is int:
        return N*f(N-1)
    else:
        return 1

def f2(N):
    if N > 0 and type(N) is int:
        for i in range(1,N):
            i*=(i+1)
        return i
    else:
        return 1

    

a = t.perf_counter_ns()
#f(992)
pass
b = t.perf_counter_ns()
recursion = b-a

a = t.perf_counter_ns()
factorial(1000000)
b = t.perf_counter_ns()
builtin = b-a

a = t.perf_counter_ns()
f2(1000000)
b = t.perf_counter_ns()
loop = b-a


print(f'''
recursion(passed): {recursion}ns
builtin:   {builtin}ns
loop:      {loop}ns''')

