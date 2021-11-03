from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys


qtcreator_file = "replaceKata.ui"
UI_ReplaceWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class myReplaceWindows(QtWidgets.QMainWindow,UI_ReplaceWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_ReplaceWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnOk.clicked.connect(self.GantiKata)


    def GantiKata(self):
        kalimat = self.txtKalimat.text()
        cari = self.txtFind.text()
        ganti = self.txtReplace.text()
        if(kalimat == '' or cari == '' or ganti == ''):
            self.txtResult.setText("Error: Terdapat Kolom Kosong!")
        else:
            self.txtResult.setText(kalimat.replace(cari,ganti))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gantiKata = myReplaceWindows()
    gantiKata.show()
    sys.exit(app.exec_())