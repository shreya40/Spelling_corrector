```

from textblob import TextBlob
from tkinter import *


def correct_spelling():
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    entry2.delete(0, END)
    entry2.insert(0, data)


def main_window():
    global entry1, entry2
    win = Tk()
    win.geometry("500x380")
    win.resizable(False,False)
    win.config(bg="white")
    win.title("my window")
    label1 = Label(win, text="enter your spelling", font=("Time New Roman", 25, "bold"), bg="grey", fg="white")
    label1.place(x=100, y=40, height=50, width=300)

    entry1 = Entry(win, text="enter your spelling", font=("Time New Roman", 20))
    entry1.place(x=50, y=100, height=50, width=400)

    label2 = Label(win, text="correct spelling", font=("Time New Roman", 25, "bold"), bg="grey", fg="white")
    label2.place(x=100, y=160, height=50, width=300)

    entry2 = Entry(win, text="correct spelling", font=("Time New Roman", 20))
    entry2.place(x=50, y=220, height=50, width=400)

    button = Button(win, text="Done", font=("Time New Roman", 25, "bold"), command=correct_spelling)
    button.place(x=150, y=300, height=50, width=200)
    win.mainloop()


main_window()

```
