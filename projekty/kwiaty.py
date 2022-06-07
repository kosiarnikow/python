from tkinter import *
from datetime import timedelta, date


opcje = ["baobab", "kaktus", "roze"]
# 15 dni, 14 dni, 21 dni

okno = Tk()

okno.geometry("600x400")
napis1 = Label(okno, text="KWIATKI", font=("Comic Sans", 50), fg="green")
napis1.pack()

def display_selected(choice):
    choice = wybor.get()
    dni = 0
    if choice == "baobab":
        dni += 14
    elif choice == "kaktus":
        dni += 15
    elif choice == "roze":
        dni += 21

    napis2 = Label(okno, text=date.today()+ timedelta(dni), font=30)
    napis2.place(x=400, y=300)
# napis2 = Label(okno, text=date.today()+ timedelta(days=10), font=30)
wybor = StringVar(okno)
wybor.set("Jaką rosline chcesz wybrać?") # ustawia wyswietlaną wartość domyślną

window = OptionMenu(okno, wybor, *opcje,command=display_selected)
window.place(x=200, y=100)

napis3 = Label(okno,text="dzisiejsza data:", font="30")
napis3.place(x=250, y=200)

date = date.today()
entry1 = Label(okno, width=30,text=f"{date:%D}")
entry1.place(x=200, y=235)

napis2 = Label(okno, text="kiedy będzie następne podlewanie?           =====>", font=30)
napis2.place(x=10, y=300)

napis2 = Label(okno, text="", font=30)
napis2.place(x=400, y=300)

mainloop()