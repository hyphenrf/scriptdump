# Verbosefuck translator v 0.2.5 Beta
# Turns verbosefuck syntax into brainfuck syntax and vice versa
# Can read both verbosefuck and brainfuck files
# What is Verbosefuck? This is verbosefuck https://esolangs.org/wiki/VerboseFuck

import os



# Defines
syntax = {
    "<" : "math.equation(pointer=pointer-void(1));",
    ">" : "math.equation(pointer=pointer+void(1));",
    "+" : "math.equation(deref(pointer)=(deref(pointer)+byte(1)):binaryand:byte(255));",
    "-" : "math.equation(deref(pointer)=(deref(pointer)-byte(1)):binaryand:byte(255));",
    "[" : "define(defines.label,defines.label.createnew());conditional(block.if,boolean.inequality(deref(pointer),byte(0))){",
    "]" : "};conditional(block.if,boolean.inequality(deref(pointer),byte(0))){program.flow.labeledjump(defines.label.last());};undefine(defines.label,defines.label.last());",
    "," : "math.equation(deref(pointer)=programcode(conversion.changedatatype(program.console.standardoutput.stream.readunbufferedchars(1).getvalue(0),types.byte)));",
    "." : "program.console.standardoutput.stream.writeunbufferedchars(array.create(1,conversion.changedatatype(deref(pointer),types.character,conversion.method.binary)),0,1);",
    "BEGIN\n\n" : "program.initialize();math.equation(program.errors.handler.activated=boolean(false));program.console.standardinput.openstream();program.console.standardoutput.openstream();define(defines.variable,variable(pointer));implanttype(pointer,types.pointer(to:types.byte));math.equation(pointer=void(0));program.memory.allocate(pointer,void(math.infinity),program.memory.memorytype.bidirectional);",
    "\n\nEND" : "program.memory.deallocate(pointer,void(math.infinity),program.memory.memorytype.bidirectional);undefine(defines.variable,variable(pointer));program.console.standardoutput.closestream();program.console.standardinput.closestream();program.terminate();"
    }



#functions
def filehandler(fname,Mode=0):
    ''' handles files and makes them ready for processing 
        Mode 0 verbose
        Mode 1 brain
    '''

    with open(fname,"r",encoding="UTF-8") as f:
        text = f.read()
        
        if Mode:
            # remove comments, preserve spacing
            nutext = ""
            for char in text:
                if char in "<>.,+-[]\n\t":
                    nutext+=char
            text = nutext
            # TODO: figure out how to add a comment every 1000 bytes of code (including comment bytes)

        else:
            # do not preserve spacing (for correct translation)
            text = text.replace("\n","").replace("\t","").replace(" ","")
            # remove comments (to avoid interpreting brainfuck characters in them)
            while "~!comment!~" in text:
                text = text.replace(text[text.index("~!comment!~"):text.index("~!uncomment!~")+len("~!uncomment!~")],"")
    
    return text


def translate(text,Mode=0):
    ''' handles direct text input, probably won't be needed in shell at all 
        Mode 0 verbose
        Mode 1 brain
    '''
    global syntax

    if Mode:
        for sym in syntax:
            synsym = syntax[sym].replace(",",", ").replace("="," = ").replace("+"," + ").replace("-"," - ").replace(";",";\n")
            text = text.replace(sym,synsym) # There has to be a way better than replacing each time to format. PATCH this.
            print(text)
            input()
            # this is a problem. It seems like whenever a replacement happens, the next replacement builds on it. Creating wrong nested replacements.
            # example: in the text g.ap
            #          first replacement replaces . with (a,.b)
            #          second replacement replaces , with (ka);
            #          Result is g(a(ka);.b)ap instead of g(a,.b)ap
            # changing order of replacement won't help
            # this algorithm is fundamentally flawed
            # I need to treat translated strings as separate chunks without losing their order.
            
        text = syntax["BEGIN\n\n"] + "\n" + text + "\n" + syntax["\n\nEND"]
    else:
        for sym in syntax:
            text = text.replace(syntax[sym],sym)

    output = text
    return output



    


# code wrapper

# print current working directory, ask user if they want to cd or proceed
print("Verbosefuck translator")
print("\n\nHello!")
print("current directory:",os.getcwd())
while True:
    choice = input("change directory or proceed? Just press enter to proceed (quit/cd/[proceed]): ")
    if choice.casefold() == "quit" or choice.casefold() == "q":
        quit()
    elif choice.casefold() == "cd":
        print("where do you want to go? (please provide full path)")
        try:
            os.chdir(input())
            print(f"moved to: {os.getcwd()}")
            break
        except Exception:
            print("please provide an existing path.")
            continue
    elif choice.casefold() == "p" or choice.casefold() == "proceed" or choice == "":
        break
    else:
        print("this is not a correct choice")

# Ask user for file name (or use default input.txt). Remind user to use full name for cwd and full path outside of it.
# ask user whether the file you're handling is brain or verbose (File handler)
# brainfuck: remind user to always make sure comments do not contain any syntax characters (especially , and .), 
# or the conversion will be incorrect
# NOTE: Fix this
#while True:
#    choice = input("Are you translating verbosefuck or brainfuck script? ([v]/b): ")
#    if choice.casefold() == "quit" or choice.casefold() == "q":
#        quit()
#    elif choice.casefold() == "v" or choice.casefold() == "":
#        mode = 0
#        break
#    elif choice.casefold() == "b":
#        print("always make sure comments do not contain any bf syntax characters (especially , and .), or the translation will be incorrect")
#        mode = 1
#        break
#    else:
#        print("this is not a correct choice")
mode = 0

print("""usually this script is accompanied by a file called input.txt
if such file doesn't exist in current directory or you didn't paste your code in it,
your best choice is to specify the file you pasted your code into, for this script to read.""")
while True:
    choice = input("read input.txt? Or read your own file?\npress enter for input.txt, you know the drill. (own/[default]): ")
    try:
        if choice.casefold() == "own":
            fname = input("what's the file name? (please provide full path if it's not in current directory)")
            open(fname,"r").close()
            break
        elif choice.casefold() == "d" or choice.casefold() == "default" or choice == "":
            open("input.txt","r").close()
            fname = "input.txt"
            break
    except Exception:
            print("the chosen file does not exist. please provide an existing file and check your spelling.")
            if input("quit the program? (y/[n]): ") == "y":
                quit()
            continue
    else:
        print("this is not a correct choice")

# open file and read (File handler)
# verbose: check for, slice, and remove comments [TODO: feature: put comments back in resultant file (preserve comments)] (File handler)
# brainfuck: wrap comments in comment tags
try:
    if fname and mode in {1,0}:
        text = filehandler(fname,mode)
    else:
        raise Exception('Sanity error')
except Exception as a:
    print(
        f'''something went wrong
        file name/path: {fname}
        file mode: {mode} (0:brainfuck, 1:verbosefuck)
        error: {a}
        press enter to quit.'''
    )
    input()
    quit()

# process file (text handler)
try:
    output = translate(text,mode)
    with open("output.txt","w",encoding="UTF-8") as f:
        f.write(output)

    print(f"translation successfully written to {os.getcwd()}/output.txt")
except Exception as a:
    print("something went wrong")
    print(a)

# ask user if they want it printed or not
while True:
    choice = input("do you want to see the output here? (y/[n]): ")
    if choice.casefold() == "quit" or choice.casefold() == "q":
        print("bye!")
        quit()
    elif choice.casefold() == "y":
        print(output)
        break
    elif choice.casefold() == "n" or choice.casefold() == "":
        break
    else:
        print("this is not a correct choice")

input("\n\n[press enter to quit]")
