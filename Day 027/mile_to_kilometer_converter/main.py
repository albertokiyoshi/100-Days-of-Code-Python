import tkinter
FONT = ("Arial", 16, "normal")


def calculate():
    label_conversion.config(text=float(miles_input.get()) * 1.609)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

value_km = 0

label_miles = tkinter.Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)
label_km = tkinter.Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)
label_equal = tkinter.Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row=1)
label_conversion = tkinter.Label(text=value_km, font=FONT)
label_conversion.grid(column=1, row=1)

miles_input = tkinter.Entry(width=10)
miles_input.insert("0")
miles_input.grid(column=1, row=0)

button_calculate = tkinter.Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)

window.mainloop()
