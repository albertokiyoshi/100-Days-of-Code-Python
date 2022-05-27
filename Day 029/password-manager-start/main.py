from tkinter import messagebox
from tkinter import *
from random import choice, shuffle, randint

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)

    lower_letter = [choice(lower_letters) for _ in range(randint(4, 5))]
    upper_letter = [choice(upper_letters) for _ in range(randint(4, 5))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = lower_letter + upper_letter + number + symbol
    shuffle(password_list)

    new_password = "".join(password_list)

    password_entry.insert(0, new_password)
    window.clipboard_clear()
    window.clipboard_append(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        save_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                                f"\nPassword: {password} \nIs it ok to save?")

        if save_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=30)
username_entry.grid(column=1, row=2)
username_entry.insert(0, "example@example.com")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password", command=password_gen)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=25, command=save)
add_button.grid(column=1, row=4)

window.mainloop()
