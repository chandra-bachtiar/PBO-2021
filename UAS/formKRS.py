import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
from dosen import Dosen
from matakuliah import Matakuliah
from mahasiswa import Mahasiswa
from krs import Krs

qtcreator_file  = "krs.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowKRS(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCariNomorBukti.clicked.connect(self.cari_krs)
        self.txtNomorBukti.returnPressed.connect(self.cari_krs) 
        self.btnCariNim.clicked.connect(self.cari_nim)
        self.btnCariNidn.clicked.connect(self.cari_nidn)
        self.btnCariMK1.clicked.connect(self.cari_mk1) 
        self.btnCariMK2.clicked.connect(self.cari_mk2) 
        self.btnCariMK3.clicked.connect(self.cari_mk3) 
        self.btnCariMK4.clicked.connect(self.cari_mk4) 
        self.btnCariMK5.clicked.connect(self.cari_mk5) 
        self.btnSimpan.clicked.connect(self.simpan) 
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=False

    def cari_mk1(self):
        try:
            mk = Matakuliah()
            kode = self.txtKodeMK1.text()
            mk.getByKODE(kode)
            a = mk.affected
            if(a!=0):
                self.txtNamaMK1.setText(mk.namamk.strip())                                              
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
    
    def cari_mk2(self):
        try:
            mk = Matakuliah()
            kode = self.txtKodeMK2.text()
            mk.getByKODE(kode)
            a = mk.affected
            if(a!=0):
                self.txtNamaMK2.setText(mk.namamk.strip())                                              
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_mk3(self):
        try:
            mk = Matakuliah()
            kode = self.txtKodeMK3.text()
            mk.getByKODE(kode)
            a = mk.affected
            if(a!=0):
                self.txtNamaMK3.setText(mk.namamk.strip())                                              
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_mk4(self):
        try:
            mk = Matakuliah()
            kode = self.txtKodeMK4.text()
            mk.getByKODE(kode)
            a = mk.affected
            if(a!=0):
                self.txtNamaMK4.setText(mk.namamk.strip())                                              
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_mk5(self):
        try:
            mk = Matakuliah()
            kode = self.txtKodeMK5.text()
            mk.getByKODE(kode)
            a = mk.affected
            if(a!=0):
                self.txtNamaMK5.setText(mk.namamk.strip())                                              
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    

    def cari_nim(self):
        try:           
            kode=self.txtNim.text()           
            mhs = Mahasiswa()
            result = mhs.getByNIM(kode)           
            a = mhs.affected
            
            if(a!=0):
                self.txtNamaMahasiswa.setText(mhs.nama.strip())
            else:
                self.messagebox("INFO", "Data Mahasiswa tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
    
    def cari_nidn(self):
        try:           
            kode=self.txtNidn.text()           
            dosen = Dosen()
            result = dosen.getByNIP(kode)           
            a = dosen.affected
            
            if(a!=0):
                self.txtNamaDosen.setText(dosen.nama.strip())
            else:
                self.messagebox("INFO", "Data Dosen tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_krs(self):
        try:           
            kode=self.txtNomorBukti.text()           
            krs = Krs()
            # search process
            result = krs.getByNOMOR_BUKTI(kode)           
            a = krs.affected            
            if(a!=0):
                self.edit_mode=True
                self.txtNim.setText(krs.nim.strip())
                self.txtNidn.setText(krs.nidn.strip())
                self.cari_nim()
                self.cari_nidn()
                self.txtTahunAkademik.setText(krs.tahun_akademik.strip())
                self.cboSemester.setCurrentText(krs.tipe_semester.strip())
                self.cboProdi.setCurrentText(krs.kode_prodi.strip())
                self.txtKodeMK1.setText(krs.kodemk_1)
                self.txtTanggal.setDate(QDate.fromString(krs.tanggal, "yyyy-MM-dd"))
                a=self.txtKodeMK1.text()
                if(a!=""):
                    self.cari_mk1()
                self.txtKodeMK2.setText(krs.kodemk_2)
                b = self.txtKodeMK2.text()
                if(b!=""):
                    self.cari_mk2()
                self.txtKodeMK3.setText(krs.kodemk_3)
                c = self.txtKodeMK3.text()
                if(c!=""):
                    self.cari_mk3()
                d = self.txtKodeMK4.text()
                if(d!=""):
                    self.cari_mk4()
                e = self.txtKodeMK5.text()
                if(e!=""):
                    self.cari_mk5()
            else:
                self.edit_mode=False
                self.messagebox("INFO", "Data KRS tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtNomorBukti.setText("")
        self.txtNim.setText("")
        self.txtNamaMahasiswa.setText("")
        self.txtNidn.setText("")
        self.txtNamaDosen.setText("")
        self.txtTahunAkademik.setText("")
        self.cboSemester.setCurrentText("")
        self.cboProdi.setCurrentText("")
        self.txtKodeMK1.setText("")
        self.txtKodeMK2.setText("")
        self.txtKodeMK3.setText("")
        self.txtKodeMK4.setText("")
        self.txtKodeMK5.setText("")
        self.txtNamaMK1.setText("")
        self.txtNamaMK2.setText("")
        self.txtNamaMK3.setText("")
        self.txtNamaMK4.setText("")
        self.txtNamaMK5.setText("")
        self.edit_mode = False

    def simpan(self):
        try:
            krs = Krs()
            NomorBukti = self.txtNomorBukti.text()
            Nim = self.txtNim.text()
            Nidn = self.txtNidn.text()
            tanggal = self.txtTanggal.date().toString("yyyy-MM-dd")
            tahun_akademik = self.txtTahunAkademik.text()
            kode_prodi = self.cboProdi.currentText()
            tipe_semster = self.cboSemester.currentText()
            kodemk1 = self.txtKodeMK1.text()
            kodemk2 = self.txtKodeMK2.text()
            kodemk3 = self.txtKodeMK3.text()
            kodemk4 = self.txtKodeMK4.text()
            kodemk5 = self.txtKodeMK5.text()
            if(self.edit_mode==False):
                krs.nomor_bukti = NomorBukti
                krs.tanggal = tanggal
                krs.nim = Nim
                krs.nidn = Nidn
                krs.tahun_akademik = tahun_akademik
                krs.tipe_semester = tipe_semster
                krs.kode_prodi = kode_prodi
                krs.kodemk_1 = kodemk1
                krs.kodemk_2 = kodemk2
                krs.kodemk_3 = kodemk3
                krs.kodemk_4 = kodemk4
                krs.kodemk_5 = kodemk5
                a = krs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Krs Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Krs Gagal Tersimpan")               
                self.clear_entry() 
            elif(self.edit_mode==True):
                krs.nomor_bukti = NomorBukti
                krs.tanggal = tanggal
                krs.nim = Nim
                krs.nidn = Nidn
                krs.tahun_akademik = tahun_akademik
                krs.kode_prodi = kode_prodi
                krs.kodemk_1 = kodemk1
                krs.kodemk_2 = kodemk2
                krs.kodemk_3 = kodemk3
                krs.kodemk_4 = kodemk4
                krs.kodemk_5 = kodemk5
                a = krs.updateByNOMOR_BUKTI(NomorBukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data KRS Berhasil Diubah")
                else:
                    self.messagebox("GAGAL", "Data KRS Gagal Diubah")   

                self.clear_entry() # Clear Entry Form
            else:
                self.messagebox("ERROR", "Terjadi kesalahan mode edit")
        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
    def delete_data(self):
        try:
            krs = Krs()
            NomorBukti=self.txtNomorBukti.text()
                       
            if(self.edit_mode==True):
                a = krs.deleteByNOMOR_BUKTI(NomorBukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data Krs Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Krs Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowKRS()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowKRS()