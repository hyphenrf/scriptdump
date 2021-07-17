# zipping

for i,j in zip( [1,2,3] , "Hello" ):
    print (f"{i}: {j}")

# more useful example:

darkness = "Hello Darkness My Old Friend..."
Dict = {}

for index,element in zip(range(len(darkness)),darkness):
    Dict[index]=element

print(str(Dict).replace(",",",\n"))
