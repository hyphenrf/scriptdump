# recursive return the largest in an input seq
def largest(a=0, x=0):

    if a == -1:
        return x

    elif a < x:
        a = int(input("Enter a value: "))
        return largest(a, x)

    else:
        x = a
        a = int(input("Enter a value: "))
        return largest(a, x)


print("your starting value is 0.")
print("largest input you entered was: ",largest())
