
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(375, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameTop = QtWidgets.QFrame(self.centralwidget)
        self.frameTop.setGeometry(QtCore.QRect(20, 10, 340, 291))
        self.frameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTop.setObjectName("frameTop")
        self.label = QtWidgets.QLabel(self.frameTop)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 60))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.from_currency = QtWidgets.QComboBox(self.frameTop)
        self.from_currency.setGeometry(QtCore.QRect(10, 90, 101, 40))
        self.from_currency.setObjectName("from_currency")
        self.to_currency = QtWidgets.QComboBox(self.frameTop)
        self.to_currency.setGeometry(QtCore.QRect(10, 210, 101, 40))
        self.to_currency.setObjectName("to_currency")
        self.from_value = QtWidgets.QLineEdit(self.frameTop)
        self.from_value.setGeometry(QtCore.QRect(160, 90, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.from_value.setFont(font)
        self.from_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.from_value.setObjectName("from_value")
        self.from_value.setPlaceholderText("0")
        self.to_value = QtWidgets.QLineEdit(self.frameTop)
        self.to_value.setGeometry(QtCore.QRect(160, 210, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.to_value.setFont(font)
        self.to_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.to_value.setObjectName("to_value")
        self.to_value.setEnabled(False)
        self.to_value.setPlaceholderText("0")
        self.convert_btn = QtWidgets.QPushButton(self.frameTop, clicked = self.get_data)
        self.convert_btn.setGeometry(QtCore.QRect(10, 145, 100, 55))
        self.convert_btn.setText("")
        self.convert_btn.setObjectName("convert_btn")
        self.frameButtom = QtWidgets.QFrame(self.centralwidget)
        self.frameButtom.setGeometry(QtCore.QRect(20, 290, 340, 301))
        self.frameButtom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtom.setObjectName("frameButtom")
        self.button_seven = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("7"))
        self.button_seven.setGeometry(QtCore.QRect(10, 10, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_seven.setFont(font)
        self.button_seven.setObjectName("button_seven")
        self.button_eight = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("8"))
        self.button_eight.setGeometry(QtCore.QRect(120, 10, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_eight.setFont(font)
        self.button_eight.setObjectName("button_eight")
        self.button_nine = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("9"))
        self.button_nine.setGeometry(QtCore.QRect(230, 10, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.button_nine.setFont(font)
        self.button_nine.setObjectName("button_nine")
        self.button_four = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("4"))
        self.button_four.setGeometry(QtCore.QRect(10, 80, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_four.setFont(font)
        self.button_four.setObjectName("button_four")
        self.button_one = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("1"))
        self.button_one.setGeometry(QtCore.QRect(10, 150, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_one.setFont(font)
        self.button_one.setObjectName("button_one")
        self.button_c = QtWidgets.QPushButton(self.frameButtom, clicked = self.clear_input)
        self.button_c.setGeometry(QtCore.QRect(10, 220, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_c.setFont(font)
        self.button_c.setObjectName("button_c")
        self.button_five = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("5"))
        self.button_five.setGeometry(QtCore.QRect(120, 80, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_five.setFont(font)
        self.button_five.setObjectName("button_five")
        self.button_six = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("6"))
        self.button_six.setGeometry(QtCore.QRect(230, 80, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.button_six.setFont(font)
        self.button_six.setObjectName("button_six")
        self.button_two = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("2"))
        self.button_two.setGeometry(QtCore.QRect(120, 150, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_two.setFont(font)
        self.button_two.setObjectName("button_two")
        self.button_three = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("3"))
        self.button_three.setGeometry(QtCore.QRect(230, 150, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_three.setFont(font)
        self.button_three.setObjectName("button_three")
        self.button_zero = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("0"))
        self.button_zero.setGeometry(QtCore.QRect(120, 220, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_zero.setFont(font)
        self.button_zero.setObjectName("button_zero")
        self.button_dot = QtWidgets.QPushButton(self.frameButtom, clicked = lambda : self.press_btn("."))
        self.button_dot.setGeometry(QtCore.QRect(230, 220, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.button_dot.setFont(font)
        self.button_dot.setObjectName("button_dot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#============================================================= Set values to QComboBox ==========================================================
        currency_list = [
    "USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", 
    "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", 
    "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF", 
    "CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", 
    "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", 
    "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", 
    "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", 
    "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", 
    "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", 
    "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", 
    "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", 
    "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", 
    "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", 
    "SLL", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", 
    "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "UYU", 
    "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF", 
    "XPF", "YER", "ZAR", "ZMW", "ZWG", "ZWL"
]
        
        self.from_currency.addItems(currency_list)
        self.to_currency.addItems(currency_list)

#============================================================= Methods ==========================================================

    def press_btn(self, pressedBtn):
        self.from_value.setText(f"{self.from_value.text()}{pressedBtn}")

    def clear_input(self):
        self.from_value.clear()
        self.to_value.clear()

    def get_data(self):

            api_key="44a0c92786b03817601ea22c"
            selected_currency_from = self.from_currency.currentText()
            amount =float(self.from_value.text())
            selected_currency_to = self.to_currency.currentText()

            
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{selected_currency_from}"
            response = requests.get(url)
            data = response.json()
            cource = float(data['conversion_rates'][selected_currency_to])
            result = amount * cource
            self.to_value.setText(str(result))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Currency Converter"))
        self.button_seven.setText(_translate("MainWindow", "7"))
        self.button_eight.setText(_translate("MainWindow", "8"))
        self.button_nine.setText(_translate("MainWindow", "9"))
        self.button_four.setText(_translate("MainWindow", "4"))
        self.button_one.setText(_translate("MainWindow", "1"))
        self.button_c.setText(_translate("MainWindow", "C"))
        self.button_five.setText(_translate("MainWindow", "5"))
        self.button_six.setText(_translate("MainWindow", "6"))
        self.button_two.setText(_translate("MainWindow", "2"))
        self.button_three.setText(_translate("MainWindow", "3"))
        self.button_zero.setText(_translate("MainWindow", "0"))
        self.button_dot.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    MainWindow.show()
    sys.exit(app.exec_())
