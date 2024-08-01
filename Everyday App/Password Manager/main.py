from tkinter import *
from tkinter import messagebox
import json
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genPassword():
    """
    Generate a random password with a mix of letters, symbols, and numbers.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random password with letters, symbols, and numbers
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    # Join list into a string
    password = "".join(password_list)
    password_entry.insert(0, password)  # Insert the generated password into the entry field
    pyperclip.copy(password)  # Copy the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Save the website, email, and password data to a JSON file.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if website and password fields are not empty
    if len(website.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure your website and password field is not empty.")
    else:
        # Confirm details before saving
        isOK = messagebox.askyesno(title=website, message=f"These are the details entered: \n Website: {website} \n Email: {email} \n Password: {password} \n Is it ok to save?")
        if isOK:
            answer = {website: {"email": email, "password": password}}

            # Try to read existing data, otherwise create a new file
            try:
                with open(file="Everyday App/Password Manager/password.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="Everyday App/Password Manager/password.json", mode="w") as file:
                    json.dump(answer, file, indent=4)
            else:
                data.update(answer)
                with open(file="Everyday App/Password Manager/password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search():
    """
    Search for the password details of a specific website.
    """
    website = website_entry.get()

    # Load the data from the JSON file
    try:
        with open(file="Everyday App/Password Manager/password.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # Show message with email and password if website exists
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"Sorry, we do not have data for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Everyday App/Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "xyz@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=genPassword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2)

window.mainloop()
