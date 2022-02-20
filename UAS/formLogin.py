import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Dashboard import WindowDashboard
# from DashboardOperator import WindowDashboardOperator
from User import User as Login

qtcreator_file  = "login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowLogin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnSubmit.clicked.connect(self.app_login)

    def app_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        valid = usr.Validasi(username,password)
        role = usr.rolename.strip() 
        if(valid==True):
            window.hide()
            self.messagebox("Info","Login Berhasil")
            windashboard.showFullScreen()
        else: # login gagal
            self.messagebox("Info","Maaf login gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin() 
    windashboard = WindowDashboard() 
    window.show()
    usr = Login()
    sys.exit(app.exec_())