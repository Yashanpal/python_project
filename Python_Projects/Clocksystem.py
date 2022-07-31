from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("clock")
def time():
    string=strftime('%H:%M:%S')
    #to make clock format for 12 hrs we can use string=strftime('%I:%M:%S: %p')
    #to make clock format for 24 hrs we can use string=strftime('%H:%M:%S:')
    label.config(text=string)
    label.after(1000,time)

label=Label(root, font=("Lato",80),background="black",foreground="white")
label.pack(anchor='center')
time()

mainloop()