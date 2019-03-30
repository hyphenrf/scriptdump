from os import getcwd
from time import sleep

# this script is a basic stream editor


file_out,file_in =      open("output.txt","w",encoding="UTF-8"),\
                        open("input.txt","r",encoding="UTF-8")


oldlink = file_in.read()
ins = eval(input("enter the character you want to replace (inputs in this script are evalled. Use quotations for str): "))
outs = eval(input("enter the replacement: "))

oldlink = oldlink.replace(str(ins),str(outs))


file_out.write(oldlink)
file_in.close()
file_out.close()


print("link written: {}\nfile path: {}".format(oldlink,getcwd()+"\output.txt"))

# Trying carriage return for fun:

for i in range(5):
	dots = "."*i	
	print(f"exiting{dots}",end="\r",flush=True) #how to use \r for showing progress?
#Here's code for Python 3.x:
#print(output , end='\r')
#The end= keyword is what does the work here -- by default, print() ends in a newline (\n) character,
#but this can be replaced with a different string.
#In this case, ending the line with a carriage return instead returns the cursor to the start of the current line. 
#Thus, there's no need to import the sys module for this sort of simple usage.
#print() actually has a number of keyword arguments which can be used to greatly simplify code. 
	sleep(0.75)

sleep(3)
exit()


