from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(7, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = mail_name_entry.get()
    password = password_entry.get()

    is_empty = (len(website) == 0) or (len(password) == 0)

    if is_empty:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it OK to save?")
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            pass


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=50)

# Canvas
canvas = Canvas(width=240, height=220)
lock = PhotoImage(file="logo.png")
canvas.create_image(120, 110, image=lock)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

mail_name_label = Label(text="Email/Username:")
mail_name_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

mail_name_entry = Entry(width=40)
mail_name_entry.insert(0, string="username@email.com")
mail_name_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", borderwidth=1, command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
