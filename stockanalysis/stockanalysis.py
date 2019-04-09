n=0
p=0
num_stock=int(input('no. of stocks :- '))
for i in range(1,num_stock+1):
		ch_op=float(input('CHOPPINESS INDEX:- '))
		if ch_op>=61:
			n=n+2
		elif ch_op<=38:
			p=p+2
		adx=float(input('ADX:- '))
		if adx>=25:
			con_8=input('Is there a crossover between -DI and +DI:-(yes/no)')
			if con_8.lower()=='yes':
				p=p+2
			elif con_8.lower()=='no':
				pass
		elif adx<25:
			n=n+2
		ad_ln=input('Direction of Advance/Decline line(upward/downward) :- ')
		if ad_ln.lower()=='downward':
			con_9=input('Direction of concerned market(upward/downward) :-')
			if con_9=='downward':
				n=n+2
			else:
				n=n+2
		elif ad_ln.lower()=='upward':
			con_9=input('Direction of concerned market(upward/downward) :-')
		if con_9.lower()=='upward':
			p=p+2
		elif con_9.lower()=='lower':
			n=n+2
		mfi=float(input('MFI :-'))
		r1=80-mfi
		r2=mfi-20
		if r1>r2:
			state_mfi='Towards oversold'
			n=n+2
		elif r1<r2:
			state_mfi=' Towards overbought'
		else:
			state_mfi='Neutral'
			p=p+2
		macd1=input('MACD(above/below) :-')
		if macd1=='above':
			state_macd='For short term high probability of price increment'
			p=p+2
		elif macd1=='below':
			state_macd='For short term high probability of price decrement'
			n=n+2
		else:
			state_macd='Cannot be predicted'
		st_p=float(input('Current stock price :- ')) #Preference
		h_st_p=float(input('This month previous high :- ')) #Preference
		if st_p>h_st_p:
			p=p+2 # Comparing stock price with current month high price of stock
		elif st_p<h_st_p:
			n=n+2
		trend_dir=input('Trend direction(Upward/Downward) :- ') #Preferance
		if trend_dir.lower()=='upward':  # Finding trend direction 
			p=p+4
		elif trend_dir.lower()=='downward':
			n=n+4
		ch_mf=float(input('CMF: '))
		if ch_mf>0:
			p=p+2
		elif ch_mf<0:
			n=n+2
		par_sr=input('PARABOLIC SAR(above/below) : ')
		if par_sr.lower()=='lower':
			p=p+2
		elif par_sr.lower()=='upper':
			n=n+2
		aw_in=input('AWESOME INDICATOR(ZERO LINE/TWIN PEAKS/SAUCER) :- ')
		if aw_in.lower()=='zero line':
			con_1=input('AO (above/below) ZERO LINE :- ')
			if con_1.lower()=='below':
				n=n+2
			elif con_1.lower()=='above':
				p=p+2
		elif aw_in.lower()=='twin peaks':
			con_2=input('(ABOVE/BELOW) ZERO LINE :- ')
			if con_2.lower()=='above':
				con_3=input('Is the second peak corresponding bar red(yes/no) :- ')
				if con_3.lower()=='yes':
					n=n+2
			elif con_2.lower()=='below':
				con_3=input('Is the second peak higher than the first one and followed by a green bar (yes/no) :- ')
				if con_3.lower()=='yes':
					p=p+2
				elif con_3.lower()=='no':
					n=n+2
		elif aw_in.lower()=='saucer':
			con_5=input('Is AO above or below Zero line(above/below):- ')
			if con_5.lower()=='above':
				con_6=input('Are ther multiple red bars with second lower than first one and followed by a green bar(yes/no):- ')
				if con_6.lower()=='yes':
					p=p+2
				elif con_6.lower()=='no':
					n=n+2
			elif con_5.lower()=='below':
				con_7=input('Are the multiple green bars with second bigger than first one followed by red bar(yes/no):- ')
				if con_7.lower()=='yes':
					p=p+2
				else:
					n=n+2



if int(p)<int(n):
	print('Recomendation : SELL')
elif int(p)>int(n):
	print('Recomendation : BUY ')
else:
	print('Stock has a neutral state on the basis of above information and future cannot be predicted')






