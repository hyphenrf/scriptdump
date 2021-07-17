# word list of all the possible passwords from 000000 to 999999 without bricking your memory.
# The key is to write to a file instead of memory and use generators which use tuple parenthesis and comprehended loop with range function in it. ex: (x for x in range(n))
# Generators don't store a whole list in memory, just one iteration at a time.
#
# Licence: none (?) It's just a note-taking script.

import datetime
import os
import time


with open("file.txt","w") as a:
    #print("file opened!")

    start = time.process_time()
    a.writelines(f"{i:06}\n" for i in range(1000000)) # {:03} format for int based variables, str(i).zfill(3) or str(i).rjust(3,"0") for string.
    end = time.process_time() - start

    # list comprehension and generators:
    # odds_lto100 = [num for num in range(100) if num % 2 != 0]

direc = os.getcwd()
stats = os.path.getsize(f"{direc}\\file.txt")
if stats >= 1024**3:
    stats = f"{stats/1024**3:.2f}GB"
elif stats >= 1024**2:
    stats = f"{stats/1024**2:.2f}MB"
elif stats >= 1024:
    stats = f"{stats/1024:.2f}KB"
else:
    stats = f"{stats}B"
end = str(datetime.timedelta(seconds=end))
end = end[:end.rfind(".")+3]

print(f'''done!
Total file size is: {stats}
Directory: {direc}
Time elapsed: {end}
''')
