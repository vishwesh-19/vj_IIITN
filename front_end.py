from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background = "grey");

f_name = Label(window ,text = "First Name").grid(row = 0,column = 0)            # defining labels for the text widgets
l_name = Label(window ,text = "Last Name").grid(row = 1,column = 0)
e_mail = Label(window ,text = "Email Id").grid(row = 2,column = 0)
contact = Label(window ,text = "Contact Number").grid(row = 3,column = 0)

f_name_1 = Entry(window).grid(row = 0,column = 1)                                   # Text widget for First name
l_name_1 = Entry(window).grid(row = 1,column = 1)                                   # Text widget for Last name
e-mail_1 = Entry(window).grid(row = 2,column = 1)                                   # Text widget for e-mail
contact_no = Entry(window).grid(row = 3,column = 1)                                 # Text widget for contact no.

def clicked():
   msg = msb.showinfo("button clicked" , "We will try to help you as soon as possible ")
 
btn = ttk.Button(window ,text="Seek Help" ,command="clicked()").grid(row=4,column=0)
window.mainloop()
