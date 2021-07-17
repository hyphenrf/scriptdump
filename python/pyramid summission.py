
def pyramid(n):
	sum = int()
	for i in range (n):
		sum += i+1
	return sum

try:
        print( pyramid( int( input( "Enter a number: " ))))
        print( "[Press Enter to exit]" )

        input()

except Exception as a:
	print( f"An error occurred: {a}", "[Press Enter to exit]", sep="\n" )
	
	input()

	
