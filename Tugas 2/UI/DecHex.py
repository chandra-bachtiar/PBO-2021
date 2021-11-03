from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from decimal import Decimal
import sys
import re


qtcreator_file = "DecHex.ui"
UI_GantiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class myGantiWindows(QtWidgets.QMainWindow,UI_GantiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_GantiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        r = re.compile(r"^\d*[.,]?\d*$")
        if r.match(self.angkaDecimal.text()):
            self.angkaDecimal.textChanged.connect(self.ganti)


    def ganti(self):
        if(self.angkaDecimal.text() != ''):
            vDecimal = str(hex(int(self.angkaDecimal.text()))).replace('0x','').upper()
            self.angkaHexa.setText(vDecimal)
        else:
            self.angkaHexa.setText("Bukan Angka!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gantiHexa = myGantiWindows()
    gantiHexa.show()
    sys.exit(app.exec_())