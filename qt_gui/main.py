from PyQt5 import QtCore, QtGui, QtWidgets
import res, sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 742)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 30, 511, 701))
        self.widget.setStyleSheet("QLineEdit {\n"
                                  "background-color: rgba(255, 255, 255, 0);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border: none;\n"
                                  "border-bottom: 1px solid rgb(209, 209, 209, 200);\n"
                                  "font: 11pt \"Trebuchet MS\";\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(90, 80, 350, 550))
        self.label.setStyleSheet("border-image: url(:/image/17.jpg);\n"
                                 "border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(220, 220, 220, 100)))

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 350, 550))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 204), stop:0.449387 rgba(53, 53, 53, 118), stop:1 rgba(184, 184, 184, 34));\n"
            "border-radius: 20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 350, 550))
        self.label_5.setStyleSheet("background-color: rgba(22, 22, 22, 55);\n"
                                   "border-radius: 20px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(220, 156, 90, 37))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 75 22pt \"Trebuchet MS\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 270, 220, 30))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 325, 188, 30))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 490, 151, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "background:rgb(65, 65, 65, 150);\n"
                                        "font: 16pt \"Trebuchet MS\";\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background:rgb(65, 65, 65, 100);\n"
                                        "font: 16pt \"Trebuchet MS\";\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background:rgb(155, 155, 155, 150);\n"
                                        "font: 16pt \"Trebuchet MS\";\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(170, 375, 16, 16))
        self.checkBox.setStyleSheet("QCheckBox::indicator:unchecked {\n"
                                    "background: rgb(200, 200, 200, 180);\n"
                                    "border-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox:indicator:unchecked:hover {\n"
                                    "background: rgb(200, 200, 200, 220);\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator:checked {\n"
                                    "background: rgb(200, 200, 200, 180);\n"
                                    "border-radius: 3px;\n"
                                    "border-image: url(:/image/galka.png);\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox:indicator:checked:hover {\n"
                                    "background: rgb(200, 200, 200, 220);\n"
                                    "}\n"
                                    "")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(190, 375, 91, 16))
        self.label_4.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                   "color: rgb(200, 200, 200);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(288, 375, 100, 16))
        self.label_6.setStyleSheet("QLabel{\n"
                                   "font: 10pt \"Trebuchet MS\";\n"
                                   "color: rgb(200, 200, 200);\n"
                                   "}\n"
                                   "\n"
                                   "QLabel:hover{\n"
                                   "color: rgb(220, 220, 220);\n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(365, 335, 25, 25))
        self.radioButton.setStyleSheet("QRadioButton::indicator {\n"
                                       "    width: 25px;\n"
                                       "    height: 25px;\n"
                                       "}\n"
                                       "\n"
                                       "QRadioButton::indicator::unchecked {\n"
                                       "    image: url(:/image/eye2.png);\n"
                                       "}\n"
                                       "QRadioButton::indicator::unchecked:hover {\n"
                                       "    image: url(:/image/eye2_1.png);\n"
                                       "}\n"
                                       "QRadioButton::indicator::checked {\n"
                                       "    image: url(:/image/eye.png);\n"
                                       "}\n"
                                       "QRadioButton::indicator::checked:hover {\n"
                                       "    image: url(:/image/eye_1.png);\n"
                                       "}")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(405, 90, 25, 25))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(20, 20, 20);\n"
                                      "border-image: url(:/image/cross.png);\n"
                                      "border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(76, 76, 76);\n"
                                      "border-image: url(:/image/cross.png);\n"
                                      "border-radius:5px;\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.close_window)

        self.radioButton.clicked.connect(self.radioEvent)

    def radioEvent(self):
        if self.radioButton.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def close_window(self):
        app.quit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Sign In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton_2.setText(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "Save Password"))
        self.label_6.setText(_translate("Form", "Forgot password?"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
