# Contact Manager

### Description
Contact Manager is a Python-based application designed to help users manage their contacts. It provides functionalities to add, edit, and delete contact information. The application uses a SQLite database to store contact details and features a graphical user interface (GUI) built with PyQt6.

### Features
- **Add Contacts**: Add new contacts with name, phone number, and email.
- **Edit Contacts**: Modify existing contact details.
- **Delete Contacts**: Remove contacts from the database.
- **Search and Display**: Search contacts and display them in a user-friendly table format.

### Installation
1. Clone the repository:
```
   git clone https://github.com/yourusername/contact-manager.git
   cd contact-manager
```

### Create a virtual environment:
```
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install the required dependencies:
```
pip install -r requirements.txt
```

### Usage
Run the application:
```
python project.py
```
Use the interface to add, edit, delete, and view contacts.

### Testing
The project includes unit tests to ensure the functionality of the contact management features. To run the tests:
```
pytest
```

### Requirements
- Python 3.8+
- PyQt6
- SQLite

### Files
    project.py: Main application file containing the GUI and core functionality.
    database.py: Module for database operations.
    test_project.py: Unit tests for the application.
    requirements.txt: List of dependencies.

### requirements.txt
Make sure this file includes all necessary dependencies for your project:
- PyQt6
- pytest

**Video Demo:**  https://www.youtube.com/watch?v=uEtOb838GlI
