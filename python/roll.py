from random import randint
Y = ['Y', 'y', 'yes', 'Yes', 'YES']
N = ['N', 'n', 'no', 'No', 'NO']
R = ['R', 'r', 'reset', 'Reset', 'RESET']

# first loop for setting min and max values
while True:
    ans = input('Roll? [Y/N]: ')
    if ans not in Y+N:
        print('wrong answer')
        continue
    if ans in N:
        quit()
    try:
        mi = int(input('Input min limit: '))
        ma = int(input('Input max limit: '))
    except:
        print('make sure your values are int')
        continue

    # second loop for continuous rolling - without the need to set min and max values
    while True:
        if ans in Y:
            print(randint(mi, ma))
            ans = input('Roll? [Y/N/R(eset)]: ')
        elif ans in N:
            quit()
        elif ans in R:
            break
        else:
            print('wrong answer')
            ans = input('Roll? [Y/N/R(eset)]: ')


