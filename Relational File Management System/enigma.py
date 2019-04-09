# INTRODUCTION :
# NOWADAYS BEING A PROGRAMMER THE MAJOR ISSUE IS OF CONNECTING SEVERAL SEGMENTS OF A PROGRAM AT DIFFERENT LOCATIONS TOGETHER
# OR OF TRANSFERRING LARGE CHUNKS OF PROGRAM FROM ONE LOCATION TO ANOTHER ON OUR SYSTEMS.WHEN WE CREATE A PROGRAM MOST OF THE TIME
# WE IMPORT SEVERAL PROGRAMS AT DIFFERENT LOCATIONS IN OUR COMPUTER INTO OUR SOURCE FILE AND THUS INCREASING THE PROCESSING TIME
# THUS INTRODUCING ENIGMA WHICH CAN HELP IN TRANSFERRING LARGE DATA FROM ONE FILE INTO ANOTHER IN A FLUENT AND USER FRIENDLY MANNER
# NOW THE USER DOESNT NEED TO COPY PASTE OR IMPORT PROGRAM FROM DIFFERENT LOCATIONS INTO THE SOURCE FILE WITH THE HELP OF ENIGMA 
# THE USER CAN EASILY HANDLE LARGE PROGRAM FILES WITHOUT EVEN OPENING THEM.IF THE USER WANTS TO ADD DATA FROM ONE LARGE FILE INTO
# ANOTHER LARGE FILE THEN WITHOUT OPENING ANY OF THEM AND WASTING TIME IN WAITING FOR THE FILES TO OPEN THE USER CAN DIRECTLY
# ACCESS THERE DATA AND CAN EXPORT THE DATA INTO A NEW FILE,ADD THAT DATA INTO ANOTHER FILE(EG.SOURCE FILE) AND CAN DELETE DATA
# FROM THE FILE WHERE THE DATA HAS BEEN ADDED OR EXPORTED PREVIOUSLY USING ENIGMA .

# ADDING DATA OF ONE FILE INTO ANOTHER FILE :
# THINK OF A CONDITION WHEN WE ARE MAKING A SOFTWARE AND WE HAVE A GIGANTIC PROGRAM WHICH ACTS AS A FUNCTION OF OUR SOFTWARE
# BUT IS TOO BIG AND AT A DIFFERENT LOCATION AND IS INCREASING OUR SOFTWARES PROCESSING TIME ,NOW USER CAN EITHER ADD THE FUNCTIONS
# PROGRAMMING INTO THE SOURCE FILE BUT OPENING THOSE GIGANTIC PROGRAMS CAN TAKE A LOT OF TIME ON AN AVERAGE COMPUTER THUS WITH 
# ENIGMA THE USER CAN EASILY TRANSFER THE GIGANTIC PROGRAM OF FUNCTION INTO THE SOURCE FILE IN 1/10TH TIME TAKEN BY COPY
# AND PASTING THE PROGRAMMING . ENIGMA ALLOWS USER TO OPERATE WITHIN FILES AT SIMMILAR LOCATIONS AS WELL AS DIFFERENT LOCATIONS


# EXPORTING DATA INTO A NEW FILE :
# THIS METHOD IS ALSO USEFUL FOR PROGRAMMER BECAUSE IF A PROGRAMMER IS TRYING TO CREATE A SOURCE FILE BY COMPILING SEVERAL SEGMENTS
# THE EXPORT METHOD IS A GOOD FUNCTION FOR TRANSFERRING LARGE FILES FROM COMPUTER INTO AN EXTERNAL DRIVE OR INTO ANOTHER FOLDER
# THE EXPORT METHOD IS ALSO USEFUL AS IT CAN BE USED TO CREATE MULTIPLECOPIES OF A PROGRAM FILE 

# REMOVING DATA FROM A FILE :
# ENIGMA HAS THE FULL CAPABILITY TO REMOVE DATA FROM A FILE WHERE DATA HAS PREVIOUSLY BEEN ADDED OR EXPORTED USING ENIGMA
# WHEN WE HAVE TO REMOVE SOME DATA FROM A LARGE PROGRAMMING FILE ONE OF THE MAJOR PROBLEM IS FINDING THAT PARTICULAR PHASE WITH
# THAT PARTICULAR PROGRAMMING LINE'S WHICH WE WANT TO REMOVE THUS WITH ENIGMA AFTER EVERY TRANSFER THE TRANSFERRED DATA'S SECOND
# COPY IS STORED AND IS GIVEN A NUMBER WHICH IS IN SEQUENCE TO TRANSACTION LIKE THE DATA TRANSFERRED IN 3RD TRANSACTION WILL BE STORED
# IN FILE '3.TXT'.
# USING ENIGMA WITHOUT OPENING THE LARGE FILES WE CAN EASILY DELETE DATA FROM THE FILE AND THUS ELIMINATING THE TIME WASTED IN 
# OPENING THE FILE


import os.path
import time

from tkinter import *
from tkinter import filedialog
from tkinter import ttk

window = Tk()
window.geometry('300x225')
a=0
b = 0
img = PhotoImage(file='bg.png')

def removef():
	
	
	window1 = Toplevel()
	window1.geometry('300x225')
	img1 = PhotoImage(file='bg.png')
	
	def file():
		global de_name
		de_name = filedialog.askopenfilename()
	def sfile():
		global de_sf
		de_sf = filedialog.askopenfilename()
	def start():
		with open(de_sf,mode='r')as se:
			k=se.read() # Reading the data in saving
		with open(de_name,mode='r+')as fe :

			f=fe.read() # Reading the data of the source file 
			length=len(k) # Finding the length of the data is savings 
			i=0  # A variable to keep the process going until the whole content of savings is deleted from the source file
			if k in f and i<length :
				p=f.index(k) # Finding the index of content in source file
				fe.truncate(p) # Deleting the data at that index in source file
				i+=1 # Increment of the variable
	l = Label(window1,image=img1).place(x=0,y=0)
	

        #Label(window,image=img).place(x=0,y=0)
	btn1 = ttk.Button(window1,text='browse the file',command=file).grid(padx=110,pady=20,ipadx=12)
	btn2 = ttk.Button(window1,text='browse the save file',command=sfile).grid(padx=110,pady=20,ipadx=0)
	btn3 = ttk.Button(window1,text='start',command=start).grid(padx=110,pady=20,ipadx=20)

	window1.mainloop()

				
def addf():
		
	global a
		
		
	window3 = Toplevel()
	window3.geometry('300x225')
	img1 = PhotoImage(file='bg.png')
	
				
	def nbt():
		global name1
		name1 = filedialog.askopenfilename()

	def nebt():
		global name2
		name2 = filedialog.askopenfilename()
				
	def start():
		global a
		name=name1
		print(name)
		new_nm=name2
		start_time=time.time()
		with open(name,mode='r')as n:
			y=n.read()
		with open(new_nm,mode='r')as nm:
			r=nm.read()
		with open(new_nm,mode='w')as nm:
			nm.write(r)
			nm.write(y)
		with open(new_nm,mode='r')as nm:
			n=nm.read()
			nm.read()
		end_time=time.time()
		time_taken=end_time-start_time
		
		Label(window3,text='Time taken : {0:.2} Seconds'.format(time_taken)).grid()
				
		sv=str(a)+' '+'savefile'+'.txt'
		a+=1 
		with open(sv,mode='w')as s:
			s.write(n)
		with open(sv,mode='r')as s:
			s.read()
	Label(window3,image=img1).place(x=0,y=0)
	nbtn = ttk.Button(window3,text='browse source file',command=nbt).grid(padx=90,pady=20,ipadx=11)
	newbtn = ttk.Button(window3,text='browse target file',command=nebt).grid(padx=90,pady=20,ipadx=12)
	
			
	startbtn = ttk.Button(window3,text='start',command=start).grid(padx=90,pady=20,ipadx=24)
	window3.mainloop()

		
def exportf():    
	window2 = Toplevel()
	window2.geometry('300x225')
	img1 = PhotoImage(file='bg.png')
	name_var = StringVar()   
	def src():
		global com_src
		com_src=filedialog.askopenfilename()
	
	def name():
		global s_text
		global nfile
		global completeName
		s_text = filedialog.askdirectory(parent=window2,initialdir="/",title='please select a folder')
		nfile = name_var.get()
		completeName = os.path.join(s_text,nfile)
	def start():
		global b
		global com_src
		global a
		completeName = 'new file'+' '+str(b)+'.txt'
		b+=1
		stat=os.stat(com_src) 
		sz=stat.st_size # Finding the size of the file
		est_time=sz/10000000 #Here the size of the file is being divided by 100Mn bytes as speed of this software is taken to be 100mb/sec to calculate th maxiimum time possible 
		start_time=time.time() # Recording the start time
		with open(com_src,mode='r')as r :
			u=r.read()  # Reading the data of source file
		with open(completeName,mode='w')as s :
			s.write(u) # Writing the data into the new file
		with open(completeName,mode='r')as s:
			n=s.read() # Assigning the transfered data to variable "n"
			s.read()   # Completing the process of transfer by reading the file 
		end_time=time.time() # Recording the when the process ends
		time_taken=end_time-start_time # Calculating the time taken by subtracting start time from end time

		 
		Label(window2,text= 'Time taken : {0:.2} Seconds'.format(time_taken)).grid()
		sv=str(a)+' '+'savefile'+'.txt'
		
		with open(sv,mode='w')as s:
			s.write(n)
		with open(sv,mode='r')as s:
			s.read()
		a+=1
	Label(window2,image=img1).place(x=0,y=0)
	btn1 = ttk.Button(window2,text='browse the path to file containing source file',command=src).grid(padx=30,pady=50,ipady=5)

	btn3 = ttk.Button(window2,text='start',command=start).grid(padx=110,pady=30,ipady=5)
		
	

		
	window2.mainloop()

l = Label(window,image=img).place(x=0,y=0)

addbtn = ttk.Button(window,text='add',command=addf).grid(padx=110,pady=20,ipadx=0)

exportbtn = ttk.Button(window,text='export',command=exportf).grid(padx=110,pady=20,ipadx=0)

removebtn = ttk.Button(window,text='remove',command=removef).grid(padx=110,pady=20)


window.mainloop()
