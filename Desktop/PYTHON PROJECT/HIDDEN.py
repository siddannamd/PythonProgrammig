from tkinter import*
import random
from tkinter import messagebox
answers = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    'h',
    'i',
    'j',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

words = [
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    'i',
    'o',
    'p',
    'a',
    's',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'z',
    'x',
    'c',
    'v',
    'b',
    'n',
    'm',
]
num=random.randrange(0,len(words),1)
def default():
    global words,answers,num
    l1.configure(text=words[num])
def res():
    global words,answers,num
    num=random.randrange(0,len(words),1)
    l1.config(text=words[num])
    e1.delete(0,END)
def checkans():
    global words,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo(title="Result",message="Success,this is right answer")
        res()
    else:
        messagebox.showerror(title="Result",message="Incorrect")
        e1.delete(0,END)
window=Tk()
window.geometry("350x400+400+300")
window.title("Jumbble Game")
window.configure(bg="#000000")
l1=Label(window,text="Your Text Here",
         font=("bold",18),
         bg="#000000",
         fg="white"
         )
l1.pack(pady=30,ipady=10,ipadx=10)
ans1=StringVar()
e1=Entry(window,
         font=("bold",16),
         textvariable=ans1,
         )
e1.pack(ipady=5,ipadx=5)
bt=Button(window,
          text="Check",
          font=("Comic sans ms",16),
          width=16,
          bg="green",
          fg="white",
          relief=GROOVE,
          command=checkans
          )
bt.pack(pady=40)
bt1=Button(window,
          text="Reset",
          font=("Comic sans ms",16),
          width=16,
          bg="red",
          fg="white",
          relief=GROOVE,
          command=res
          )
bt1.pack()
default()
window.mainloop()