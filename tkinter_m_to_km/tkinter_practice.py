from tkinter import *


# Button
def button_clicked():
    print("I got clicked!")
    my_label.config(text="I got clicked!")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.config(text="New Text", padx=100, pady=100)
my_label.grid(row=0, column=0)

# Button
button = Button(text="Click here", command=button_clicked)
button.grid(row=1, column=1)

# New Button
button = Button(text="New Button", command=button_clicked)
button.grid(row=0, column=2)

# Entry
input_ = Entry(width=10)
print(input_.get())
input_.grid(row=2, column=3)


window.mainloop()
