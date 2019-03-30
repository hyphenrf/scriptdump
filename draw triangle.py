# sep print option is useful for comma separated print *args

try:
	l = input('triangle length: ')
	l = int(l) # will raise exception if l.isdigit()==False

        # will raise exception on condition
	if l<1:
		raise Exception

        # create the sides like this / |
	for i in range(l-1):
    		print(
                        ' '*(l-i-1),
                        '/',
                        ' '*(i),
                        '|',
                        sep=''
                )
        # create the base like this /___|
	print(
                '/',
                '_'*(l-1),
                '|',
                sep=''
        )

except Exception:
	print(f"your input '{l}' is invalid.")



input()
