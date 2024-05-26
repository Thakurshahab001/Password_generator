from tkinter import messagebox, END, Tk, Canvas, PhotoImage, Label, Entry, Button
import json
import random
import string
#==================================function=======================================================
def write_to_file(value):
    with open("myfile.txt", "a") as f:  # Use "a" for append mode
        f.write(value + "\n")  # Add a newline character after each value
        input_website.delete(0, END)
        input_email.delete(0, END)
        input_password.delete(0, END)

def save(website, email, password):
    website_value = website.get()
    email_value = email.get()
    password_value = password.get()
    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value
        }
    }

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        write_to_file(website_value)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_password_button_click():
    random_password = generate_random_password()
    input_password.delete(0, END)  # Clear any existing text
    input_password.insert(0, random_password)

def on_add_button_click():
    save(input_website, input_email, input_password)

def find_password():
    website_value = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found")
    else:
        if website_value in data:
            email = data [ website_value ] [ "email" ]
            password = data [ website_value ] [ "password" ]
            messagebox.showinfo(title=website_value, message=f"Email :{email}\nPassword :{password}")
        else:
            messagebox.showerror(title="Error", message=f"No Detail For {website_value} exists.")

#=========================================UI Design=====================================================================
window = Tk()
window.title("Password Manager:")
window.config(padx=80, pady=100)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

my_label = Label(text="Website", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)

input_website = Entry(width=21)
input_website.grid(column=1, row=1)
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

search_button = Button(text="Search",command=find_password ,width=13)
search_button.grid(row=1 ,column=2)

generate_password_button = Button(text="Generate Password", command=on_generate_password_button_click)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=on_add_button_click)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
