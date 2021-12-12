from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from decimal import Decimal
import sys
import re


qtcreator_file = "konversi.ui"
UI_GantiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class konversiSuhu(QtWidgets.QMainWindow,UI_GantiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_GantiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btn_konversi.clicked.connect(self.konversi)


    def konversi(self):
        celcius = int(self.txt_celcius.text());
        #Rumus Celcius -> Fahrenheit = ($celcius × 9/5) + 32 = fahreinheit °F
        #rumus Celcius -> Kelvin = 35 °C + 273,15 = 308,15 K
        fahrenheit = (celcius * (9/5)) + 32
        kelvin = celcius + 273.15
        self.txt_fahrenheit.setText(str(fahrenheit) + ' Derajat')
        self.txt_kelvin.setText(str(kelvin) + ' Derajat')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    suhuKonversi = konversiSuhu()
    suhuKonversi.show()
    sys.exit(app.exec_())