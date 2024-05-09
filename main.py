from tkinter import messagebox
def write_to_file(value):
    with open("myfile.txt", "a") as f:  # Use "a" for append mode
        f.write(value + "\n")  # Add a newline character after each value
        input_website.delete(0,END)
        input_email.delete(0,END)
        input_password.delete(0,END)



def save(website, email, password):
    website_value = website.get()
    email_value = email.get()
    password_value = password.get()

    if not (email_value and password_value and website_value):
        # Email, password, or website field is empty, show an error message
        messagebox.showerror("Error", "Please fill in all fields.")
        return False
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detail entered : \n Email: {email_value} \nPassword: {password_value}")
        if is_ok:
            # Here you can save the values to a file or perform any other actions you want
            write_to_file(f"Website: {website_value} | Email: {email_value} |Password: {password_value}\n")

#Generate Random Password.

import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_password_button_click():
    random_password = generate_random_password()
    input_password.delete(0, END)  # Clear any existing text
    input_password.insert(0, random_password)


from tkinter import *

window = Tk()
window.title("Password Manager:")
window.config(padx=80, pady=100)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

my_label = Label(text="Website", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)

input_website = Entry(width=40)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

email = Label(text="Email/Username", font=("Arial", 12, "bold"))
email.grid(column=0, row=2)

input_email = Entry(width=40)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "shiwanshu785@gmail.com")

password = Label(text="Password", font=("Arial", 12, "bold"))
password.grid(column=0, row=3)

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password" , command=on_generate_password_button_click)
generate_password_button.grid(row=3, column=2)


def on_add_button_click():
    save(input_website, input_email, input_password)


add_button = Button(text="Add", width=36, command=on_add_button_click)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
