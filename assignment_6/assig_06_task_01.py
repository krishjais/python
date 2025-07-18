from tkinter import * 

window = Tk()
window.geometry("500x500")

e = Entry(window, width= 56, borderwidth= 5)
e.place(x = 0, y= 0)

def click (num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))



b = Button(window, text ="1" , width = 12, command = lambda:click(1)) #one
b.place(x = 10 , y = 60)

b = Button(window, text ="2" , width = 12, command = lambda:click(2)) #two
b.place(x = 80 , y = 60)

b = Button(window, text ="3" , width = 12, command = lambda:click(3)) #three
b.place(x = 170 , y = 60)

b = Button(window, text ="4" , width = 12, command = lambda:click(4)) #four
b.place(x = 10 , y = 120)

b = Button(window, text ="5" , width = 12, command = lambda:click(5)) #five
b.place(x = 80 , y = 120)

b = Button(window, text ="6" , width = 12, command = lambda:click(6)) #six
b.place(x = 170 , y = 120)

b = Button(window, text ="7" , width = 12, command = lambda:click(7)) #seven
b.place(x = 10 , y = 180)

b = Button(window, text ="8" , width = 12, command = lambda:click(8)) #eight
b.place(x = 80 , y = 180)

b = Button(window, text ="9" , width = 12, command = lambda:click(9)) #nine
b.place(x = 170 , y = 180)

b = Button(window, text ="0" , width = 12, command = lambda:click(0)) #zero
b.place(x = 10 , y = 240)


def add():
    n1 = e.get()
    global math 
    math = "addition"
    global i 
    i  = int(n1)
    e.delete(0, END)

b = Button(window, text ="+" , width = 12, command = add) #plus
b.place(x = 80 , y = 240)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i 
    i  = int(n1)
    e.delete(0, END)


b = Button(window, text ="-" , width = 12, command = sub) #minus
b.place(x = 170 , y = 240)


def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i 
    i  = int(n1)
    e.delete(0, END)


b = Button(window, text ="*" , width = 12, command = mult) #multiply
b.place(x = 10 , y = 300)

def div():
    n1 = e.get()
    global math
    math = "divison"
    global i 
    i  = int(n1)
    e.delete(0, END)



b = Button(window, text ="/" , width = 12, command = div) #divide
b.place(x = 80 , y = 300)


def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "substraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))


b = Button(window, text ="=" , width = 12, command = equal) #result
b.place(x = 170 , y = 300)


def clear():
    e.delete(0,END)

b = Button(window, text ="Clear" , width = 12, command = clear) #clear
b.place(x = 10 , y = 360)




mainloop()