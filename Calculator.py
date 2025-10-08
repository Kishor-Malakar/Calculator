from tkinter import *

def click(a):
    global val
    text=a.widget.cget("text")
    if text=="=":
        if val.get().isdigit():
            result=str(eval(val.get()))
        else:
            try:
                result=eval(val.get())
                
            except Exception as e:
                print(e)
                result=("Error")
        val.set(result)
    elif text=="C":
        val.set("")
    else:
        val.set(val.get()+text)
        
root = Tk()
root.geometry("300x450")
root.title("Calculator By dot dot dot")
root.resizable(0,0)
#root.wm_iconbitmap("") 

val = StringVar()
val.set("")
disp = Entry(root, textvar=val, font="font 40 bold")
disp.pack(fill=X, pady=15, padx=10)

frame= Frame(root, bg="white")
button= Button(frame, text="7", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="8", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="9", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="/", padx=11, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

frame.pack()


frame= Frame(root, bg="white")
button= Button(frame, text="4", padx=9, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="5", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=3, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="6", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="*", padx=9, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

frame.pack()



frame= Frame(root, bg="white")
button= Button(frame, text="1", padx=9, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="2", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="3", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="-", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

frame.pack()


frame= Frame(root, bg="white")
button= Button(frame, text="C", padx=6, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="0", padx=10, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="=", padx=9, pady=8, font="font 25")
button.pack(side=LEFT, padx=3, pady=2)
button.bind("<Button>", click)

button= Button(frame, text="+", padx=6, pady=8, font="font 25")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button>", click)

frame.pack()


root.mainloop()
