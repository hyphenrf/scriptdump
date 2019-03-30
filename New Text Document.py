inp = open ("input.txt", "r", encoding="UTF-8")
oup = open ("output.txt", "w", encoding="UTF-8")

inpu = inp.read().split("[")
inpunya = []

for item in inpu:
	inpunya += ["["+item.replace("\n","").replace("  "," ")+"\n"]

oup.writelines(inpunya)
