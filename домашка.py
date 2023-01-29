from tkinter import *
root = Tk()
root.title('Домашняя работа')
root.geometry('600x500')
canvas = Canvas(root, width=300, height=400, bg='white')
canvas.pack()
def color1():
    canvas.itemconfig(oval,fill='red', outline='red')
def color2():
    canvas.itemconfig(rectangle, fill='blue', outline='blue')
def color3():
    canvas.itemconfig(polygon, fill='black', outline='black')
rectangle = canvas.create_rectangle(50,400,250,250, width=5, fill='grey',
outline='grey')
polygon = canvas.create_polygon([25,250],[275,250],[150,70], fill='brown')
oval = canvas.create_oval(300,10,200,103, width=1, fill='yellow', outline='yellow')
b1 = Button(root, height=1, width=10, text='Солнце',
                bg='pink', activebackground='white', command=color1)
b2 = Button(root, height=1, width=10, text='Стены',
                bg='pink', activebackground='white', command=color2)
b3 = Button(root, height=1, width=10, text='Крыша',
                bg='pink', activebackground='white', command=color3)
b1.pack()
b2.pack()
b3.pack()
root.mainloop()