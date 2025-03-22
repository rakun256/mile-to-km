import tkinter as tk

window = tk.Tk()
window.title("Simple GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tk.Label(text=f"Hello, World! \n Enter Your Name: ", font=("Arial", 20, "normal"))
my_label.pack()

#Button
def button_clicked():
    print("Button was clicked")

my_button = tk.Button(text="Click Me")
my_button.pack()


#Many Positional Arguments
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1,2,3,4,5,6,7,8,9))

#Many Keywords Arguments
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

window.mainloop()