import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QTableWidgetItem, QTableWidget, QMessageBox, QDialogButtonBox
from PyQt6.QtGui import QIcon
from database import Database

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 1000, 500)

        self.database = Database()
        self.setup_ui()
        self.load_contacts()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.contact_table = QTableWidget()
        self.contact_table.setColumnCount(4)  # Updated to include email column
        self.contact_table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])
        self.contact_table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.contact_table)

        btn_add = QPushButton("Add Contact")
        btn_add.setObjectName("addButton")  # Set object name for styling
        btn_add.clicked.connect(self.add_contact)
        btn_edit = QPushButton("Edit Contact")
        btn_edit.setObjectName("editButton")  # Set object name for styling
        btn_edit.clicked.connect(self.edit_contact)
        btn_delete = QPushButton("Delete Contact")
        btn_delete.setObjectName("deleteButton")  # Set object name for styling
        btn_delete.clicked.connect(self.delete_contact)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_edit)
        btn_layout.addWidget(btn_delete)
        self.layout.addLayout(btn_layout)

        self.contact_table.itemSelectionChanged.connect(self.update_buttons_state)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #fff;
                border: none;
            }

            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0;
                border: none;
                border-radius: 10px;
            }

            QTableWidget::item:selected {
                background-color: rgba(255, 255, 0, 1);
                color: #000
            }

            QTableWidget::item {
                background-color: rgba(255, 255, 0, .1);
            }

            QTableWidget::item:hover {
                background-color: rgba(255, 255, 0, .3);
            }

            QPushButton#addButton, QPushButton#editButton, QPushButton#deleteButton {
                padding: 8px 10px;
                border-radius: 10px;
                font-size: 20px;
            }

            QPushButton#addButton {
                background-color: transparent;
                border: 3px solid rgba(10, 10, 255, .6);
                color: #000;
            }

            QPushButton#editButton {
                background-color: transparent;
                color: #000;
                border: 3px solid rgba(10, 255, 10, .6);
            }

            QPushButton#deleteButton {
                background-color: transparent;
                color: #000;
                border: 3px solid rgba(255, 10, 10, .6);
            }

            QPushButton#addButton:hover {
                background-color: rgba(10, 10, 255, .1);
            }

            QPushButton#editButton:hover {
                background-color: rgba(10, 255, 10, .1);
            }

            QPushButton#deleteButton:hover {
                background-color: rgba(255, 10, 10, .1);
            }
            
            QPushButton#addButton:pressed {
                background-color: rgba(10, 10, 255, .6);
            }

            QPushButton#editButton:pressed {
                background-color: rgba(10, 255, 10, .6);
            }

            QPushButton#deleteButton:pressed {
                background-color: rgba(255, 10, 10, .6);
            }

            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #333;
            }

            QLineEdit {
                padding: 20px;
                border: none
                border-radius: 3px;
            }
        """)

    def load_contacts(self):
        contacts = self.database.fetch_contacts()
        self.contact_table.setRowCount(len(contacts))
        for row, contact in enumerate(contacts):
            for col, data in enumerate(contact):
                item = QTableWidgetItem(str(data))
                self.contact_table.setItem(row, col, item)

    def add_contact(self):
        dialog = ContactDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name = dialog.name_input.text()
            phone = dialog.phone_input.text()
            email = dialog.email_input.text()

            if name.strip() == "" or phone.strip() == "":
                QMessageBox.warning(self, "Validation Error", "Name and Phone fields are mandatory.")
                return

            if not self.database.insert_contact(name, phone, email):
                QMessageBox.warning(self, "Duplicate Entry", "This phone number already exists in the database.")
                return

            self.load_contacts()

    def edit_contact(self):
        selected_row = self.contact_table.currentRow()
        if selected_row != -1:
            contact_id = int(self.contact_table.item(selected_row, 0).text())
            name = self.contact_table.item(selected_row, 1).text()
            phone = self.contact_table.item(selected_row, 2).text()
            email = self.contact_table.item(selected_row, 3).text()

            dialog = ContactDialog(self)
            dialog.setWindowTitle("Edit Contact")
            dialog.name_input.setText(name)
            dialog.phone_input.setText(phone)
            dialog.email_input.setText(email)

            if dialog.exec() == QDialog.DialogCode.Accepted:
                new_name = dialog.name_input.text()
                new_phone = dialog.phone_input.text()
                new_email = dialog.email_input.text()

                if new_name.strip() == "" or new_phone.strip() == "":
                    QMessageBox.warning(self, "Validation Error", "Name and Phone fields are mandatory.")
                    return

                if not self.database.update_contact(contact_id, new_name, new_phone, new_email):
                    QMessageBox.warning(self, "Duplicate Entry", "This phone number already exists in the database.")
                    return

                self.load_contacts()

    def delete_contact(self):
        selected_row = self.contact_table.currentRow()
        if selected_row != -1:
            confirmation = QMessageBox.question(self, "Delete Contact", "Are you sure you want to delete this contact?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmation == QMessageBox.StandardButton.Yes:
                contact_id = int(self.contact_table.item(selected_row, 0).text())
                self.database.delete_contact(contact_id)
                self.load_contacts()

    def update_buttons_state(self):
        selected_row = self.contact_table.currentRow()
        btn_edit = self.layout.itemAt(1).itemAt(0).widget()  # Assuming edit button is the first in the layout
        btn_delete = self.layout.itemAt(1).itemAt(2).widget()  # Assuming delete button is the third in the layout

        if selected_row == -1:
            btn_edit.setEnabled(False)
            btn_delete.setEnabled(False)
        else:
            btn_edit.setEnabled(True)
            btn_delete.setEnabled(True)

class ContactDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Contact")
        self.setFixedSize(500, 300)  # Set fixed size for the dialog
        self.setModal(True)

        layout = QVBoxLayout(self)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                color: #000;
            }

            QLineEdit {
                font-size: 20px;
                padding: 10px;
                border: 1px solid rgba(10, 10, 255, .6);
                border-radius: 10px;
                height: 40px;
            }
        """)

def main():
    try:
        app = QApplication(sys.argv)
        manager = ContactManager()
        manager.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
