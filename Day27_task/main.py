# import tkinter

# window = tkinter.Tk()
# window.title("Mile to Km converter")
# window.minsize(width=500, height=300)


# input = tkinter.Entry(width=100)
# input.grid(1, 1)

# my_label = tkinter.Label(text="I am a label.", font=("Gothic", 24, "italic"))
# my_label.grid(column=0, row=0)

# input = tkinter.Entry(width=10)
# input.grid(column=1, row=1)

# def button_got_clicked():
#     my_label["text"] = input.get()
# button = tkinter.Button(text="Click Me", command=button_got_clicked)
# button.grid(column=2, row=2)



# window.mainloop()

from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


window.mainloop()