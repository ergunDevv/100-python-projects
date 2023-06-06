from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_letters)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open(r"29-)password-manager-app\data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Python Password Manager")
window.config(pady=50, padx=50)
window.resizable(False, False)


# Canvas
new_canvas = Canvas(width=200, height=200,  highlightthickness=0)
logo_img = PhotoImage(file=r"29-)password-manager-app\logo.png")
new_canvas.create_image(100, 100, image=logo_img)
new_canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website: ", font="Arial 12")
email_label = Label(text="Email/Username: ",
                    font="Arial 12")
password_label = Label(text="Password: ", font="Arial 12")
website_label.grid(row=1, column=0, pady=(0, 10))
email_label.grid(row=2, column=0, pady=(0, 10))
password_label.grid(row=3, column=0, pady=(0, 10))

# Input
website_input = Entry(font="Arial 12")
website_input.grid(row=1, column=1, columnspan=2,
                   sticky="WE", ipady=5, pady=(0, 10))
website_input.focus()
email_input = Entry(font="Arial 12")
email_input.grid(row=2, column=1, columnspan=2,
                 sticky="EW", ipady=5, pady=(0, 10))
email_input.insert(0, "angela@gmail.com")
password_input = Entry(font="Arial 12")
password_input.grid(row=3, column=1, sticky="EW",
                    pady=(0, 10), ipady=5, padx=(0, 10))
# Buttons
gen_pwd_btn = Button(text="Generate password", command=generate_password,
                     font="Arial 10")
gen_pwd_btn.grid(row=3, column=2, sticky="we", pady=(0, 10), ipady=2)
add_button = Button(text="Add", font="Arial 10", width=60, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", ipady=2)

window.mainloop()
