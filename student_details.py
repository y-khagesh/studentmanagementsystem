from tkinter import *
from tkinter import messagebox,filedialog
import time
import ttkthemes

from tkinter import ttk
import pymysql
import pandas

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')

def updatestudent():
    def update_data():
        currentdate=time.strftime('%d/%m/%y')
        currenttime = time.strftime('%H:%M:%S')
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,DOB=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(namelabelentry.get(),mobilelabelentry.get(),emaillabelentry.get(),addresslabelentry.get(),genderlabelentry.get(),DOBlabelentry.get(),currentdate,currenttime,idlabelentry.get()))
        con.commit()
        messagebox.showinfo('Success',f'id {idlabelentry.get()} is modified successfully')
        updatestudentwindow.destroy()
        showstudent()


    updatestudentwindow = Toplevel()
    updatestudentwindow.resizable(0,0)
    updatestudentwindow.grab_set()
    updatestudentwindow.title('update window')
    idlabel = Label(updatestudentwindow, text='Id', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0)
    idlabelentry = Entry(updatestudentwindow)
    idlabelentry.grid(row=0, column=1, padx=10, pady=10)

    namelabel = Label(updatestudentwindow, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0)
    namelabelentry = Entry(updatestudentwindow)
    namelabelentry.grid(row=1, column=1, padx=10, pady=10)

    mobilelabel = Label(updatestudentwindow, text='Mobile', font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=0)
    mobilelabelentry = Entry(updatestudentwindow)
    mobilelabelentry.grid(row=2, column=1, padx=10, pady=10)

    emaillabel = Label(updatestudentwindow, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=3, column=0)
    emaillabelentry = Entry(updatestudentwindow)
    emaillabelentry.grid(row=3, column=1, padx=10, pady=10)

    addresslabel = Label(updatestudentwindow, text='Address', font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=4, column=0)
    addresslabelentry = Entry(updatestudentwindow)
    addresslabelentry.grid(row=4, column=1, padx=10, pady=10)

    genderlabel = Label(updatestudentwindow, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=5, column=0)
    genderlabelentry = Entry(updatestudentwindow)
    genderlabelentry.grid(row=5, column=1, padx=10, pady=10)

    DOBlabel = Label(updatestudentwindow, text='DOB', font=('times new roman', 20, 'bold'))
    DOBlabel.grid(row=6, column=0)
    DOBlabelentry = Entry(updatestudentwindow)
    DOBlabelentry.grid(row=6, column=1, padx=10, pady=10)

    updatestudentwindow_button = ttk.Button(updatestudentwindow, text='update student',command=update_data)
    updatestudentwindow_button.grid(row=7, column=1, columnspan=2)

    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    print(content)
    content_list = content['values']
    print(content_list)
    idlabelentry.insert(0, content_list[0])
    namelabelentry.insert(0,content_list[1])
    mobilelabelentry.insert(0,content_list[2])
    emaillabelentry.insert(0,content_list[3])
    addresslabelentry.insert(0,content_list[4])
    genderlabelentry.insert(0,content_list[5])
    DOBlabelentry.insert(0,content_list[6])


def showstudent():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def deletestudent():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    print(content)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)





def searchstudent():
    def search_data():
        if idlabelentry.get()=='' and namelabelentry.get()=='' and mobilelabelentry.get()=='' and emaillabelentry.get()=='' and addresslabelentry.get()=='' and genderlabelentry.get()=='' and  DOBlabelentry.get()=='' :
            messagebox.showerror('Error','empty data not allowed',parent=searchstudentwindow)
        query='select *from student where id=%s or name=%s or mobile=%s or email=%s or address=%s or  gender=%s or DOB=%s '
        mycursor.execute(query,
                         (idlabelentry.get(), namelabelentry.get(), mobilelabelentry.get(), emaillabelentry.get(),
                          addresslabelentry.get(),
                          genderlabelentry.get(), DOBlabelentry.get()))
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)
    searchstudentwindow = Toplevel()
    searchstudentwindow.resizable(0, 0)
    searchstudentwindow.grab_set()
    searchstudentwindow.title('search window')
    idlabel = Label(searchstudentwindow, text='Id', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0)
    idlabelentry = Entry(searchstudentwindow)
    idlabelentry.grid(row=0, column=1, padx=10, pady=10)

    namelabel = Label(searchstudentwindow, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0)
    namelabelentry = Entry(searchstudentwindow)
    namelabelentry.grid(row=1, column=1, padx=10, pady=10)

    mobilelabel = Label(searchstudentwindow, text='Mobile', font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=0)
    mobilelabelentry = Entry(searchstudentwindow)
    mobilelabelentry.grid(row=2, column=1, padx=10, pady=10)

    emaillabel = Label(searchstudentwindow, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=3, column=0)
    emaillabelentry = Entry(searchstudentwindow)
    emaillabelentry.grid(row=3, column=1, padx=10, pady=10)

    addresslabel = Label(searchstudentwindow, text='Address', font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=4, column=0)
    addresslabelentry = Entry(searchstudentwindow)
    addresslabelentry.grid(row=4, column=1, padx=10, pady=10)

    genderlabel = Label(searchstudentwindow, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=5, column=0)
    genderlabelentry = Entry(searchstudentwindow)
    genderlabelentry.grid(row=5, column=1, padx=10, pady=10)

    DOBlabel = Label(searchstudentwindow, text='DOB', font=('times new roman', 20, 'bold'))
    DOBlabel.grid(row=6, column=0)
    DOBlabelentry = Entry(searchstudentwindow)
    DOBlabelentry.grid(row=6, column=1, padx=10, pady=10)

    searchstudentwindow_button = ttk.Button(searchstudentwindow, text='Search student', command=search_data)
    searchstudentwindow_button.grid(row=7, column=1, columnspan=2)


def addstudent():
    def add_data():
        if idlabelentry.get()=='' or namelabelentry.get()=='' or mobilelabelentry.get()=='' or emaillabelentry.get()=='' or addresslabelentry.get()=='' or genderlabelentry.get()=='' or  DOBlabelentry.get()=='' :
            messagebox.showerror('Error','empty data not allowed',parent=addstudentwindow)
        else:
            try:
                 currentdate = time.strftime('%d/%m/%y')
                 currenttime = time.strftime('%H:%M:%S')
                 query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                 mycursor.execute(query,
                             (idlabelentry.get(), namelabelentry.get(), mobilelabelentry.get(), emaillabelentry.get(), addresslabelentry.get(),
                              genderlabelentry.get(), DOBlabelentry.get(), currentdate, currenttime))
                 con.commit()
                 result=messagebox.askyesno('data successfully added','if u want to clean the data')
                 print(result)
                 if result:
                   idlabelentry.delete(0,END)
                   namelabelentry.delete(0, END)
                   mobilelabelentry.delete(0, END)
                   emaillabelentry.delete(0, END)
                   addresslabelentry.delete(0, END)
                   genderlabelentry.delete(0, END)
                   DOBlabelentry.delete(0, END)
                 else:
                     pass
            except:
                  messagebox.showerror('Error', 'Id cannot be repeated')

            query ='select *from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('', END, values=data)

    addstudentwindow =Toplevel()
    addstudentwindow.resizable(0,0)
    addstudentwindow.grab_set()
    idlabel=Label(addstudentwindow,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0)
    idlabelentry=Entry(addstudentwindow)
    idlabelentry.grid(row=0, column=1,padx=10,pady=10)

    namelabel = Label(addstudentwindow, text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1, column=0)
    namelabelentry= Entry(addstudentwindow)
    namelabelentry.grid(row=1, column=1,padx=10,pady=10)

    mobilelabel = Label(addstudentwindow, text='Mobile',font=('times new roman',20,'bold'))
    mobilelabel.grid(row=2, column=0)
    mobilelabelentry = Entry(addstudentwindow)
    mobilelabelentry.grid(row=2, column=1,padx=10,pady=10)

    emaillabel = Label(addstudentwindow, text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=3, column=0)
    emaillabelentry = Entry(addstudentwindow)
    emaillabelentry.grid(row=3, column=1,padx=10,pady=10)

    addresslabel = Label(addstudentwindow, text='Address',font=('times new roman',20,'bold'))
    addresslabel.grid(row=4, column=0)
    addresslabelentry = Entry(addstudentwindow)
    addresslabelentry.grid(row=4, column=1,padx=10,pady=10)

    genderlabel = Label(addstudentwindow, text='Gender',font=('times new roman',20,'bold'))
    genderlabel.grid(row=5, column=0)
    genderlabelentry = Entry(addstudentwindow)
    genderlabelentry.grid(row=5, column=1,padx=10,pady=10)

    DOBlabel =Label(addstudentwindow, text='DOB',font=('times new roman',20,'bold'))
    DOBlabel.grid(row=6, column=0)
    DOBlabelentry = Entry(addstudentwindow)
    DOBlabelentry.grid(row=6, column=1,padx=10,pady=10)


    addstudentwindow_button=ttk.Button(addstudentwindow,text='Add student',command=add_data)
    addstudentwindow_button.grid(row=7,column=1,columnspan=2)


def connect_database():

    def connect():
        global mycursor,con
        try:
             con=pymysql.connect(host=hostnameentry.get(),user=usernameentry.get(),password=passwordentry.get())
             mycursor=con.cursor()
             
        except:
               messagebox.showerror('error', 'invalid details',parent=connectwindow)
               return
        try:
               query='create database studentmanagementsystem'
               mycursor.execute(query)
               query='use studentmanagementsystem'
               mycursor.execute(query)
               query='create table student(id int not null primary key, name varchar(30) , mobile varchar(10),email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50) )'
               mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful')
        connectwindow.destroy()

        addstudentbutton.config(state=NORMAL)
        searchbutton.config(state=NORMAL)
        updatebutton.config(state=NORMAL)
        showbutton.config(state=NORMAL)
        Exportbutton.config(state=NORMAL)
        deletebutton.config(state=NORMAL)
        exitbutton.config(state=NORMAL)






    connectwindow =Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.resizable(0,0)
    connectwindow.title('connection window')

    hostname=Label(connectwindow,text='Hostname:',font=('arial',20,'bold'))
    hostname.grid(row=1,column=1,padx=10)

    hostnameentry=Entry(connectwindow,font=('arial',20,'bold'))
    hostnameentry.grid(row=1,column=2)




    username=Label(connectwindow,text='Username:',font=('arial',20,'bold'))
    username.grid(row=2,column=1,padx=10,pady=15)

    usernameentry = Entry(connectwindow, font=('arial', 20, 'bold'))
    usernameentry.grid(row=2, column=2,pady=15)

    password=Label(connectwindow,text='Password:',font=('arial',20,'bold'))
    password.grid(row=3,column=1,padx=10,pady=15)

    passwordentry = Entry(connectwindow, font=('arial', 20, 'bold'))
    passwordentry.grid(row=3, column=2,pady=15)

    c_connectbutton=ttk.Button(connectwindow,text='Connect',command=connect)
    c_connectbutton.grid(row=4,columnspan=4)


def clock():
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datelabel.config(text=f'Date:{date} \nTime:{currenttime}')
    datelabel.after(1000,clock)
count=0
text=''

def slider():
 global text,count
 if count==len(s):
     count=0
     text=''
 text=text+s[count]
 count +=1
 sliderlabel.config(text=text)
 sliderlabel.after(300,slider)





root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')


root.title('student details')
root.geometry('1280x700+0+0')
root.resizable(0,0)



datelabel=Label(root,text='date',font=('times new roman',20,'bold'))
datelabel.place(x=5,y=5)
clock()

s='Student Management system'
sliderlabel=Label(root,text='s',font=('times new roman', 30,'bold'),width=30)
sliderlabel.place(x=300,y=0)
slider()

connectbutton=ttk.Button(root,text='Connect_database',command=connect_database)
connectbutton.place(x=1040,y=0)


leftframe=ttk.Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

students2image=PhotoImage(file='2students.png')
students2imagelabel=Label(leftframe,image=students2image)
students2imagelabel.grid(row=0,column=1,pady=8)

addstudentbutton=ttk.Button(leftframe,text='Add student',width=20,state=DISABLED,command=addstudent)
addstudentbutton.grid(row=2,column=1,pady=8)


searchbutton=ttk.Button(leftframe,text='Search student',state=DISABLED,width=20,command=searchstudent)
searchbutton.grid(row=4,column=1,pady=8)

deletebutton=ttk.Button(leftframe,text='Delete student',state=DISABLED,width=20,command=deletestudent)
deletebutton.grid(row=6,column=1,pady=8)

updatebutton=ttk.Button(leftframe,text='Update student',state=DISABLED,width=20,command=updatestudent)
updatebutton.grid(row=8,column=1,pady=8)

showbutton=ttk.Button(leftframe,text='Show student',state=DISABLED,width=20,command=showstudent)
showbutton.grid(row=10,column=1,pady=8)

Exportbutton=ttk.Button(leftframe,text='Export student',state=DISABLED,width=20,command=export_data)
Exportbutton.grid(row=12,column=1,pady=8)

exitbutton=ttk.Button(leftframe,text='Exit',state=DISABLED,command=iexit)
exitbutton.grid(row=14,column=1,pady=8)

rightframe=ttk.Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
scrollbary=Scrollbar(rightframe,orient=VERTICAL)
studentTable=ttk.Treeview(rightframe,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

scrollbarx.config(command=studentTable.xview)
scrollbary.config(command=studentTable.yview)

studentTable.pack(fill=BOTH,expand=1)

scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.config(show='headings')


root.mainloop()
