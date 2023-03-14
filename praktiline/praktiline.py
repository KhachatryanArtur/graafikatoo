from tkinter import *
import math

def solve():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    
    if not a:
        a_entry.configure(bg="pink")
        return
    if not b:
        b_entry.configure(bg="pink")
        return
    if not c:
        c_entry.configure(bg="pink")
        return
    
    a_entry.configure(bg="white")
    b_entry.configure(bg="white")
    c_entry.configure(bg="white")
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    D = b**2 - 4*a*c
    
    if D < 0:
        result_label.config(text="Juuri pole")
    elif D == 0:
        x = -b / (2*a)
        result_label.config(text=f"Üks juur: x = {x}")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        result_label.config(text=f"Kaks juuri: x1 = {x1}, x2 = {x2}")
    

root = Tk()
root.title("Ruutvõrrandi lahendamine")

a_label = Label(root, text="a = ")
a_label.grid(row=0, column=0, padx=10, pady=10)

a_entry = Entry(root)
a_entry.grid(row=0, column=1, padx=10, pady=10)

b_label = Label(root, text="b = ")
b_label.grid(row=1, column=0, padx=10, pady=10)

b_entry = Entry(root)
b_entry.grid(row=1, column=1, padx=10, pady=10)

c_label = Label(root, text="c = ")
c_label.grid(row=2, column=0, padx=10, pady=10)

c_entry = Entry(root)
c_entry.grid(row=2, column=1, padx=10, pady=10)

solve_button = Button(root, text="Lahendada", command=solve)
solve_button.grid(row=3, column=0, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
