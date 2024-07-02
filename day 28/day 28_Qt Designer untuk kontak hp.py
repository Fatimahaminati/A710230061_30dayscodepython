import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from contact_form import Ui_MainWindow

class ContactApp(QMainWindow):
    def __init__(self):
        super(ContactApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.contacts = []  # List to store contact information

        self.ui.addButton.clicked.connect(self.add_contact)
        self.ui.editButton.clicked.connect(self.edit_contact)
        self.ui.deleteButton.clicked.connect(self.delete_contact)

    def add_contact(self):
        name, phone = self.get_contact_info()
        if name and phone:
            self.contacts.append((name, phone))
            self.update_table()
    
    def edit_contact(self):
        selected_row = self.ui.contactTable.currentRow()
        if selected_row >= 0:
            name, phone = self.contacts[selected_row]
            new_name, new_phone = self.get_contact_info(name, phone)
            if new_name and new_phone:
                self.contacts[selected_row] = (new_name, new_phone)
                self.update_table()
        else:
            QMessageBox.warning(self, "Warning", "No contact selected to edit.")
    
    def delete_contact(self):
        selected_row = self.ui.contactTable.currentRow()
        if selected_row >= 0:
            del self.contacts[selected_row]
            self.update_table()
        else:
            QMessageBox.warning(self, "Warning", "No contact selected to delete.")
    
    def get_contact_info(self, name="", phone=""):
        # This method will show a dialog to input contact info
        dialog = ContactDialog(name, phone, self)
        dialog.exec_()
        return dialog.get_name(), dialog.get_phone()

    def update_table(self):
        self.ui.contactTable.setRowCount(0)
        for contact in self.contacts:
            row_position = self.ui.contactTable.rowCount()
            self.ui.contactTable.insertRow(row_position)
            self.ui.contactTable.setItem(row_position, 0, QTableWidgetItem(contact[0]))
            self.ui.contactTable.setItem(row_position, 1, QTableWidgetItem(contact[1]))

class ContactDialog(QMessageBox):
    def __init__(self, name="", phone="", parent=None):
        super(ContactDialog, self).__init__(parent)
        self.setWindowTitle("Contact Information")
        self.name_input = QLineEdit(name)
        self.phone_input = QLineEdit(phone)
        self.phone_input.setValidator(QIntValidator())
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(self.phone_input)
        self.setLayout(layout)
        self.addButton("OK", QMessageBox.AcceptRole)
        self.addButton("Cancel", QMessageBox.RejectRole)

    def get_name(self):
        return self.name_input.text()

    def get_phone(self):
        return self.phone_input.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactApp()
    window.show()
    sys.exit(app.exec_())
