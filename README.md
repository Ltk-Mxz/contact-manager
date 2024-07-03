# Contact Manager

#### Video Demo: https://youtu.be/O_UyNfOfXkk

#### Description
  Contact Manager is a simple application built with Python and PyQt6 that allows users to manage their contacts. It utilizes SQLite for data storage.

#### Features
  - Add new contacts with name, phone number, and optional email.
  - Edit existing contacts.
  - Delete contacts.
  - View all contacts in a table view.

#### Installation
  1. Clone the repository:
  
  git clone https://github.com/Ltk-Mxz/contact-manager.git
  cd contact-manager
  
  2. Install dependencies:
  
  pip install -r requirements.txt
  
  3. Run the application:
  python project.py

#### Dependencies
  - PyQt6: Provides the GUI framework.
  - SQLite3: Embedded database for storing contacts.
  - PyTest: For Unit test.

#### Usage
  - Use the "Add Contact" button to add a new contact.
  - Select a contact from the table to edit or delete it.

  requirements.txt
  
  The requirements.txt file lists Python dependencies required for your project. You can generate it automatically using the following command in your virtual environment where you have installed your dependencies:
  
  pip freeze > requirements.txt
  
  Make sure your virtual environment is activated before running this command. It will generate a requirements.txt file that looks like this:

  PyQt6==6.7.0

  Ensure to replace PyQt6==6.7.0 with the specific versions of libraries you are actually using in your project, if necessary.
