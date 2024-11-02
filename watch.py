from tkinter import *
import time

root = Tk()
root.title('Часы')
root.resizable(width = False, height = False)


def tic():
    watch.after(1000, tic)
    watch['text'] = time.strftime('%H:%M:%S')


watch = Label(root, font = 'Arial 100')
watch.pack()
tic()


root.mainloop()