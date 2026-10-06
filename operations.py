from storage import load_data, save_data
from validators import valid_name, valid_phone, valid_email

def get_valid_input(prompt, validator, error):
    while True:
        value = input(prompt).strip()
        if validator(value):
            return value
        print(f"Invalid: {error}")

def create_contact():
    data = load_data()
    contact = {
        "id": max((c["id"] for c in data), default=0) + 1,
        "name": get_valid_input("Name: ", valid_name, "min 2 characters"),
        "phone": get_valid_input("Phone: ", valid_phone, "7-15 digits only"),
        "email": get_valid_input("Email: ", valid_email, "e.g. a@b.com"),
    }
    data.append(contact)
    save_data(data)
    print("Contact added.")

def view_contacts():
    data = load_data()
    if not data:
        print("No contacts found.")
        return
    for c in data:
        print(f"[{c['id']}] {c['name']} | {c['phone']} | {c['email']}")

def update_contact():
    data = load_data()
    try:
        cid = int(input("Enter contact ID to update: "))
    except ValueError:
        print("ID must be a number.")
        return
    for c in data:
        if c["id"] == cid:
            c["name"] = get_valid_input(f"New name ({c['name']}): ", valid_name, "min 2 characters")
            c["phone"] = get_valid_input(f"New phone ({c['phone']}): ", valid_phone, "7-15 digits only")
            c["email"] = get_valid_input(f"New email ({c['email']}): ", valid_email, "e.g. a@b.com")
            save_data(data)
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    data = load_data()
    try:
        cid = int(input("Enter contact ID to delete: "))
    except ValueError:
        print("ID must be a number.")
        return
    new_data = [c for c in data if c["id"] != cid]
    if len(new_data) == len(data):
        print("Contact not found.")
    else:
        save_data(new_data)
        print("Contact deleted.")

def search_contacts():
    keyword = input("Search by name: ").strip().lower()
    results = [c for c in load_data() if keyword in c["name"].lower()]
    if not results:
        print("No matches.")
    for c in results:
        print(f"[{c['id']}] {c['name']} | {c['phone']} | {c['email']}")