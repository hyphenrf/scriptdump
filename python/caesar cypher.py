
def cypherz(a,b):
    if a==' ':
        return a
    elif ord(a)<(127-b):
        return chr(ord(a)+b)
    elif ord(a)>(126-b):
        return chr(ord(' ')+b-126+ord(a))
    else:
        return '*out of range*'

while True:        
    s=input('paste your text here OR type "!exit" to quit ')
    if s=='!exit':
        break
    shift=int(input('how many letters do you want to shift? '))

    cypher=''
    for i in s:
        cypher+=cypherz(i,shift)

    print(cypher)
