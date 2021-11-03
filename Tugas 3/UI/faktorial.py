from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys
import os

qtcreator_file = "faktorial.ui"
formWindow,QtBaseClass = uic.loadUiType(qtcreator_file)

class faktorial(QtWidgets.QMainWindow,formWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        formWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.inputValue.textChanged.connect(self.hitungFaktorial)


    def hitungFaktorial(self):
        Nvalue = int(self.inputValue.text())
        hasil  = 1
        if(Nvalue == ''):
            self.outputValue.setText("Masukan Nilai n")
        else:
            for i in range(1, Nvalue + 1):
                hasil *= i
            self.outputValue.setText(str(hasil))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    faktorialProgram = faktorial()
    faktorialProgram.show()
    sys.exit(app.exec_())