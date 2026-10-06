from operations import (create_contact, view_contacts, update_contact,
                        delete_contact, search_contacts)

def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contacts")
    print("6. Exit")

def main():
    actions = {
        "1": create_contact,
        "2": view_contacts,
        "3": update_contact,
        "4": delete_contact,
        "5": search_contacts,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print("Invalid choice. Enter 1-6.")

if __name__ == "__main__":
    main()