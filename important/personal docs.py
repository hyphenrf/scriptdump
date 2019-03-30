# # removes all instances of 1
# # lesson learned: for loops are index change sensitive, and should not be used on lists that will be modified under the loop
# L=[1,2,1,2,3,1,2,1,1,1,1,1,1]
# n=L.count(1)
# while n>0:
#     L.remove(1)
#     n-=1
# print(L)
# print(' - '.join(L)) # printing a list as a string

# #------------------------------------------------------------

# #lessons learned: enumerate() and the fact that you can use more than one var in for loops
# houses = ["Hazem's","Shaban's","Doe's"]
# for ind,num in enumerate(houses):
#     print (ind,num)

# # prints:
# # 0 Hazem's
# # 1 Shaban's
# # 2 Doe's

# #------------------------------------------------------------

# # prints the multiplication table as a table not a single column
# # lesson learend: it's way fucking harder than doing a single column table
# # also: format *arg must be iterable
# # also: you can leave the placeholder empty {} or actually add in the index of the item in the .format(0,1,2) tuple like this {1} {0} {2} to manipulate order
# # also: when using an iterable *arg, it must be finished before format looks at the next arg; that's why I used only one list to store all my table values
# # also: you can use format outside of print
# stra=""
# L=[]
# for y in range(1, 13):
#     for x in range(1,13):
#         stra+="{:2d} x {:2d} = {:3d}  ||  "
#         L.append(x)
#         L.append(y)
#         L.append(x*y)
#     output = stra.format(*L)[:len(stra.format(*L))-6]
#     print(output)
#     stra=""
#     L=[]
# print()

# #----------------------------------------------------------------------

# # to RETURN a vertical string, not print it which is very easy
# # just say:
# # s='string'
# # for let in s:
# # 	print let

# def vertical(s):
#     new=s[0]
#     for let in s:
#         new+="\n"+let
#     return new

# print (vertical("based"))


# #-----------------------------------------------------------------

# # trying to make my own version of a range() fumct using lists
# def my_range(start, end):
#     Lava = []
#     while start < end:
#         Lava.append(start)
#         start += 1
#     return Lava
# # how fast is this compared to python's native range() function?

# from time import clock

# start = clock()
# for x in my_range(0, 10000000):     # my range
#     pass
# stop = clock()
# print(stop-start)

# start = clock()
# for x in range(10000000):       # python's range
#     pass
# stop = clock()
# print(stop - start)

# #----------------------------------------------------------------

# # some fun with dicts
# # dicts are sets (unordered lists) which you can modify the keys (indexes) of
# # sets are immutable and reject duplicate values, they're optimized for testing whether an item belongs in them or not better than any other iterable. for loops don't work on sets
# # some methods are unique to sets like set.intersection(), set.difference(), set.union(), set.update(iterable)
# # to create an empty set you can't use {} as it creates a dictionary, instead you use the built in CLASS set()
# # you can also create lists, dicts, and tuples this way L=list() T=tuple() D=dict()
# # unlike lists, the .pop() method in dicts returns the key as a VARIABLE with its value assigned to it
# # so you can use the popped item for other operations multiple times 

# tiny={
#     0:1,
#     1:2,
#     2:4,
#     3:8,
#     4:16
# }
# tiny2={
#     0:1,
#     1:2,
#     2:3,
#     5:6
# }

# print(tiny.keys())      # NOT A LIST
# print(list(tiny.keys()))# A LIST
# print(tiny.values())
# print(list(tiny.values()))
# print(tiny.items())
# print(list(tiny.items()))
# print(str(tiny))
# print(tiny2[1])
# print(tiny2.get(1)) # does the same as the line above, but this one returns None when it can't find the key instead of throwing a key error
# print(tiny2.get(10,"lol not found")) #returns specific val instead of None

# tinyset={1,2,4,8,16}
# tiny_values=set()
# tiny_values.update(tiny.values())
# # you can also extend a dict using the dict.update(newdict) method for batch additions
# print(tinyset)
# print(tiny_values)
# print(tiny_values == tinyset) # should return True

# for key,value in tiny.items():
#     print (key, value)

# #------------------------------------------------------------------

# import time,calendar
# print(time.asctime(time.localtime()))
# # time.sleep(10)
# calendar.setfirstweekday(6)
# print(calendar.month(1997,8))
# print("UTC",time.timezone/3600," ",time.tzname[0])
# print(calendar.isleap(2018))

# #------------------------------------------------------------------

# #anonymous functions
# coll= lambda a,b:a+b    # anon functs are one line functs
# print(coll(1,2))

# #------------------------------------------------------------------

# # in a local function scope, you can import a global variable like this:
# Money = 2000
# def AddMoney():
#    global Money
#    Money = Money + 1
#    print(locals())
#    print(globals())

# print(globals())

# #------------------------------------------------------------------

# # packages: importable directories
# import package_test
# print(dir(package_test))
# package_test.hello.oof()
# package_test.oof()

# #----------------------------------------------------------------------

# # in a packaged program, you can import the main progrm (the file that's supposed to be running to run all the other files) into one of the modules, and doing so will run all the global scope code in it. So when you don't want that happening, you use the condition below in the main file:
# if __name__ == "__main__":
#     # this condition means that if the main file's scope (__name__) is equal to the currently running scope ("__main__"), 
#     # which is false when the main file is imported, as "__main__" becomes the __name__ of the currently running module instead, and the main file's __name__ becomes its regular name,
#     # but if true, aka when running the program from the main file's scope, execute the code below
#     a=1
#     b=2
#     c= a+b
#     print(c)

# #------------------------------------------------------------------

# # trying to handle errors in my midterm's function using try-except

# def isDiv(x,y):
#     '''
#     This function tests whether the first prameter is divisable by the second parameter or not
#     '''
#     try:
#         if x%y==0:
#             return True
#         else:
#             return False
#     except ZeroDivisionError:
#         return "You tried to divide by Zero"
#     except TypeError:
#         if type(x) not in [int,float] and type(y) not in [int,float]:
#             return "please use numbers only, you used %s with the type %s and %s with the type %s"%(x,type(x),y,type(y))
#         elif type(x) not in [int,float]:
#             return "please use numbers only, you used %s with the type %s"%(x,type(x))
#         else:
#             return "please use numbers only, you used %s with the type %s"%(y,type(y))
#     except Exception as a:
#         print('your error is: ', a)
#    # except:
#    #     print('I can\'t tell what that error was!')


# #------------------------------------------------------------------------------------

# # Trying to use and/or on a list of conditions instead of listing them on if
# # method used is all() and any() functions which return True/False depending on if the list has true values (any value is a true one except a handful you know).

# while True:
#     ans=input()
#     l=['hazem','taha']
#     l2=[]

#     for name in l:
#         if name in ans:
#             l2.append(True)
#         else:
#             l2.append(False)
#     if all(l2):       # meaning if all values in L2 are true (equiv. to AND)
#         print ("AYAYA")
#     elif any(l2):     # meaning if any value in L2 is true (equiv. to OR)
#         print ("Ok..")
#     elif ans == "quit":
#         quit()
#     else:
#         print("aw...")

# #----------------------------------------------------------------------

# # more error handling:
# # assert tests a condition and if it returns false, assert stops the code and returns AssertionError as its second argument
# try:
#     print('hi')
#     assert (1>1), "1 isn't greater than 1! that's impossible!"
#     print('hello')
# except AssertionError as a:
#     print(a)
#     print('hahaha!')
# else:
#     print('this line will only be executed if there wasn\'t an exception')
# finally:
#     print('this line will be executed no matter what')


# # # raising your own exceptions:
# # # you can create an error within a function in which you raise your very own errors for a try-except method to execute later
# # # here's an example: NEVERMIND, THIS EXAMPLE IS OUTDATED

# # def row(boat):
# #     if boat>9:
# #         raise "SmallBoat" from IndexError.with_traceback("hi")
# #     else:
# #         print(boat*3)

# # try:
# #     row(15)
# # except "SmallBoat" as a:
# #     print(a)

# # # or you can use a default type error like this:

# try:
#     print("hi")
#     raise TypeError("this is how you print an error message in raise")
#     print('hello')
# except TypeError as a:
#     print(a)
#     print('hahaha!')

# #-------------------------------------------------------------------------------

# # "with" is a better way to ensure that your file is closed right after the code block underneath "with" is executed

# with open('test.txt','a+') as target:
# # use r+ when you know file exists, and you don't want to rewrite it, writing in r+ appends.
# # use w+ when you want to create/rewrite a file. AFAIK the '+' (indicating reading abilities) didn't work because the file was truncated (rewritten as empty)
# # use a+ when you want to create a file without truncating, and want to read it too. the pointer is always at the end of the file so if you want to read it, you must seek.
#     import os 
#     print(os.path.dirname(os.path.realpath('test.txt')))
#     target.seek(0)
#     stra=target.read(10)
#     target.write('HINJAKU!')
#     print(stra)
#     print('file should be closed after this!')
# try:
#     target.read()       # testing if file is still open
# except Exception as a:
#     print(a)

# #---------------------------------------------------------------------------

# # CLASSES AND METHODS

# class Employee:

#     RaiseAmount = 1.05
#     nEmployees = 0

#     def __init__(self,firstName='John',lastName='Doe',salary=5000):
#         self.first = firstName
#         self.last = lastName
#         self.salary = salary

#         Employee.nEmployees += 1
    

#     def email(self):
#         return '{}.{}@company.com'.format(self.first,self.last)
    

#     def fullname(self, american=False):
#         if american:
#             return '{1}, {0}'.format(self.first,self.last)
#         else:
#             return '{} {}'.format(self.first,self.last)


#     def raise_salary(self):
#         salary *= Employee.RaiseAmount 
#         return self.salary * Employee.RaiseAmount

# print()
# print('n of emps before adding John: {}'.format(Employee.nEmployees))
# print('Jon = Employee()')
# Jon = Employee()
# print('n of emps after adding John: {}'.format(Employee.nEmployees))
# print()
# print('John\'s full name, lastfirst: {}'.format(Jon.fullname(True)))
# print()
# print('John\'s salary before raise: {}'.format(Jon.salary))
# print(Jon.__dict__)
# print()
# print('Jon.RaiseAmount = 1.03')
# Jon.RaiseAmount = 1.03
# print('Jon.raise_salary()')
# Jon.raise_salary()
# print('John\'s salary after raise: {}'.format(Jon.salary))
# print(Jon.__dict__)
# print()

# -------------------------------------------------------------

# # fstrings!!!!

# hello = "fuck you"
# world = "this is good syntax"
# print(f"{hello} {world}.")

# # fuck you this is good syntax.

