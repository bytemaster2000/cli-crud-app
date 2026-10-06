# Contact Book CLI

A command-line application built with Python that lets users manage contacts using full CRUD operations (Create, Read, Update, Delete), with search and persistent storage.

## Features

- Menu-driven interface
- Add, view, update and delete contacts
- Search contacts by name
- Data saved in a JSON file (persists after closing the program)
- Input validation for name, phone and email
- Exception handling so the program never crashes on bad input
- Modular code split across multiple files

## Project Structure

```
cli-crud-app/
├── main.py          # menu and program loop
├── storage.py       # loading and saving JSON data
├── operations.py    # create, read, update, delete, search
├── validators.py    # input validation
└── README.md
```

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

1. Clone the repository:

```bash
   git clone https://github.com/bytemaster2000/cli-crud-app.git
   cd cli-crud-app
```

2. Run the program:

```bash
   python main.py
```

## Example Usage

```
=== Contact Book ===
1. Add contact
2. View all contacts
3. Update contact
4. Delete contact
5. Search contacts
6. Exit
Choose an option: 1
Name: Raj Kumar
Phone: 9876543210
Email: raj@gmail.com
Contact added.
```

## What I Learned

- Building a menu-driven CLI in Python
- CRUD operations and data persistence with JSON
- Input validation and exception handling
- Organizing code into modules
- Using Git and GitHub

## Author

Lakshmi Priya