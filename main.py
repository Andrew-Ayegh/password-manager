from tkinter import messagebox
from tkinter import *
import random
import json
YELLOW = "#f7f5dd"

FONT = ("courier", 10) 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''Generates a random password using letters, numbers and special characters'''
    letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '|', '/', '?', '>', '<',  ';', ':']
# __________Clearing the entry field before generating password
    password_entry.delete(0, END)
    letter_list =[random.choice(letters) for _ in range(random.randint(8, 10))]
    number_list =[random.choice(numbers) for _ in range(random.randint(6,8))]
    special_characters_list =[random.choice(special_characters) for _ in range(random.randint(4,6))]

    password = letter_list + number_list + special_characters_list
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)

# ----------------------------CLEAR ALL SAVED DATA---------------------------#
def clear():
    '''Clears all saved Websites, Emails and Passwords'''
    clear_all = messagebox.askokcancel(title="Clear Data", message='Do you want to clear all saved information?')
    blank = {}
    if clear_all:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            with open("data.json", "w") as data:
                json.dump(blank, data)

# -------------------------CHECK SAVED WEBSITE INFORMATION-------------------------#
def search():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            email = data[website_entry.get()]["Email"]
            password = data[website_entry.get()]["Password"]
        except KeyError:
            messagebox.showerror(title="Error", message="No data on this website")
        else:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {email}\nPassword: {password}")
            website_entry.focus()
            

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    '''Saves the website, email & password entry and clears entry fields'''
    
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()


#______________checking for valid password, email and website 
    if len(website.strip()) > 1:
        if len(email.strip()) >1:
            if len(password.strip()) > 1:
                
                new_data = {
                    website:{
                        "Email":email, 
                        "Password":password
                    } 
                }
# _______________Running exceptions to catch file not found
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file ,indent=4)
                
                else:
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file,indent=4)
                finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    website_entry.focus()
            else:
                messagebox.showerror(title="Missing Field", message="Password can not be blank")
                password_entry.focus()
        else:
            messagebox.showerror(title="Missing Field", message="Email can not be blank")
            email_entry.focus()
    else:
        messagebox.showerror(title="Missing Field", message="Website can not be blank")
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

#__________creating a Display window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=YELLOW)

image = PhotoImage(file="logo.png")

canva = Canvas(width= 200, height=200, bg=YELLOW ,highlightthickness=0)
canva.create_image(100, 100, image=image)
canva.grid(row=0, column = 1)

#__________Creating Labels
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:', bg= YELLOW)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(row=3, column=0)

#__________Creating entries
website_entry= Entry(width=38)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width= 54)
email_entry.insert(0, "Terna@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=38)
password_entry.grid(row=3, column=1)

#__________Creating buttons
generate_button = Button(text="Geneate Password", font=("ariel", 7), command=generate_password, width=14)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add",width=38,font=("ariel", 8), command=save_entry)
add_button.grid(row=4, column=1)
clear_data = Button(text="Clear Data", font=("ariel", 8), width=14, command=clear)
clear_data.grid(row=4, column=2)
search_button = Button(text="Search",font=("ariel", 7), width=14, command=search)
search_button.grid(row=1 ,column=2)

window.mainloop()