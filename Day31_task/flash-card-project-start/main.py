from tkinter import *
import pandas as pd
from random import choice
import time
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA ------------------------------- #
try:
    words_df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    words_df = pd.read_csv('data/french_words.csv')
finally:
    words_list = words_df.to_dict(orient='records')
current_word = {}

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_word, flip_timer
    flash_card_window.after_cancel(flip_timer)
    current_word = choice(words_list)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    card_canvas.itemconfig(bg_image, image=card_image_front)
    flip_timer = flash_card_window.after(3000, func=flip_card)

def flip_card():
    card_canvas.itemconfig(bg_image, image=card_image_back)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_word["English"], fill="white")

def is_known():
    words_list.remove(current_word)
    data = pd.DataFrame(words_list)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- USER INTERFACE ------------------------------- #
flash_card_window = Tk()
flash_card_window.title("Flash Card")
flash_card_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = flash_card_window.after(3000, func=flip_card)

card_canvas = Canvas(width=800, height=526, highlightthickness=0)
card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
bg_image = card_canvas.create_image(400, 273, image=card_image_front)
card_canvas.config(bg=BACKGROUND_COLOR)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))
card_canvas.grid(row=0, column=0, columnspan=2)
next_card()

unknownword_image = PhotoImage(file="images/wrong.png")
unknownword_button = Button(image=unknownword_image, highlightthickness=0, command=next_card)
unknownword_button.config(bg=BACKGROUND_COLOR)
unknownword_button.grid(row=1, column=0)

rightword_image = PhotoImage(file="images/right.png")
rightword_button = Button(image=rightword_image, highlightthickness=0, command=is_known)
rightword_button.config(bg=BACKGROUND_COLOR)
rightword_button.grid(row=1, column=1)


flash_card_window.mainloop()