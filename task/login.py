import json 
import re 
import os
import getpass


USER_FILE="users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            content = file.read().strip()  
            if not content:  
                return []
            return json.loads(content)  
    return []



def save_user(users):
    with open (USER_FILE,"w") as file:
        json.dump(users,file,indent=4)


def valid_phone_num(phone):
    return re.match(r"^01[0-2,5]\d{8}$",phone) is not None

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def register():
    users = load_users()

    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")

    email = input("Enter email: ")

    if not is_valid_email(email):
        print("❌ Invalid email format! Please enter a valid email.")
        return
    
    if any(user["email"] == email for user in users):
        print("❌ Email already exists!")
        return
    
    password = getpass.getpass("Enter password: ")
    confirm_pass = getpass.getpass("Enter password again: ")

    if password != confirm_pass:
        print("❌ Passwords do not match!")
        return
    
    phone = input("Enter phone number: ")
    if not valid_phone_num(phone):
        print("❌ Phone number does not match Egyptian phone format!")
        return

    user = {
        "f_name": f_name,
        "l_name": l_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_user(users)
    print("✅ Registration successful!")

def login():
    users = load_users()

    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("✅ Welcome", user["f_name"])
            return user

    print("❌ Invalid email or password!")
    return None





def logout(user_email):
    users = load_users()
    users = [user for user in users if user["email"] != user_email]
    save_user(users)
    print("🔴 Logged out and account deleted successfully!")