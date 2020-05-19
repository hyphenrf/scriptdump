# you can call one-liners through a dict
# like this:

d = {
        1: lambda: print('Hello!'),
        2: lambda: input('What\'s your name?\n> ')
        3: lambda john: print(f'Hello {john}!')
    }

d[1]()
name = d[2]()
d[3](name)

# you can exec a bunch of steps in different orders/combinations with
# different outcomes without having to write it all in a decision tree in some
# cases this way.
