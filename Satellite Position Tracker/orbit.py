from pyorbital.orbital import Orbital
from datetime import datetime
import time
n=int(input('No of sattelites : '))
for x in range(0,n):
	sat=str(input('Sattelite Name : '))
	info=str(input('Sattelite Details/Sattelite Observation (x/y) : '))
	orb=Orbital(sat)
	now=datetime.utcnow()
	if info == 'x':
		val=list(orb.get_lonlatalt(now))
		longitude=val[0]
		latitude=val[1]
		altitude=val[2]
		print('Longitude : ',longitude)
		print('Latitude  : ',latitude)
		print('Altitude  : ',altitude)
	if info =='y':
		print('Oservation Started')
		obs=0
		n_o=int(input('No. of Oservations : '))
		past_d=''
		while obs<=n_o:
			with open('observation '+sat+'.txt',mode='w') as o:
				now=datetime.utcnow()
				o.write(past_d)
				orb=Orbital(sat)
				val=list(orb.get_lonlatalt(now))
				longitude=val[0]
				latitude=val[1]
				altitude=val[2]
				o.write('\n')
				o.write(str(datetime.now().time()))
				o.write(':')
				o.write('\n')
				o.write('Longitude :')
				o.write(str(longitude))
				o.write('\n')
				o.write('Latitude  :')
				o.write(str(latitude))
				o.write('\n')
				o.write('Altitude  :')
				o.write(str(altitude))
				time.sleep(36000) # Delay of 1 hour 
				obs=obs+1 
			with open('observation '+sat+'.txt',mode='r')as o:
				past_d=o.read()






