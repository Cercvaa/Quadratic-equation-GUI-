
from tkinter import *
import cmath

window = Tk()
window.title("aleksandre's gui")
window.geometry("800x800")
aleko = StringVar()
solve = StringVar()

def search():
    a = float(entry.get())
    b  = float(entry1.get())
    c = float(entry2.get())
    d = abs(b**2-4*a*c)
    x1 = (-b+cmath.sqrt(d))/(2*a)
    x2 = (-b-cmath.sqrt(d))/(2*a)
    aleko.set(str(x1))
    solve.set(str(x2))
    
    
label = Label(window, text = "a:", padx = 10, pady = 10)
label.grid(row = 0, column = 0)

entry = Entry(window)
entry.grid(row = 0, column = 1)

label1 = Label(window, text = "b:", padx = 10, pady = 10)
label1.grid(row = 1, column  = 0)

entry1 = Entry(window)
entry1.grid(row = 1, column = 1)

label2 = Label(window, text = "c:", padx = 10, pady = 10)
label2.grid(row = 2, column = 0)

entry2 = Entry(window)
entry2.grid(row = 2, column = 1)

button1 = Button(window, text = "solve", padx = 10, pady = 10, command = lambda: search())
button1.grid(row = 3, column = 1)

label3 = Label(window, text = "x1:", padx = 10, pady = 10)
label3.grid(row = 4, column = 0)

entry3 = Entry(window, textvariable = aleko)
entry3.grid(row = 4, column = 1)

label4 = Label(window, text = "x2:", padx = 10, pady = 10)
label4.grid(row = 5, column = 0)

entry4 = Entry(window, textvariable = solve)
entry4.grid(row = 5, column = 1)

window.mainloop()

