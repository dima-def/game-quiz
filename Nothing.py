from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 

car  = {
    'color': '',
    'brand': '',
    'hp': 0 
}
 
def click():
    window = Tk()
    window.title("Ваша машина")
    window.geometry("250x200")
 
button = ttk.Button(text="Создать окно", command=click)
button.pack(anchor=CENTER, expand=1)
button.brand = input('Введите марку машины:')

root.mainloop()