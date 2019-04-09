from gtts import gTTS
import playsound
import time
import os
for q in range(0,100000000):
	with open('fl.txt',mode='r')as f:
		x=f.read()
		if x =='' or type(x) != str:
			time.sleep(1)
		else:
			tex=gTTS(x)
			tex.save('run'+str(q)+'.mp3')
			playsound.playsound('C:\\Users\\siddhant\\Desktop\\samridh\\codes\\run'+str(q)+'.mp3', True)
			os.remove('C:\\Users\\siddhant\\Desktop\\samridh\\codes\\run'+str(q)+'.mp3')
			with open('fl.txt',mode='r')as f:
				y=f.read()
				if x != y:
					continue
				else:
					while x==y:
						time.sleep(1)
						with open('fl.txt',mode='r')as f:
							x=f.read()
					else:
						continue