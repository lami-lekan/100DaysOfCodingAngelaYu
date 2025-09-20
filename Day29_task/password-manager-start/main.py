from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)

password_list = []
rand_letters = [password_list.append(random.choice(letters)) for letter in range(nr_letters)]
rand_numbers = [password_list.append(random.choice(numbers)) for letter in range(nr_numbers)]
rand_symbols = [password_list.append(random.choice(symbols)) for letter in range(nr_symbols)]

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char


def generate_password():
    password_entry.insert(0, password)
    copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password(website, email, password):
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(message="Sorry, entry can't be empty!", title="Oops!")
    else:
        choice = messagebox.askyesnocancel(title="Save Password", message="Are you sure you want to save this?")
        if choice == True:
                try:
                    with open("password_manager.json", "r") as pass_details:
                        update_data = json.load(pass_details)
                except FileNotFoundError:
                    with open("password_manager.json", "w") as pass_details:
                        json.dump(new_data, pass_details, indent=4)          
                else:
                    update_data.update(new_data)
                    with open("password_manager.json", "w") as pass_details:
                        json.dump(update_data, pass_details, indent=4)          

def del_entry(entry1, entry2):
    entry1.delete(0, END)
    entry2.delete(0, END)

def search_func(website_entry):
    try:
        with open("password_manager.json", "r") as password_detail:
            new_password_details = json.load(password_detail)
    except FileNotFoundError:
        pass
    else:
        try:
            messagebox.showinfo(message=f'Email: {new_password_details[website_entry.get()]["email"]} \nPassword: {new_password_details[website_entry.get()]["password"]}', title=website_entry.get())
        except KeyError:
            messagebox.showinfo(message=f"No details found for '{website_entry.get()}'", title="Sorry!")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1 , column=0)
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="          Search          ", command= lambda: search_func(website_entry))
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2 , column=0)
email_entry = Entry(width=51)
email_entry.insert(0, "Olagbajuisrael11@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3 , column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command= generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=lambda: [add_password(website_entry.get(), email_entry.get(), password_entry.get()), del_entry(website_entry, password_entry)])
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()