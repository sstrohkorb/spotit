from Tkinter import *

root = Tk()

root.title("Spot-It Game Options")
root.geometry("200x500")

e = Entry(root)
e.pack()
e.focus_set()

def callback():
    print e.get()

b = Button(root, text="get", width=10, command=callback)
b.pack()

# Checkbutton Widget
var = IntVar()
var2 = IntVar()
c1 = Checkbutton(root, text="Expand", variable=var)
c1.pack()
c2 = Checkbutton(root, text="Second Choice", variable=var2)
c2.pack()

#Litbox Widget
listbox = Listbox(root)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
    
#Radiobutton Widget
v = IntVar()

Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)


mainloop()
