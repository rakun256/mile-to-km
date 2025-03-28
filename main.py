from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Milden Kilometre Çevirici")
window.config(bg="pink", padx=50, pady=50)

miles_input = Entry(width=7, bg="white", fg="purple", font=("Arial", 20))
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", bg="pink", fg="white", font=("Arial", 20))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", bg="pink", fg="white", font=("Arial", 20))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0",bg="pink", fg="white", font=("Arial", 20))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", bg="pink", fg="white", font=("Arial", 20))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", bg="pink", fg="white", command=miles_to_km, font=("Arial", 20))
calculate_button.grid(column=1, row=2)

window.mainloop()