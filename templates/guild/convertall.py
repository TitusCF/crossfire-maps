import os
t=open('GuildLocations')
a=t.read()
t.close()
b=a.split('\n')
for c in b:
	os.system('./convert.py '+c)