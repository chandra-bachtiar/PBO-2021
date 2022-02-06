import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Supplier import Supplier

qtcreator_file  = "Supplier.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowSupplier(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.btnCari.clicked.connect(self.search_data) 
        self.btnSimpan.clicked.connect(self.save_data) 
        self.txtKodeSupplier.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=False   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            supplier = Supplier()
            result = supplier.getAllData()

            self.gridSupplier.setHorizontalHeaderLabels(['ID', 'KodeSupplier', 'NamaSupplier', 'KontakPerson', 'Telp'])
            self.gridSupplier.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.gridSupplier.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridSupplier.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kodesupplier=self.txtKodeSupplier.text()           
            supplier = Supplier()
            # search process
            result = supplier.getByKodeSupplier(kodesupplier)           
            a = supplier.affected
            if(a!=0):
                self.txtNamaSupplier.setText(supplier.namasupplier.strip())
                self.txtCP.setText(supplier.cp.strip())
                self.txtTelp.setText(supplier.telp.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNamaSupplier.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            supplier = Supplier()
            kodesupplier=self.txtKodeSupplier.text()
            namasupplier=self.txtNamaSupplier.text()
            kontakperson=self.txtCP.text()
            telpon=self.txtTelp.text()
            
            if(self.edit_mode==False):   
                supplier.kodesupplier = kodesupplier
                supplier.namasupplier = namasupplier
                supplier.cp = kontakperson
                supplier.telp = telpon
                a = supplier.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Supplier Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Supplier Gagal Tersimpan")
                
                self.clear_entry()
                self.select_data()
            elif(self.edit_mode==True):
                supplier.kodesupplier = kodesupplier
                supplier.namasupplier = namasupplier
                supplier.cp = kontakperson
                supplier.telp = telpon
                a = supplier.updateByKodeSupplier(kodesupplier)
                if(a>0):
                    self.messagebox("SUKSES", "Data Supplier Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Supplier Gagal Diperbarui")
                
                self.clear_entry()
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            supplier = Supplier()
            kodesupplier=self.txtKodeSupplier.text()
                       
            if(self.edit_mode==True):
                a = supplier.deleteByKodeSupplier(kodesupplier)
                if(a>0):
                    self.messagebox("SUKSES", "Data Supplier Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Supplier Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtKodeSupplier.setText("")
        self.txtNamaSupplier.setText("")
        self.txtCP.setText("")
        self.txtTelp.setText("")
        self.btnSimpan.setText("Simpan")
        self.edit_mode=False
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowSupplier()
    window.show()
    window.select_data()
    sys.exit(app.exec_())