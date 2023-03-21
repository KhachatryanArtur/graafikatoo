import tkinter as tk
from tkinter.font import Font


def show_bahamas_flag():
    canvas.delete("all")
    canvas.create_rectangle(30,50, 300,150,fill="cyan")
    canvas.create_rectangle(30,100, 300,150,fill="yellow")
    canvas.create_rectangle(30,200, 300,150,fill="cyan")
    canvas.create_polygon(30,50,100,125,30,200, fill="black")


def show_estonia_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 50, 300, 150, fill="Blue")
    canvas.create_rectangle(0, 100, 300, 150, fill="Black")
    canvas.create_rectangle(0, 200, 300, 150, fill="White")


def show_russian_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 50, 300, 150, fill="White")
    canvas.create_rectangle(0, 100, 300, 150, fill="Blue")
    canvas.create_rectangle(0, 200, 300, 150, fill="Red")


def create_flag_button(text, command):
    button_font = Font(family="Helvetica", size=14, weight="bold")
    button = tk.Button(root, text=text, font=button_font, command=command)
    button.pack(pady=10)


root = tk.Tk()
root.title("Флаги")
root.configure(background="white")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

create_flag_button("Флаг Багамских островов", show_bahamas_flag)
create_flag_button("Флаг Эстонии", show_estonia_flag)
create_flag_button("Флаг России", show_russian_flag)

root.mainloop()
