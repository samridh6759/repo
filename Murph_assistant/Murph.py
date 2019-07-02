'''How to use Murph : open command line with python in Path and change the directory to the place
where this program is saved to run the program.

SourcecodeFile : Murph.py is the sourcecode file

Functions Murph can do :
1) Say (search,calcualte) : it will ask what to search/calculate etc.
2) Say (search on wikipedia or brief or explain) : Murph will ask what to search for speak the name of the variable
(eg.Steve jobs) in the microphone Murph brief you about the variable. 
3) Say (find relationship,connection) : Murph will ask you for the variables to
search the relationship between(eg Jupiter and pencil-Murph will say Carbon)
4)Say sleep : Murph will sleep(you can also define the minutes or seconds by saying
 sleep for 5 minutes or sleep for 10 seconds)
5)Say set alarm: Murph will set alarm
6)Say learn : Murph will ask for the path of the datatset to learn then the
name of the columns to take into consideration once learned it will ask wether to 
predict something and wether to save the learning'''

import wolframalpha
import wikipedia
from gtts import gTTS
import speech_recognition as sr
import playsound
import os
from requests import get
from requests.exceptions import RequestException
from contextlib import closing 
from splinter import Browser
import time
import random
from datetime import datetime
import sys
import gym
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd 
import numpy as np 
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from warnings import simplefilter
import pickle
state=1
app_id='6WPAP6-L4WVRG22XG'
client = wolframalpha.Client(app_id)
q=2
def speak(x):
	tex=gTTS(x,lang='en-in')
	tex.save('run'+str(q)+'.mp3')
	playsound.playsound('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\run'+str(q)+'.mp3', True)
	os.remove('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\run'+str(q)+'.mp3')
speak('Hello sir what can i do for you')
q=q+1
print('Hello sir what can i do for you')
# argl
def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:                
		audio = r.record(source,duration=5)         
	try:
		output=r.recognize_google(audio)
		return(output)
	except :
		
while state==1:
	arg=listen()
	if type(arg)!=str:
		listen()
	else:
		if arg=='sleep':
			state=0
		elif 'sleep' in arg  and 'for' in arg and 'minutes' in arg or 'minute' in arg :
			sleep=arg.split(' ')
			time.sleep(int(sleep[-2]*60))
			speak('Awake')
			q=q+1
			print('Awake !!')
		elif 'sleep' in arg  and 'for' in arg and 'seconds' in arg or 'second' in arg:
			sleep=arg.split(' ')
			time.sleep(int(sleep[-2]))
			speak('Awake')
			q=q+1
			print('Awake !!')
		elif 'what' in arg and 'your' in arg or 'name' in arg or 'who' in arg and 'you' in arg :
			speak('I am Murph , i was born on 1st of june 2019 and My creator is Samridh and I am his assistant')
			q=q+1
			print('I am Murph , i was born on 1st of june 2019 and My creator is Samridh and I am his assistant')
		if 'search' in arg and 'wikipedia' not in arg or 'calculate' in arg or 'find' in arg and 'connection' not in arg:
			speak('what shall i search ')
			q=q+1
			print('What to search for')
			search_query=listen()
			try :
				res = client.query(search_query)
				answer = next(res.results).text 
				speak(answer)
				print(answer)
				q=q+1
			except:
				speak('Sir i cant find any resource able to answer your question please elaborate your question ')
				q=q+1
				print('Sir i cant find any resource able to answer your question please elaborate your question ')
		elif 'brief' in arg or 'explain' in arg or 'search' and 'wikipedia' in arg:
			try:
				speak('what shall i search on wikipedia ')
				q=q+1
				print('what shall i search on wikipedia ')
				user_query=listen()
				result=wikipedia.summary(user_query)
				speak(result)
				q=q+1
			except:
				print('I am unable to understand the wikipedia page you are referring to please elaborate')
		elif 'find relationship' in arg or 'connection' in arg or 'is' and 'connection' in arg :
			speak('Between which 2 arguments shall i find the relation')
			q=q+1
			print(('Relationship between'))
			user_query=listen()
			l=user_query.split(' ')
			src=l[0]
			target=l[-1]
			with Browser('chrome') as browser:
				url = "https://www.sixdegreesofwikipedia.com"
				browser.visit(url)
				browser.find_by_xpath(xpath="//*[@id=\"root\"]/div[2]/div/div[2]/div[1]/div/input").fill(src)
				browser.find_by_xpath(xpath="//*[@id=\"root\"]/div[2]/div/div[2]/div[2]/div/input").fill(target)
				xp='//*[@id="root"]/div[2]/div/button'
				browser.find_by_xpath(xp).click()
				time.sleep(10)
				out_xp='//*[@id="root"]/div[2]/div/div[3]'
				res=browser.find_by_xpath(xpath=out_xp).text
				p=res.index('in')
				res=res[:p]
				speak(res)
				q=q+1
				print(res)
				paths=browser.find_by_xpath(xpath='//*[@id="root"]/div[2]/div/div[5]').text
				speak('What do you want to do with the relations found between '+src+'and'+target)
				q=q+1
				print('What do you want to do with the relations found between '+src+' and '+target)
				prog=listen()
				sw=''
				ac_out=''
				fc_out=''
				for x in paths:
					if x!=' ':
						sw=sw+x.lower()
					else:
						ac_out=ac_out+sw+' '
						sw=''
				for g in ac_out:
					if g!='\n' or g!=' ':
						fc_out=fc_out+g
					else:
						fc_out=fc_out
				if 'all' in prog :
					speak(fc_out)
					q=q+1
					print(fc_out)
				else:
					speak('Which Element Do you want me to find in the connections ')
					q=q+1
					print('Which Element Do you want me to find in the connections ')
					el=listen()
					if el in fc_out:
						s_spk=('Yes '+el+' is having relationship with both '+src+' and '+target)
						print('Yes '+el+' is having relationship with both '+src,' and '+target)
						speak(s_spk)
						q=q+1
					else:
						s_spk=('No '+el+' does not have '+' any relation with '+src+' and '+target)
						speak(s_spk)
						q=q+1
						print('No '+el+' does not have '+' any relation with '+src+' and '+target)
		elif 'wake' in arg and 'me' in arg and 'up' in arg or 'alarm' in arg and 'set' in arg or 'alarm' in arg:
			speak('At what time will you like to wake up.Please tell the time only')
			q=q+1
			print('At what time will you like to be alarmed.Please tell the time only')
			alarm_time=listen()
			w_l=alarm_time.split(' ')
			month=time.localtime().tm_mon
			year=time.localtime().tm_year
			current_date=time.localtime().tm_mday
			time_wake=int(w_l[0])
			spinner = spinning_cursor()
			speak('Alarm Set all functions have been disabled')
			q=q+1
			print('Alarm Set all functions have been disabled')
			while time.localtime().tm_hour!=time_wake:
				wake_st=listen()
				if wake_st=='wakeup':
					time_wake=time.localtime().tm_hour
			else:
				print('Alarm off all functions enabled')
				speak('Alarm off all functions enabled')
				q=q+1
		elif 'learn' in arg :
			speak('Please provide the path to dataset file')
			q=q+1
			data_path=str(input('Please provide the path to dataset file : '))
			data=pd.read_csv(data_path)
			speak('Which column shall i consider as the label')
			q=q+1
			label=str(input('Which column shall i consider as the label : '))
			score_dict={}
			l=[]
			for w in data.columns:
				speak('Shall i consider '+w+' for learning')
				q=q+1
				c_w=str(input('Shall i consider '+w+' for learning (y/n) : '))
				if c_w=='y':
					l.append(w)
			print(l)
			time_start=time.time()
			X=data[l]
			y=data[label]
			X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
			linear_reg=LinearRegression()
			linear_reg.fit(X_train,y_train)
			score=linear_reg.score(X_test,y_test)
			score_dict['linear_regression']=round(score,2)
			time_end=time.time()
			train_state=0
			if (time_end-time_start)>25:
				speak('This is a large dataset and learning time can take from 1 minute to 5 Hours')
				q=q+1
				print('This is a large dataset and learning time can take from 1 minute to 5 Hours')
			try:
				logistic_reg=LogisticRegression()
				X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
				logistic_reg.fit(X_train,y_train)
				score_dict['logistic_regression']=round(score,2)
				train_state=1
			except:
				try:
					lab_enc = preprocessing.LabelEncoder()
					training_scores_encoded = lab_enc.fit_transform(y_train)
					test_encoded=lab_enc.fit_transform(y_test)
					logistic_reg=LogisticRegression()
					X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
					logistic_reg.fit(X_train,training_scores_encoded)
					score=logistic_reg.score(X_test,test_encoded)
					score_dict['logistic_regression']=round(score,2)
					train_state=2
				except:
					lab_enc = preprocessing.LabelEncoder()
					training_scores_encoded = lab_enc.fit_transform(X_train)
					test_encoded=lab_enc.fit_transform(X_test)
					logistic_reg=LogisticRegression()
					X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
					logistic_reg.fit(training_scores_encoded,y_train)
					score=logistic_reg.score(test_encoded,y_test)
					score_dict['logistic_regression']=round(score,2)
					train_state=3
			pref_algo=max(score_dict)
			speak('Appointed'+pref_algo+'as preffered algorithm for learning')
			q=q+1
			print('Appointed',pref_algo,'as preffered algorithm for learning')
			speak('Learning Done')
			q=q+1
			print('Learning Done')
			speak('Dataset has been learned,Do you want me to predict state of any datapoint')
			q=q+1
			pred_t_f=str(input('Dataset has been learned,Do you want me to predict state of any datapoint(y/n) : '))
			if pred_t_f=='y':
				user_query_pred=[]
				for v in l:
					inp=float(input(v+' : '))
					user_query_pred.append(inp)
				user_query_pred=np.array([user_query_pred])
				if pref_algo=='logistic_regression':
					prediction=logistic_reg.predict(user_query_pred)
					print(label,' : ',prediction)
					print(score_dict)
				else:
					prediction=linear_reg.predict(user_query_pred)
					print(label,': ',prediction)
					speak('Predicted'+label+'is'+prediction)
					q=q+1
			speak('Do you want me to save the learning')
			q=q+1
			save_data=str(input('Do you want me to save the learning (y/n) : '))
			if save_data=='y':
				data_name=str(input('Dataset Name : '))
				data_info=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\Datasets_info.txt','a')
				data_info.write('\n')
				data_info.write(data_name)
				data_info.close()
				file=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\'+data_name+'.txt','a')
				file_l=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\'+data_name+'_l.data','wb')
				file.write(pref_algo)
				file.write(' ')
				file.write(data_path)
				file.write(' ')
				file.write(str(train_state))
				file.write(' ')
				file.write(label)
				file.close()
				pickle.dump(l,file_l)
				file_l.close()
		elif 'predict' in arg or 'load' in arg and 'dataset' in arg or 'estimate' in arg and 'value' in arg :
			data_info=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\Datasets_info.txt','r')
			info=data_info.read()
			speak(info)
			q=q+1
			print(info)
			dataset_name=str(input('Dataset Name : '))
			try:
				file=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\'+dataset_name+'.txt','r')
				file_l=open('C:\\Users\\siddhant\\Desktop\\Samridh\\codes\\Projects\\Murph_assistant\\Murph_learned_data\\'+dataset_name+'_l.data','rb')
				dat=file.read()
				data_list=dat.split(' ')
				pref_algo=data_list[0]
				print(pref_algo)
				path=data_list[1]
				cols=pickle.load(file_l)
				cols=np.array(cols)
				train_state=int(data_list[2])
				label=data_list[3]
				data=pd.read_csv(path)
				X=data[cols]
				y=data[label]
				if pref_algo=='linear_regression':
					X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
					linear_reg=LinearRegression()
					linear_reg.fit(X_train,y_train)
					pred_arr=[]
					for w in cols:
						query=float(input(w+' : '))
						pred_arr.append(query)
					pred_arr=np.array([pred_arr])
					prediction=linear_reg.predict(pred_arr)
					speak('Predicted'+label+'is'+prediction)
					q=q+1
					print(label,' : ',prediction)
				elif pref_algo=='logistic_regression':
					X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
					logistic_reg=LogisticRegression()
					if train_state==1:
						logistic_reg.fit(X_train,y_train)
						pred_arr=[]
						for w in cols:
							query=float(input(w+' : '))
							pred_arr.append(query)
						pred_arr=np.array([pred_arr])
						prediction=logistic_reg.predict(pred_arr)
						speak('Predicted'+label+'is'+prediction)
						q=q+1
						print(label,' : ',prediction)
					elif train_state==2:
						lab_enc = preprocessing.LabelEncoder()
						training_scores_encoded = lab_enc.fit_transform(y_train)
						test_encoded=lab_enc.fit_transform(y_test)
						X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
						logistic_reg.fit(X_train,training_scores_encoded)
						pred_arr=[]
						for w in cols:
							query=float(input(w+' : '))
							pred_arr.append(query)
						pred_arr=np.array([pred_arr])
						prediction=logistic_reg.predict(pred_arr)
						speak('Predicted'+label+'is'+prediction)
						q=q+1
						print(label,' : ',prediction)
					elif train_state==3:
						lab_enc = preprocessing.LabelEncoder()
						training_scores_encoded = lab_enc.fit_transform(X_train)
						test_encoded=lab_enc.fit_transform(X_test)
						logistic_reg=LogisticRegression()
						X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
						logistic_reg.fit(training_scores_encoded,y_train)
						pred_arr=[]
						for w in cols:
							query=float(input(w+' : '))
							pred_arr.append(query)
						pred_arr=np.array([pred_arr])
						prediction=logistic_reg.predict(pred_arr)
						speak('Predicted'+label+'is'+prediction)
						q=q+1
						print(label,' : ',prediction)
			except:
				speak('Error encountered please check the dataset name and if  all the resources are in place')
				q=q+1
				print('Error encountered please check the dataset name and if  all the resources are in place')