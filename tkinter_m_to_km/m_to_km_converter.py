from tkinter import *


# Button
def m_to_km():
    calculated = float(entry.get()) * 1.60934
    result.config(text=f"{calculated:.1f}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Label
label = Label()
label.config(text="is equal to")
label.grid(row=1, column=0, padx=5, pady=5)

# Entry
entry = Entry()
entry.config(width=7)
entry.grid(row=0, column=1)

# Label
miles = Label()
miles.config(text="Miles")
miles.grid(row=0, column=2, padx=5, pady=5)

# Label
result = Label()
result.config(text="0")
result.grid(row=1, column=1, padx=5, pady=5)

# Label
km = Label()
km.config(text="Km")
km.grid(row=1, column=2, padx=5, pady=5)

# Calculate calls m_to_km()
calculate = Button()
calculate.config(text="Calculate", width=6, padx=5, pady=5, command=m_to_km)
calculate.grid(row=2, column=1)


window.mainloop()
