import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)


def button_clicked():
    my_label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=4, row=3)
window.mainloop()
