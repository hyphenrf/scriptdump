# NOTE: could've used RegEx

import os

os.chdir("C:\\Users\\Hazem Elmasry\\Downloads\\platform-tools")

print('Logging...')

with open('UIDs.txt','w+',encoding='UTF-8') as UIDs:

	with open("log.txt",'r',encoding='UTF-8') as log:
		for logline in log:
			if 'ActivityManager: START u0 {act=android.intent.action.MAIN' in logline:
				uidline = logline[logline.index('uid')+4:]
				UIDs.write('uid='+uidline[:uidline.index(' ')]+'\n')

print('Done!')