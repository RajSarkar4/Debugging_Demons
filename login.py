from tkinter import *


root = Tk()
root.title("")
root.geometry('310x150')
root.resizable(False, False)
root.config(padx=10,pady=30)


# =============================UI=================================

# Label 
user_name = Label(text="Your Email:", font=("Roboto",12))
Password = Label(text="Password:", font=("Roboto",12))
empty = Label(text="")
user_name.grid(column=0, row=2)
Password.grid(column=0, row=3)
empty.grid(column=0,row=4)

# Entry
user_name_entry = Entry(width=33)
Password_entry = Entry(width=33)
user_name_entry.grid(column=1, row=2, columnspan=2)
Password_entry.grid(column=1, row=3, columnspan=2)

# Button 

login_btn = Button(text="Login")
login_btn.grid(column=1, row=5)




root.mainloop()