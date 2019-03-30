print("""
NOTE: preceed your string with 'ascii:' to use ASCII-to-Alpha mode.
ASCII numbers should be separated by one space like this:
ascii:72 69 87 87 79 63 63""")
print()

while True:
	
	inp = str(input("your input [!q to quit]: "))

	if inp == "!q":
		quit()

	elif inp.startswith("ascii:"):

		try:
		
			inp = inp.split(":")
			inp = inp[1].split()
			print(
				"".join([chr(int(i)) for i in inp]) #list comprehension desu
			)
		except Exception as a:
			print("your input was incorrect, error:{}".format(a))

	else:

		print(
			" ".join([str(ord(i)) for i in inp])
		)

# NOTE: input() at the end of file will prevent it from closing automatically.