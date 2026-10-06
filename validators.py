import re

def valid_name(name):
    return len(name.strip()) >= 2

def valid_phone(phone):
    return phone.isdigit() and 7 <= len(phone) <= 15

def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None