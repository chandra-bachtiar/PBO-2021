import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from matakuliah import Matakuliah


qtcreator_file  = "matakuliah.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowMatakuliah(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKode.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode = False
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            mk = Matakuliah()

            # Get all 
            result = mk.getAllData()

            self.gridMatakuliah.setHorizontalHeaderLabels(['ID', 'Kode MK', 'Nama MK', 'sks', 'Prodi'])
            self.gridMatakuliah.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridMatakuliah.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridMatakuliah.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode=self.txtKode.text()           
            mk = Matakuliah()
            # search process
            result = mk.getByKODE(kode)           
            a = mk.affected
            if(a!=0):
                self.txtNama.setText(mk.namamk.strip())
                self.txtSKS.setText(str(mk.sks).strip())
                self.cboProdi.setCurrentText(mk.kode_prodi.strip())
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
            mk = Matakuliah()
            kodemk=self.txtKode.text()
            namamk=self.txtNama.text()
            sks=self.txtSKS.text()
            kode_prodi=self.cboProdi.currentText()
            
            if(self.edit_mode==False):   
                mk.kodemk = kodemk
                mk.namamk = namamk
                mk.sks = sks
                mk.kode_prodi = kode_prodi
                a = mk.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Tersimpan")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mk.namamk = namamk
                mk.sks = sks
                mk.kode_prodi = kode_prodi
                a = mk.updateByKODE(kodemk)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Diperbarui")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            mk = Matakuliah()
            kode=self.txtKode.text()
                       
            if(self.edit_mode==True):
                a = mk.deleteByKODE(kode)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtKode.setText("")
        self.txtNama.setText("")
        self.txtSKS.setText("")
        self.cboProdi.setCurrentText("")
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
    window = WindowMatakuliah()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowMatakuliah()