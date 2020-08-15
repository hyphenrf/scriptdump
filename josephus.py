""" Josephus Problem -- see: - https://en.wikipedia.org/wiki/Josephus_problem 
                             - https://youtu.be/uCsD3ZGzMgE """
def j(n):
    tmp = n
    pow = 0
    while (tmp>>1):
        tmp >>= 1
        pow += 1
    
    return ((n ^ (1<<pow)) << 1) + 1
            #  |    `-- msb |
            #  `- reset msb |
            #               `-- shift to the left and add 1
            #  110110 -> 010110 -> 101100 -> 101101
