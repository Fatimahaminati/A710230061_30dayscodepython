from PyQt5 import QtWidgets, QtCore
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("quote")
        Dialog.resize(400, 300)
        
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(100, 50, 200, 30))
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Semangat UAS!")

        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(100, 150, 200, 30))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Keluar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("quote", "quote"))
        self.pushButton.setText(_translate("quote", "Semangat UAS!"))
        self.exitButton.setText(_translate("quote", "Keluar"))
        self.nameLineEdit.setPlaceholderText(_translate("quote", "Masukkan Nama"))

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_message)
        self.exitButton.clicked.connect(self.close)

    def show_message(self):
        name = self.nameLineEdit.text()
        QtWidgets.QMessageBox.information(self, "Semangat UAS!", f"Semangat UAS, {name}!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())