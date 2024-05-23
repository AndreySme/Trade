from tkinter import *
from tkinter import ttk

def show_message():
    label["text"] = name_var.get()

root = Tk()
root.geometry("250x200") 
name_var=ttk.StringVar().grid(column=0, row=1)
frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text="").grid(column=0, row=6)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
btn = ttk.Button(text="Click", command=show_message).grid(column=0, row=4)
ent = ttk.Entry(frm, )
ent2 = ttk.Entry(frm, ).grid(column=0, row=2)
ent3 = ttk.Entry(frm, ).grid(column=0, row=3)
root.mainloop()