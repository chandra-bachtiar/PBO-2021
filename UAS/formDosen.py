import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from dosen import Dosen

qtcreator_file  = "dosen.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowDosen(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNIP.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode = False
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            dosen = Dosen()

            # Get all 
            result = dosen.getAllData()

            self.gridDosen.setHorizontalHeaderLabels(['ID', 'NIP', 'Nama', 'Email', 'Alamat'])
            self.gridDosen.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridDosen.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridDosen.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nip=self.txtNIP.text()           
            dosen = Dosen()
            # search process
            result = dosen.getByNIP(nip)           
            a = dosen.affected
            if(a!=0):
                self.txtNama.setText(dosen.nama.strip())
                self.txtAlamat.setText(dosen.alamat.strip())
                self.txtEmail.setText(dosen.email.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            dosen = Dosen()
            nip=self.txtNIP.text()
            nama=self.txtNama.text()
            alamat = self.txtAlamat.text()
            email = self.txtEmail.text()
            
            if(self.edit_mode==False):   
                dosen.nip = nip
                dosen.nama = nama
                dosen.alamat = alamat
                dosen.email = email
                a = dosen.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Tersimpan")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                dosen.nama = nama
                dosen.alamat = alamat
                dosen.email = email
                a = dosen.updateByNIP(nip)
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Diperbarui")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            dosen = Dosen()
            nip=self.txtNIP.text()
                       
            if(self.edit_mode==True):
                a = dosen.deleteByNIM(nip)
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtNIP.setText("")
        self.txtNama.setText("")
        self.txtAlamat.setText("")
        self.txtEmail.setText("")
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
    window = WindowDosen()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDosen()