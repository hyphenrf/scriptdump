namae = """Jugemu Jugemu (寿限無、寿限無)
    Gokō-no surikire (五劫の擦り切れ)
    Kaijarisuigyo-no (海砂利水魚の)
    Suigyōmatsu Unraimatsu Fūraimatsu (水行末 雲来末 風来末)
    Kuunerutokoro-ni Sumutokoro (食う寝る処に住む処)
    Yaburakōji-no burakōji (やぶら小路の藪柑子)
    Paipopaipo Paipo-no-shūringan (パイポパイポ パイポのシューリンガン)
    Shūringan-no Gūrindai (シューリンガンのグーリンダイ)
    Gūrindai-no Ponpokopī-no Ponpokonā-no (グーリンダイのポンポコピーのポンポコナーの)
    Chōkyūmei-no Chōsuke (長久命の長助)"""


record = True
no_paren = ""


for i in namae:
        
	if i == "(":
		record = False
	elif i == ")":
		record = True
		continue

	if record == True:
		no_paren += i

no_paren = no_paren.rstrip("\n").split()
no_paren = " ".join(no_paren)

with open("output.txt","w",encoding="UTF-8") as out:
	out.write(no_paren)


# Now, try this again after learning regex
