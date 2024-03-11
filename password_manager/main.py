from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
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
def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    mail_name_entry.delete(0, END)
    mail_name_entry.insert(0, string="username@email.com")


def save():
    website = website_entry.get()
    email = mail_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }

    is_empty = (len(website) == 0) or (len(password) == 0)

    if is_empty:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            clear_entries()
            messagebox.showinfo(title=f"{website}", message="Password added successfully!")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you've filled the Website field.")
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="No passwords", message=f"You have no saved passwords.")
    else:
        if website in data or website.title() in data or website.lower() in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        elif website == "":
            pass
        else:
            messagebox.showinfo(title="Password not found", message=f"{website} does not have a saved password. "                                                           
                                                                    f"Check the spelling of the website.")
    finally:
        clear_entries()


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
website_entry = Entry(width=22)
website_entry.focus()
website_entry.grid(row=1, column=1)

mail_name_entry = Entry(width=40)
mail_name_entry.insert(0, string="username@email.com")
mail_name_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, borderwidth=1, command=find_password)
search_button.grid(row=1, column=2)

password_button = Button(text="Generate Password", borderwidth=1, command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
