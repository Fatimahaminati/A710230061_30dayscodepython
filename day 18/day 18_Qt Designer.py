from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from hitung_pajak import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        # Hubungkan tombol hitung pajak dengan fungsi calculate_tax
        self.pushButton.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        try:
            # Ambil nilai harga dari QLineEdit
            price = float(self.lineEdit.text())
            
            # Ambil nilai pajak dari QComboBox
            tax_rate_str = self.comboBox.currentText()
            tax_rate = float(tax_rate_str.rstrip('%')) / 100
            
            # Hitung total harga beserta pajak
            total_price = price + (price * tax_rate)
            
            # Tampilkan hasilnya di QLabel
            self.label_4.setText(f"Total Harga beserta pajak: Rp {total_price:.2f}")
        except ValueError:
            # Tampilkan pesan kesalahan jika input tidak valid
            QMessageBox.warning(self, "Input Error", "Masukkan harga yang benar.")

if __name__ == '__main__':
    app = QApplication([])
    dialog = Dialog()
    dialog.show()
    app.exec_()