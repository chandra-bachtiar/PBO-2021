import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Barang import Barang

qtcreator_file  = "barang.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowBarang(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.btnCari.clicked.connect(self.search_data) 
        self.btnSimpan.clicked.connect(self.save_data) 
        self.txtKodeBarang.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=False   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            barang = Barang()
            result = barang.getAllData()

            self.gridBarang.setHorizontalHeaderLabels(['ID', 'KodeBarang', 'NamaBarang', 'Merk', 'Harga'])
            self.gridBarang.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.gridBarang.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridBarang.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kodebarang=self.txtKodeBarang.text()           
            barang = Barang()
            # search process
            result = barang.getByKodeBarang(kodebarang)           
            a = barang.affected
            if(a!=0):
                print(barang.harga)
                self.txtNamaBarang.setText(barang.namabarang.strip())
                self.txtMerk.setText(barang.merk.strip())
                self.txtHarga.setValue(int(barang.harga))
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNamaBarang.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            barang = Barang()
            kodebarang=self.txtKodeBarang.text()
            namabarang=self.txtNamaBarang.text()
            merk=self.txtMerk.text()
            harga=self.txtHarga.text()
            
            if(self.edit_mode==False):   
                barang.kodebarang = kodebarang
                barang.namabarang = namabarang
                barang.merk = merk
                barang.harga = harga
                a = barang.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Barang Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Barang Gagal Tersimpan")
                
                self.clear_entry()
                self.select_data()
            elif(self.edit_mode==True):
                barang.kodebarang = kodebarang
                barang.namabarang = namabarang
                barang.merk = merk
                barang.harga = harga
                a = barang.updateByKodeBarang(kodebarang)
                if(a>0):
                    self.messagebox("SUKSES", "Data Barang Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Barang Gagal Diperbarui")
                
                self.clear_entry()
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            barang = Barang()
            kodebarang=self.txtKodeBarang.text()
                       
            if(self.edit_mode==True):
                a = barang.deleteByKodeBarang(kodebarang)
                if(a>0):
                    self.messagebox("SUKSES", "Data Barang Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Barang Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtKodeBarang.setText("")
        self.txtNamaBarang.setText("")
        self.txtMerk.setText("")
        self.txtHarga.setValue(0)
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
    window = WindowBarang()
    window.show()
    window.select_data()
    sys.exit(app.exec_())