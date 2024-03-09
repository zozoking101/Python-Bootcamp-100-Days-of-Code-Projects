from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label = "Timer"
    title_label.config(text="Timer")
    # reset check_marks
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Reps of the Pomodoro Technique
    # 1st 🍅 25min Work
    #     5min Break 🍅
    # 3rd 🍅 25min Work
    #     5min Break 🍅
    # 5th 🍅 25min Work
    #     5min Break 🍅
    # 7th 🍅 25min Work
    #     20min Break 🍅
    # if it's the 1st/3rd/5th/7th rep:
    if reps in [1, 3, 5, 7]:
        title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
        count_down(work_sec)
    # if it's the 8th rep:
    elif reps == 8:
        title_label.config(text="Break", fg=RED, font=(FONT_NAME, 50), bg=YELLOW)
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th rep:
    elif reps in [2, 4, 6]:
        title_label.config(text="Break", fg=PINK, font=(FONT_NAME, 50), bg=YELLOW)
        count_down(short_break_sec)
    else:
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # "00:00"
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        text = ""
        for _ in range(reps//2):
            text += "✔"
        check_mark.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row=0, column=1)

# Start
start_button = Button(text="Start", width=7, fg=RED, bg=GREEN, borderwidth=0, highlightthickness=0, font=10,
                      command=start_timer)
start_button.grid(row=2, column=0)

# Reset
reset_button = Button(text="Reset", width=7, fg=RED, bg=GREEN, borderwidth=0, highlightthickness=0, font=10,
                      command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark
check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=30)
check_mark.grid(row=3, column=1)

window.mainloop()
