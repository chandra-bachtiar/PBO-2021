import sys
from PyQt5 import QtCore, QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from formMahasiswa import WindowMahasiswa
from formDosen import WindowDosen
from formMatakuliah import WindowMatakuliah
from formKRS import WindowKRS

qtcreator_file  = "dashboard.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowDashboard(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.app_exit)
        self.actionMahasiswa.triggered.connect(self.ke_mahasiswa)
        self.actionDosen.triggered.connect(self.ke_dosen)
        self.actionMK.triggered.connect(self.ke_matakuliah)
        self.actionKRS.triggered.connect(self.ke_krs)     

    def app_exit(self):
        sys.exit()
    
    def ke_mahasiswa(self):
        self.window = WindowMahasiswa()
        self.window.show()

    def ke_dosen(self):
        self.window = WindowDosen()
        self.window.show()

    def ke_matakuliah(self):
        self.window = WindowMatakuliah()
        self.window.show()

    def ke_krs(self):
        self.window = WindowKRS()
        self.window.show()  

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboard()
    winMahasiswa = WindowMahasiswa()
    # winmatakuliah = WindowMatakuliah()
    window.showFullScreen()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboard()
    winMahasiswa = WindowMahasiswa()
    # winmatakuliah = WindowMatakuliah() 