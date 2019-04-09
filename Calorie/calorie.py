from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()

txtvar = StringVar()
im = PhotoImage(file='b.png')
im2 = PhotoImage(file='a.png')
im3 = PhotoImage(file='BT.png')
im4 = PhotoImage(file='BT1.png')
im5 = PhotoImage(file='BT2.png')
window.iconbitmap('BT.ico')
window.title('Calorie Counter')




#f1 = Frame(window).grid(row=0,column=0)
#f2 = Frame(window).grid(row=2,column=0)
window.geometry('950x550')
window.resizable(False,False)

Font = ('Calibri',22)

abus='''This Has Been developed by Samridh Srivastava'''


def btnclk():
        
        try:                
                n=txtvar.get()
                n = int(n)
                        
                cal=n/20  # 1 calorie per 20 steps


                p=n*720   # Estimating the calories in 720 mins or 12 hrs


                if p>=8000:
                        
                        rc=('Calories Burned = {},\nGreat!!! You have taken care of \nyour bones by being physically active.'.format(cal))

                        lbl1['image'] = im
                        lbl3['text'] = rc
                        lbl4['text']=cal
                        
                        
                        


                else:
                        
                        
                         
                        r='Calories Burned = {},\nYou are close to keeping your bones\n healthy and need to walk a little more\n in order to keep your bones healthy'.format(cal)
                        lbl1['image'] = im2
                        lbl3['text'] = r
                        
                ent.delete(0,'end')
        except:
                pass



def about_us():
        messagebox.showinfo('About us',abus)





def dark():
        bg['image'] = im3
        ent['bg'] = '#141414'
        ent['fg'] = 'white'
        lbl1['fg'] = 'white'
        lbl1['bg'] = '#262626'
        lbl3['fg'] = 'white'
        lbl3['bg'] = '#262626'
        btn['fg'] = 'white'
        btn['bg'] = '#141414'

def light():
        bg['image'] = im4
        ent['bg'] = 'white'
        ent['fg'] = 'black'
        lbl1['fg'] = 'black'
        lbl1['bg'] = 'white'
        lbl3['fg'] = 'black'
        lbl3['bg'] = 'white'
        btn['fg'] = 'black'
        btn['bg'] = 'white'
def colourfull():
        bg['image'] = im5
        ent['bg'] = 'purple'
        ent['fg'] = 'lightgreen'
        lbl1['fg'] = 'lightgreen'
        lbl1['bg'] = 'purple'
        lbl3['fg'] = 'lightgreen'
        lbl3['bg'] = 'purple'
        btn['fg'] = 'lightgreen'
        btn['bg'] = 'purple'
        



menuBar = Menu(window)
window.config(menu=menuBar)

subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='help',menu=subMenu)
subMenu.add_command(label='About us',command=about_us)



subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Theme',menu = subMenu)
subMenu.add_command(label='Dark',command=dark)
subMenu.add_command(label='Light',command=light)
subMenu.add_command(label='colourfull',command=colourfull)


bg = Label(window,image=im3)
bg.place(x=0,y=0)

ent = Entry(window,textvariable=txtvar,font=('Calibri',50),bg='#141414',fg='white',relief='flat')
ent.grid(row=0,column=1,pady=50,padx=20,ipady=15)

lbl1 = Label(window,bg='#262626',fg='white',font=Font,relief='flat')
lbl1.grid(row=1,column=0)
lbl3 = Label(window,font = Font,bg='#262626',fg='white',relief='flat')
lbl3.grid(row=1,column=1)
                        
                        

btn = Button(window,text='check\nsteps',command=btnclk,bg='#141414',fg='white',font=('Calibri',19))
btn.grid(row=0,column=0,ipadx=10,ipady=20,pady=50,padx=10)


window.mainloop()
