from tkinter import*
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' and passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Renuka'and passwordEntry.get()=='2211':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import SMS
    else:
        messagebox.showerror('Error','Wrong Password')

window=Tk()

window.geometry("1550x900+0+0")
window.title('Login System for System Management')
window.resizable(False,False)
backgroundImage=PhotoImage(file='background.png')
backgroundLabel=Label(window,image=backgroundImage)
backgroundLabel.place(x=0,y=0)

loginFrame=Frame(window,background='plum1')
loginFrame.place(x=700,y=250)

logoImage=PhotoImage(file='logo.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='username.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='username',compound=LEFT,font=('times new roman',20,'bold'),background='plum1')
usernameLabel.grid(row=1,column=0,pady=10,padx=10)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=10)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='password',compound=LEFT,font=('times new roman',20,'bold'),background='plum1')
passwordLabel.grid(row=2,column=0,pady=10,padx=10)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginButton=Button(loginFrame,text='Login',font=('times new roman',20,'bold'),bd=5,fg='black',width=5,
                   background='white',activebackground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()