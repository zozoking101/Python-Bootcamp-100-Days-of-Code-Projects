from tkinter import *
import pandas as pd
import random


# -------------------------- CONSTANTS ------------------------
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
QUESTION_SEC = 3

# -------------------------- SCORING --------------------------
try:
    data = pd.read_csv("./data/words_left_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient='records')
    current_card = {}
else:
    to_learn = data.to_dict(orient='records')
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(QUESTION_MSEC, func=flip_card)


# -------------------------- FLIP CARD -------------------------
def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=card_back)
 
        
# -------------------------- CARD KNOWN -------------------------
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
    
    
# -------------------------- UI SETUP -------------------------

# Window
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

QUESTION_MSEC = QUESTION_SEC * 1000

flip_timer = window.after(QUESTION_MSEC, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
background = canvas.create_image(400, 262, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="./images/card_back.png")

title = canvas.create_text(400, 100, text="Title", fill="black", font=(FONT_NAME, 30, "italic"))
word = canvas.create_text(400, 262, text="word", fill="black", font=(FONT_NAME, 45, "bold"))

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=0)

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=1)

# -------------------------- APP ---------------------------

next_card()


window.mainloop()
