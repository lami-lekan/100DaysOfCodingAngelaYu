from tkinter import *
BLUE = "#1B56FD"

window = Tk()
window.title("To Do List")
window.geometry("300x500")
window.config(background=BLUE, padx=5, pady=10)

ui_label_1 = Label(text="My Day", font=("Arial", 18, "bold"), background=BLUE, fg="white")
ui_label_1.grid(row=0, column=0)

ui_label_2 = Label(text="Saturday, April 26", font=("Arial", 10, "normal"), background=BLUE, fg="white")
ui_label_2.grid(row=1, column=0, columnspan=4)
task_text_box = Entry(width=10)
task_text_box.grid(row=9, column=0)





window.mainloop()
