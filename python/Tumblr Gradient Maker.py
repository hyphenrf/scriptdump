import re
import math as m
import os


# the matching REGEX of strict hex colour codes
hexpattern = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")
# the span HTML tag
span = lambda a,word : f'<span style="color:#{a}">{word}</span>'


def inputs():

	while True:

		try:
			word = str(input("what's the word you wanna colorize?:\n>>> "))
			
			ngrads = input("how many defined colors do you want in your gradient?\n[minimum is 2, press enter for default (2)]:\n>>> ")

			if not ngrads: # user entered default
				print("default number of colors set to 2")
				ngrads = 2
			else:
				ngrads = int(ngrads) 
				if ngrads < 2: 
					print("please enter a value that is larger than 2")
					continue

			# TODO: add a colorschemes mode where start is a list of predefined gradient values (like rainbow) 

			start = [ str(input(f"what's the color({i}) hex?\n>>> ")) for i in range(1,ngrads+1) ]

			# TODO:	make it possible to add more than just two color hex codes. (DONE)
			#		maybe add a mode to color the gradient word by word instead of char ber char
			#		and another mode to read straight from an input file
			#		maybe even make it possible to return to the misinput(?) instead of
			#		inputting the whole thing again.

		except ValueError:
			print("please only input a number in the number of colors prompt.")
			continue

		except Exception as e:
			print(e)
			print("how did you even do this?") # i dunno I'm bored. Can't make this bitch work on hex. Will try rgb??
			continue

		# check input integrity
		checkstart = [ hexpattern.match(a) for a in start ]

		# checking where a wrong pattern was entered:
		if not all(checkstart):
			errorset = ""
			for b in range(len(checkstart)):
				if not checkstart[b]:
					if b == len(checkstart)-1:
						errorset += start[b]
					else:
						errorset += start[b]+", "

			print(f"your input(s) [{errorset}] were not legitimate color hex codes.\n\
A hex color code is in the form of #XXX or #XXXXXX where x is in {{0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f}}.")
			continue
		else:
			break
	
	return (word, start)

def dubthehexa(hexlist):

	out = []
	for hexa in hexlist:
		hexa = hexa.lstrip("#")
		n,b = len(hexa)//6, 1
		if not n: n=1;b=2
		hexa = [ hexa[i:i+n]*b for i in range(0,len(hexa),n) ]
		out += [hexa]
	
	return out
	


def parsecols(start):
	# parse the input params to turn them into rgb values

	# first, turn hex into rgb for ease of calculation
	rgbstart = []
	for hexa in dubthehexa(start):
		
		rgb = {
			'R':int(hexa[0],16),
			'G':int(hexa[1],16),
			'B':int(hexa[2],16)
		}

		rgbstart += [rgb]

	rgbparsed = []
	for i in range(len(rgbstart)-1):
		col1 = rgbstart[i]
		col2 = rgbstart[i+1]
		dR = col2['R']-col1['R']
		dG = col2['G']-col1['G']
		dB = col2['B']-col1['B']
		cold = {
			'dR':dR,
			'dG':dG,
			'dB':dB
		}

		rgbparsed += [(col1,col2,cold)]
	
	return tuple(rgbparsed)
 
def parseword(word):
	# parse the word in a format that's usable by other functions
	# TODO: make a word mode next to the character mode
	charlist = list(word)
	# wordlist = word.split()

	return charlist

def returnspan():

	word,hexcols = inputs() 		# str,strlist

	if len(word) < 2: return span("".join(dubthehexa(hexcols)[0]),word)

	charlist = parseword(word)		# strlist
	rgbcols = parsecols(hexcols)	# intdicttupltupl (
	#	(
	# 		[0]=col1={R:r,G:g,B:b},
	# 		[1]=col2={same stuff},
	# 		[2]=cold={dR:dr,dG:dg,dB:db}
	# 	),
	#	(...), ...
	# )

	dxcol = len(hexcols)-1
	dxchar = len(charlist)-1
	step = dxcol/dxchar # this is to define the x step length for the col equations
	
	hex_perchar=""
	for i in range(dxchar+1):
		# the x value is the value that will be used in the y = dy*(x-colind)+colval
		x = i*step
		colind = m.floor(x)
		
		if colind == dxcol:
			hexa = "".join(dubthehexa(hexcols)[colind])

		else:
			R = rgbcols[colind][0]['R']\
				+rgbcols[colind][2]['dR']\
				*(x-colind)
			G = rgbcols[colind][0]['G']\
				+rgbcols[colind][2]['dG']\
				*(x-colind)
			B = rgbcols[colind][0]['B']\
				+rgbcols[colind][2]['dB']\
				*(x-colind)

			hexa = \
			f"\
{hex(round(R)).replace('0x','').upper().zfill(2)}\
{hex(round(G)).replace('0x','').upper().zfill(2)}\
{hex(round(B)).replace('0x','').upper().zfill(2)}"

		hex_perchar += span(hexa,charlist[i])

	return hex_perchar


print("current directory: ",os.getcwd(),sep="\n")

with open("output.html","w") as f:
	f.write(returnspan())
