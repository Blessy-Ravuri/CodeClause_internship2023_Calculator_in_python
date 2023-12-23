from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    value = ""
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

    elif text!="c":
        value = scvalue.get()+ text

    scvalue.set(value)
    screen.update()

root = Tk()
root.geometry("600x900")
root.title("Blessy's Calculator")
root.config(bg="purple")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=6, pady=6, padx=6)


for i in range(9 ,0, -3):
    f = Frame(root, bg="#4b371c")
    
    for i in range(i, i-3, -1):
        b = Button(f, text=str(i), padx=7, pady=5, font="lucida 25 bold")
        b.pack(side=LEFT, padx=7, pady=5)
        b.bind("<Button-1>", click)
        
    f.pack()


f = Frame(root, bg="#4b371c")

for char in "0-*":
    b = Button(f, text=char, padx=9, pady=5, font="lucida 25 bold")
    b.pack(side=LEFT, padx=7, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#4b371c")

for char in "/%=":
    b = Button(f, text=char, padx=7, pady=5, font="lucida 25 bold")
    b.pack(side=LEFT, padx=7, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#4b371c")

b = Button(f, text="c", padx=7, pady=5, font="lucida 25 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="clac", padx=7, pady=5, font="lucida 25 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=7, pady=5, font="lucida 25 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()