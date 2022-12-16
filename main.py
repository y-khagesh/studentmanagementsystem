
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():

        if usernameEntry.get()=='' or passwordEntry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty')
        elif usernameEntry.get() =='khagesh' and passwordEntry.get()=='ykrbtech123#':
            messagebox.showinfo('success','welcome')
            window.destroy()
            import student_details
        else:messagebox.showerror('Error','incorrect details')
window=Tk()

window.geometry('1280x848+0+0')

window.title('login page')

window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='bgimage 2.jpg')

bgLabel=Label(window,image=backgroundImage)

bgLabel.place(x=0,y=0)
LoginFrame=Frame(window)
LoginFrame.place(x=300,y=200)
logoImage=PhotoImage(file='studentlogo 2.png')
logoLabel=Label(LoginFrame,image=logoImage)
logoLabel.grid(row=500,column=100,columnspan=2,pady=4)

userlogo=PhotoImage(file='username.png')
usernameLable=Label(LoginFrame,image=userlogo,text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernameLable.grid(row=501,column=100,padx=10,pady=20)


usernameEntry=Entry(LoginFrame,font=('times new roman',20,'bold'))
usernameEntry.grid(row=501,column=101,pady=10,padx=20)

passwordlogo=PhotoImage(file="lock.png")
passwordLabel=Label(LoginFrame,image=passwordlogo,text='Password',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=502,column=100,padx=20,pady=10)

passwordEntry=Entry(LoginFrame,font=('times new roman',20,'bold'))
passwordEntry.grid(row=502,column=101)

loginbutton=Button(LoginFrame,text='login',font=('times new roman',14,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='green',cursor='hand2',command=login)
loginbutton.grid(row=503,column=101,padx=20,pady=10)

window.mainloop()
