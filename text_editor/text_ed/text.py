from PyQt5 import QtCore, QtGui, QtWidgets
import source


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Application")
        MainWindow.resize(1280, 712)
        MainWindow.setStyleSheet("QWidget{\n"
                                 "selection-background-color: rgba(255, 192, 43, 125);\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:handle:vertical,\n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:handle:vertical {\n"
                                 "background-color: rgb(121, 147, 171);\n"
                                 "height: 15px;\n"
                                 "border-radius:3px;\n"
                                 "}\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:handle:vertical:pressed, \n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:handle:vertical:pressed {\n"
                                 "background-color: rgb(149, 172, 194);\n"
                                 "}\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field  QScrollBar:sub-line:vertical, \n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:sub-line:vertical {\n"
                                 "background: none;\n"
                                 "}\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:add-line:vertical, \n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:add-line:vertical {\n"
                                 "background: none;\n"
                                 "}\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:vertical, QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:vertical {\n"
                                 "border: none;\n"
                                 "border-radius: 12px;\n"
                                 "width: 6px;\n"
                                 "background-color: rgb(176, 196, 222);\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:add-page:vertical, \n"
                                 "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:sub-page:vertical, \n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:add-page:vertical,\n"
                                 "QFrame#content QWidget#css_page QPlainTextEdit#css_form QScrollBar:sub-page:vertical{\n"
                                 "background-color: rgb(44, 52, 71, 50);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_window = QtWidgets.QFrame(self.centralwidget)
        self.title_window.setStyleSheet("QFrame {\n"
                                        "background-color: rgb(44, 52, 71);\n"
                                        "border: none;\n"
                                        "}\n"
                                        "QPushButton {\n"
                                        "border: none;\n"
                                        "background-color: rgb(44, 52, 71);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(86, 94, 110, 100);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background: rgb(86, 94, 110, 150);\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.title_window.setObjectName("title_window")
        self.title = QtWidgets.QHBoxLayout(self.title_window)
        self.title.setContentsMargins(0, 0, 0, 0)
        self.title.setSpacing(0)
        self.title.setObjectName("title")
        self.side_full_button = QtWidgets.QPushButton(self.title_window)
        self.side_full_button.setMinimumSize(QtCore.QSize(50, 50))
        self.side_full_button.setMaximumSize(QtCore.QSize(50, 50))
        self.side_full_button.setStyleSheet("border-image: url(:/icons/images/full_side2.png);")
        self.side_full_button.setText("")
        self.side_full_button.setObjectName("side_full_button")
        self.title.addWidget(self.side_full_button)
        self.status_title_bars = QtWidgets.QFrame(self.title_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_title_bars.sizePolicy().hasHeightForWidth())
        self.status_title_bars.setSizePolicy(sizePolicy)
        self.status_title_bars.setMinimumSize(QtCore.QSize(0, 50))
        self.status_title_bars.setMaximumSize(QtCore.QSize(16777215, 50))
        self.status_title_bars.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_title_bars.setObjectName("status_title_bars")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.status_title_bars)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.status_title_bars)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.title_bar.setPalette(palette)
        self.title_bar.setStyleSheet("QFrame {\n"
                                     "background-color: rgb(44, 52, 71);\n"
                                     "border: none;\n"
                                     "}\n"
                                     "QLabel {\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: 75 10pt \"Century Gothic\";\n"
                                     "padding-left: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_window = QtWidgets.QLabel(self.title_bar)
        self.name_window.setObjectName("name_window")
        self.horizontalLayout.addWidget(self.name_window)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tittle_buttons = QtWidgets.QFrame(self.title_bar)
        self.tittle_buttons.setMinimumSize(QtCore.QSize(0, 25))
        self.tittle_buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tittle_buttons.setStyleSheet("QPushButton:hover {\n"
                                          "background-color: rgb(86, 94, 110, 150);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "background-color: rgb(86, 94, 110, 220);\n"
                                          "}\n"
                                          "QPushButton#close_button:hover {\n"
                                          "background-color: rgb(255, 83, 86, 170)\n"
                                          "}\n"
                                          "QPushButton {\n"
                                          "background-color: rgb(44, 52, 71);\n"
                                          "border: none;\n"
                                          "}")
        self.tittle_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tittle_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_buttons.setLineWidth(1)
        self.tittle_buttons.setObjectName("tittle_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tittle_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hide_button = QtWidgets.QPushButton(self.tittle_buttons)
        self.hide_button.setMinimumSize(QtCore.QSize(25, 25))
        self.hide_button.setMaximumSize(QtCore.QSize(25, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.hide_button.setPalette(palette)
        self.hide_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/hide1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_button.setIcon(icon)
        self.hide_button.setFlat(False)
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout_2.addWidget(self.hide_button)
        self.full_button = QtWidgets.QPushButton(self.tittle_buttons)
        self.full_button.setMinimumSize(QtCore.QSize(25, 25))
        self.full_button.setMaximumSize(QtCore.QSize(25, 25))
        self.full_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/full1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full_button.setIcon(icon1)
        self.full_button.setObjectName("full_button")
        self.horizontalLayout_2.addWidget(self.full_button)
        self.close_button = QtWidgets.QPushButton(self.tittle_buttons)
        self.close_button.setMinimumSize(QtCore.QSize(25, 25))
        self.close_button.setMaximumSize(QtCore.QSize(25, 25))
        self.close_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.horizontalLayout.addWidget(self.tittle_buttons)
        self.verticalLayout.addWidget(self.title_bar)
        self.status_bar = QtWidgets.QFrame(self.status_title_bars)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_bar.sizePolicy().hasHeightForWidth())
        self.status_bar.setSizePolicy(sizePolicy)
        self.status_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.status_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.status_bar.setStyleSheet("QFrame{\n"
                                      "background-color:rgb(64, 73, 89);\n"
                                      "}\n"
                                      "QLabel {\n"
                                      "color: rgb(144, 154, 173);\n"
                                      "font: 75 10pt \"Century Gothic\";\n"
                                      "padding-left: 5px;\n"
                                      "}\n"
                                      "QLabel#page_name{\n"
                                      "padding-right: 5px;\n"
                                      "padding-left: 0px;\n"
                                      "}")
        self.status_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_bar.setObjectName("status_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.status_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_text = QtWidgets.QLabel(self.status_bar)
        self.status_text.setObjectName("status_text")
        self.horizontalLayout_3.addWidget(self.status_text)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.page_name = QtWidgets.QLabel(self.status_bar)
        self.page_name.setObjectName("page_name")
        self.horizontalLayout_3.addWidget(self.page_name)
        self.verticalLayout.addWidget(self.status_bar)
        self.title.addWidget(self.status_title_bars)
        self.verticalLayout_2.addWidget(self.title_window)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.side_bar = QtWidgets.QFrame(self.content)
        self.side_bar.setMinimumSize(QtCore.QSize(50, 0))
        self.side_bar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.side_bar.setStyleSheet("QFrame {\n"
                                    "background-color: rgb(44, 52, 71);\n"
                                    "border: none;\n"
                                    "}\n"
                                    "")
        self.side_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar.setObjectName("side_bar")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.side_bar)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.top_side_buttons = QtWidgets.QFrame(self.side_bar)
        self.top_side_buttons.setMinimumSize(QtCore.QSize(150, 0))
        self.top_side_buttons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_side_buttons.setStyleSheet("QPushButton {\n"
                                            "border: none;\n"
                                            "background-color: rgb(44, 52, 71);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 75 10pt \"Century Gothic\";\n"
                                            "text-align:left;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background-color: rgb(86, 94, 110, 100);\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "background: rgb(86, 94, 110, 150);\n"
                                            "}\n"
                                            "")
        self.top_side_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_side_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_side_buttons.setObjectName("top_side_buttons")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.top_side_buttons)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.home_button = QtWidgets.QPushButton(self.top_side_buttons)
        self.home_button.setMinimumSize(QtCore.QSize(50, 50))
        self.home_button.setMaximumSize(QtCore.QSize(50, 50))
        self.home_button.setStyleSheet("QPushButton {\n"
                                       "background:rgba(77, 88, 110, 50);\n"
                                       "border-right: 4px solid rgb(77, 88, 110);   \n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: rgba(86, 94, 110, 100);\n"
                                       "} \n"
                                       "QPushButton:pressed{\n"
                                       "background: rgb(86, 94, 110, 150);\n"
                                       "}\n"
                                       "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon3)
        self.home_button.setIconSize(QtCore.QSize(50, 50))
        self.home_button.setObjectName("home_button")
        self.verticalLayout_6.addWidget(self.home_button)
        self.settings_button = QtWidgets.QPushButton(self.top_side_buttons)
        self.settings_button.setMinimumSize(QtCore.QSize(50, 50))
        self.settings_button.setMaximumSize(QtCore.QSize(50, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/settings1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon4)
        self.settings_button.setIconSize(QtCore.QSize(50, 50))
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_6.addWidget(self.settings_button)
        self.verticalLayout_5.addWidget(self.top_side_buttons, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.side_bar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.content)
        self.stackedWidget.setStyleSheet("QWidget{\n"
                                         "background-color: rgb(77, 88, 110);\n"
                                         "}\n"
                                         "\n"
                                         "QFrame#content QWidget#text_page QTextEdit#text_field{\n"
                                         "padding: 5px;\n"
                                         "border: 0px;\n"
                                         "border-radius: 10px;\n"
                                         "color: white;\n"
                                         "background-color: rgb(44, 52, 71, 50);\n"
                                         "}\n"
                                         "")
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.text_page = QtWidgets.QWidget()
        self.text_page.setStyleSheet("QFrame#status_text_field{\n"
                                     "padding: 5px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "")
        self.text_page.setObjectName("text_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.text_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_field = QtWidgets.QTextEdit(self.text_page)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.text_field.setFont(font)
        self.text_field.setStyleSheet("")
        self.text_field.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_field.setTabStopWidth(80)
        self.text_field.setCursorWidth(1)
        self.text_field.setFontPointSize(12)
        self.text_field.setObjectName("text_field")
        self.verticalLayout_3.addWidget(self.text_field)
        self.status_text_field = QtWidgets.QFrame(self.text_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_text_field.sizePolicy().hasHeightForWidth())
        self.status_text_field.setSizePolicy(sizePolicy)
        self.status_text_field.setMinimumSize(QtCore.QSize(0, 35))
        self.status_text_field.setMaximumSize(QtCore.QSize(16777215, 35))
        self.status_text_field.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "font: 75 10pt \"Century Gothic\";")
        self.status_text_field.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status_text_field.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_text_field.setObjectName("status_text_field")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.status_text_field)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.status_bar_2 = QtWidgets.QFrame(self.status_text_field)
        self.status_bar_2.setObjectName("status_bar_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.status_bar_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(25)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.words_ = QtWidgets.QFrame(self.status_bar_2)
        self.words_.setObjectName("words_")
        self.words = QtWidgets.QHBoxLayout(self.words_)
        self.words.setContentsMargins(0, 0, 0, 0)
        self.words.setSpacing(4)
        self.words.setObjectName("words")
        self.words_label = QtWidgets.QLabel(self.words_)
        self.words_label.setObjectName("words_label")
        self.words.addWidget(self.words_label)
        self.words_count = QtWidgets.QLabel(self.words_)
        self.words_count.setObjectName("words_count")
        self.words.addWidget(self.words_count)
        self.horizontalLayout_6.addWidget(self.words_)
        self.chars_ = QtWidgets.QFrame(self.status_bar_2)
        self.chars_.setObjectName("chars_")
        self.chars = QtWidgets.QHBoxLayout(self.chars_)
        self.chars.setContentsMargins(0, 0, 0, 0)
        self.chars.setSpacing(4)
        self.chars.setObjectName("chars")
        self.chars_label = QtWidgets.QLabel(self.chars_)
        self.chars_label.setObjectName("chars_label")
        self.chars.addWidget(self.chars_label)
        self.chars_count = QtWidgets.QLabel(self.chars_)
        self.chars_count.setObjectName("chars_count")
        self.chars.addWidget(self.chars_count)
        self.selected_chars = QtWidgets.QLabel(self.chars_)
        self.selected_chars.setObjectName("selected_chars")
        self.chars.addWidget(self.selected_chars)
        self.horizontalLayout_6.addWidget(self.chars_)
        self.lines = QtWidgets.QFrame(self.status_bar_2)
        self.lines.setObjectName("lines")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lines)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lines_label = QtWidgets.QLabel(self.lines)
        self.lines_label.setObjectName("lines_label")
        self.horizontalLayout_5.addWidget(self.lines_label)
        self.count_lines = QtWidgets.QLabel(self.lines)
        self.count_lines.setObjectName("count_lines")
        self.horizontalLayout_5.addWidget(self.count_lines)
        self.current_lines = QtWidgets.QLabel(self.lines)
        self.current_lines.setObjectName("current_lines")
        self.horizontalLayout_5.addWidget(self.current_lines)
        self.horizontalLayout_6.addWidget(self.lines)
        self.horizontalLayout_7.addWidget(self.status_bar_2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.status_text_field)
        self.status_text_field.raise_()
        self.text_field.raise_()
        self.stackedWidget.addWidget(self.text_page)
        self.css_page = QtWidgets.QWidget()
        self.css_page.setStyleSheet("QPlainTextEdit{\n"
                                    "font: 12pt \"Trebuchet MS\";\n"
                                    "padding: 5px;\n"
                                    "border: 0px;\n"
                                    "border-radius: 10px;\n"
                                    "color: white;\n"
                                    "background-color: rgb(44, 52, 71, 50);\n"
                                    "}")
        self.css_page.setObjectName("css_page")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.css_page)
        self.horizontalLayout_11.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.css_window = QtWidgets.QFrame(self.css_page)
        self.css_window.setMinimumSize(QtCore.QSize(350, 400))
        self.css_window.setMaximumSize(QtCore.QSize(350, 400))
        self.css_window.setObjectName("css_window")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.css_window)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.examples = QtWidgets.QStackedWidget(self.css_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examples.sizePolicy().hasHeightForWidth())
        self.examples.setSizePolicy(sizePolicy)
        self.examples.setMinimumSize(QtCore.QSize(350, 350))
        self.examples.setMaximumSize(QtCore.QSize(350, 350))
        self.examples.setStyleSheet("QWidget{\n"
                                    "background-color: rgb(55, 66, 87);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.examples.setObjectName("examples")
        self.button = QtWidgets.QWidget()
        self.button.setStyleSheet("QPushButton{\n"
                                  "background: white;\n"
                                  "}")
        self.button.setObjectName("button")
        self.css_pushButton = QtWidgets.QPushButton(self.button)
        self.css_pushButton.setGeometry(QtCore.QRect(132, 162, 75, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.css_pushButton.sizePolicy().hasHeightForWidth())
        self.css_pushButton.setSizePolicy(sizePolicy)
        self.css_pushButton.setObjectName("css_pushButton")
        self.examples.addWidget(self.button)
        self.label = QtWidgets.QWidget()
        self.label.setStyleSheet("QLabel{\n"
                                 "color: white;\n"
                                 "}")
        self.label.setObjectName("label")
        self.css_label = QtWidgets.QLabel(self.label)
        self.css_label.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.css_label.setObjectName("css_label")
        self.examples.addWidget(self.label)
        self.horizontal_scroll_bar = QtWidgets.QWidget()
        self.horizontal_scroll_bar.setObjectName("horizontal_scroll_bar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.horizontal_scroll_bar)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(80, 170, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.examples.addWidget(self.horizontal_scroll_bar)
        self.vertical_scroll_bar = QtWidgets.QWidget()
        self.vertical_scroll_bar.setObjectName("vertical_scroll_bar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.vertical_scroll_bar)
        self.verticalScrollBar.setGeometry(QtCore.QRect(160, 90, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.examples.addWidget(self.vertical_scroll_bar)
        self.vertical_slider_bar = QtWidgets.QWidget()
        self.vertical_slider_bar.setObjectName("vertical_slider_bar")
        self.verticalSlider = QtWidgets.QSlider(self.vertical_slider_bar)
        self.verticalSlider.setGeometry(QtCore.QRect(150, 110, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.examples.addWidget(self.vertical_slider_bar)
        self.horizontal_slider_bar = QtWidgets.QWidget()
        self.horizontal_slider_bar.setObjectName("horizontal_slider_bar")
        self.horizontalSlider = QtWidgets.QSlider(self.horizontal_slider_bar)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 160, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.examples.addWidget(self.horizontal_slider_bar)
        self.radio_button = QtWidgets.QWidget()
        self.radio_button.setStyleSheet("QRadioButton{\n"
                                        "color: white;\n"
                                        "}")
        self.radio_button.setObjectName("radio_button")
        self.radioButton = QtWidgets.QRadioButton(self.radio_button)
        self.radioButton.setGeometry(QtCore.QRect(110, 170, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.examples.addWidget(self.radio_button)
        self.line_edit = QtWidgets.QWidget()
        self.line_edit.setStyleSheet("QLineEdit{\n"
                                     "background: white;\n"
                                     "}")
        self.line_edit.setObjectName("line_edit")
        self.lineEdit = QtWidgets.QLineEdit(self.line_edit)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.examples.addWidget(self.line_edit)
        self.check_box = QtWidgets.QWidget()
        self.check_box.setStyleSheet("QCheckBox{\n"
                                     "color: white;\n"
                                     "}")
        self.check_box.setObjectName("check_box")
        self.checkBox = QtWidgets.QCheckBox(self.check_box)
        self.checkBox.setGeometry(QtCore.QRect(130, 170, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.examples.addWidget(self.check_box)
        self.verticalLayout_4.addWidget(self.examples)
        self.examples_bar = QtWidgets.QFrame(self.css_window)
        self.examples_bar.setMinimumSize(QtCore.QSize(0, 0))
        self.examples_bar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.examples_bar.setStyleSheet("QLabel{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 75 10pt \"Century Gothic\";\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox{\n"
                                        "border:0px;\n"
                                        "background-color: rgb(55, 66, 87, 175);\n"
                                        "border-radius: 5px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "padding\n"
                                        "}\n"
                                        "QComboBox:on {\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "background-color: rgb(55, 66, 87);\n"
                                        "}\n"
                                        "QComboBox::drop-down {\n"
                                        "border-radius: 0px;\n"
                                        "}\n"
                                        "QComboBox:down-arrow {\n"
                                        "border-image: url(:/icons/images/arrow_combo_box_down.png);\n"
                                        "}\n"
                                        "QComboBox::down-arrow:on {\n"
                                        "border-image: url(:/icons/images/arrow_combo_box_up.png)\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView {\n"
                                        "background: rgb(63, 78, 107);\n"
                                        "outline: 0;\n"
                                        "border: 0px;\n"
                                        "color:white;\n"
                                        "selection-background-color: rgb(55, 66, 87);\n"
                                        "\n"
                                        "}")
        self.examples_bar.setObjectName("examples_bar")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.examples_bar)
        self.horizontalLayout_10.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_box = QtWidgets.QComboBox(self.examples_bar)
        self.widget_box.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.widget_box.setFont(font)
        self.widget_box.setObjectName("widget_box")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.widget_box.addItem("")
        self.horizontalLayout_10.addWidget(self.widget_box)
        self.verticalLayout_4.addWidget(self.examples_bar, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_11.addWidget(self.css_window)
        self.css_form = QtWidgets.QPlainTextEdit(self.css_page)
        self.css_form.setMinimumSize(QtCore.QSize(500, 0))
        self.css_form.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.css_form.setObjectName("css_form")
        self.horizontalLayout_11.addWidget(self.css_form)
        self.stackedWidget.addWidget(self.css_page)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.tools_bar = QtWidgets.QFrame(self.content)
        self.tools_bar.setMinimumSize(QtCore.QSize(175, 0))
        self.tools_bar.setMaximumSize(QtCore.QSize(25, 16777215))
        self.tools_bar.setStyleSheet("QFrame {\n"
                                     "background-color: rgb(44, 52, 71);\n"
                                     "border: none;\n"
                                     "}\n"
                                     "")
        self.tools_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tools_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools_bar.setObjectName("tools_bar")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tools_bar)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.co_button_frame = QtWidgets.QFrame(self.tools_bar)
        self.co_button_frame.setMinimumSize(QtCore.QSize(0, 25))
        self.co_button_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.co_button_frame.setStyleSheet("QPushButton {\n"
                                           "border: none;\n"
                                           "border-radius: 2px;\n"
                                           "background-color: rgb(44, 52, 71);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "font: 75 10pt \"Century Gothic\";\n"
                                           "text-align:left;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: rgba(86, 94, 110, 100);\n"
                                           "} \n"
                                           "QPushButton:pressed{\n"
                                           "background: rgb(86, 94, 110, 150);\n"
                                           "}\n"
                                           "")
        self.co_button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.co_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.co_button_frame.setObjectName("co_button_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.co_button_frame)
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.close_open_tools_bar_but = QtWidgets.QPushButton(self.co_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_open_tools_bar_but.sizePolicy().hasHeightForWidth())
        self.close_open_tools_bar_but.setSizePolicy(sizePolicy)
        self.close_open_tools_bar_but.setMinimumSize(QtCore.QSize(15, 15))
        self.close_open_tools_bar_but.setMaximumSize(QtCore.QSize(15, 15))
        self.close_open_tools_bar_but.setStyleSheet("")
        self.close_open_tools_bar_but.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/arrow_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_open_tools_bar_but.setIcon(icon5)
        self.close_open_tools_bar_but.setIconSize(QtCore.QSize(15, 15))
        self.close_open_tools_bar_but.setObjectName("close_open_tools_bar_but")
        self.horizontalLayout_8.addWidget(self.close_open_tools_bar_but)
        self.verticalLayout_8.addWidget(self.co_button_frame, 0, QtCore.Qt.AlignLeft)
        self.tools_frame = QtWidgets.QFrame(self.tools_bar)
        self.tools_frame.setMinimumSize(QtCore.QSize(175, 0))
        self.tools_frame.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tools_frame.setFont(font)
        self.tools_frame.setStyleSheet("QCheckBox {\n"
                                       "color: white;\n"
                                       "}\n"
                                       "QCheckBox:indicator{\n"
                                       "background-color: rgb(176, 196, 222, 120);\n"
                                       "border-radius: 3px;\n"
                                       "width: 15px;\n"
                                       "height: 15px;\n"
                                       "}\n"
                                       "QCheckBox:indicator:hover {\n"
                                       "background-color: rgb(176, 196, 222, 200);\n"
                                       "}\n"
                                       "QCheckBox:indicator:checked {\n"
                                       "border-image: url(:/icons/images/checked.png);\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::groove:horizontal {\n"
                                       "height: 3px; \n"
                                       "background-color: rgb(176, 196, 222, 180);\n"
                                       "border-radius: 1px;\n"
                                       "}\n"
                                       "QSlider::handle:horizontal {\n"
                                       "background-color: rgb(176, 196, 222);\n"
                                       "width:10px;\n"
                                       "margin-top: -3px;\n"
                                       "margin-bottom: -3px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QLabel{\n"
                                       "color:white;\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit{\n"
                                       "color: white;\n"
                                       "padding:2px;\n"
                                       "border: none;\n"
                                       "border-radius: 5px;\n"
                                       "background-color: rgb(176, 196, 222, 120);\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.tools_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools_frame.setObjectName("tools_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tools_frame)
        self.verticalLayout_7.setContentsMargins(25, 25, 25, -1)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.findword_line = QtWidgets.QLineEdit(self.tools_frame)
        self.findword_line.setMinimumSize(QtCore.QSize(125, 24))
        self.findword_line.setMaximumSize(QtCore.QSize(125, 24))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.findword_line.setFont(font)
        self.findword_line.setObjectName("findword_line")
        self.verticalLayout_7.addWidget(self.findword_line)
        self.font_size_frame = QtWidgets.QFrame(self.tools_frame)
        self.font_size_frame.setStyleSheet("QSpinBox{\n"
                                           "color: white;\n"
                                           "padding:2px;\n"
                                           "border: none;\n"
                                           "border-radius: 4px;\n"
                                           "background-color: rgb(176, 196, 222, 120);\n"
                                           "}")
        self.font_size_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.font_size_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.font_size_frame.setObjectName("font_size_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.font_size_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.font_size_label = QtWidgets.QLabel(self.font_size_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_label.sizePolicy().hasHeightForWidth())
        self.font_size_label.setSizePolicy(sizePolicy)
        self.font_size_label.setMinimumSize(QtCore.QSize(61, 10))
        self.font_size_label.setMaximumSize(QtCore.QSize(61, 10))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.font_size_label.setFont(font)
        self.font_size_label.setObjectName("font_size_label")
        self.horizontalLayout_9.addWidget(self.font_size_label)
        self.font_spin_box = QtWidgets.QSpinBox(self.font_size_frame)
        self.font_spin_box.setAlignment(QtCore.Qt.AlignCenter)
        self.font_spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.font_spin_box.setSpecialValueText("")
        self.font_spin_box.setMinimum(10)
        self.font_spin_box.setMaximum(72)
        self.font_spin_box.setProperty("value", 12)
        self.font_spin_box.setObjectName("font_spin_box")
        self.horizontalLayout_9.addWidget(self.font_spin_box)
        self.verticalLayout_7.addWidget(self.font_size_frame)
        self.font_style_frame = QtWidgets.QFrame(self.tools_frame)
        self.font_style_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.font_style_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.font_style_frame.setObjectName("font_style_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.font_style_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.underline_check_box = QtWidgets.QCheckBox(self.font_style_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.underline_check_box.setFont(font)
        self.underline_check_box.setObjectName("underline_check_box")
        self.verticalLayout_9.addWidget(self.underline_check_box)
        self.italic_check_box = QtWidgets.QCheckBox(self.font_style_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.italic_check_box.setFont(font)
        self.italic_check_box.setObjectName("italic_check_box")
        self.verticalLayout_9.addWidget(self.italic_check_box)
        self.bold_check_box = QtWidgets.QCheckBox(self.font_style_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.bold_check_box.setFont(font)
        self.bold_check_box.setObjectName("bold_check_box")
        self.verticalLayout_9.addWidget(self.bold_check_box)
        self.verticalLayout_7.addWidget(self.font_style_frame)
        self.verticalLayout_8.addWidget(self.tools_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.file_frame = QtWidgets.QFrame(self.tools_bar)
        self.file_frame.setMinimumSize(QtCore.QSize(175, 0))
        self.file_frame.setMaximumSize(QtCore.QSize(175, 16777215))
        self.file_frame.setStyleSheet("QPushButton{\n"
                                      "border: none;\n"
                                      "border-radius:10px;\n"
                                      "padding:5px;\n"
                                      "color:white;\n"
                                      "background-color:rgba(64, 73, 89, 180);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(86, 94, 110, 100);\n"
                                      "}\n"
                                      "QPushButton:hover:pressed{\n"
                                      "background: rgb(86, 94, 110, 150);\n"
                                      "}")
        self.file_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.file_frame)
        self.verticalLayout_10.setContentsMargins(40, 12, 40, 12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.save_button = QtWidgets.QPushButton(self.file_frame)
        self.save_button.setMinimumSize(QtCore.QSize(0, 0))
        self.save_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_10.addWidget(self.save_button)
        self.open_button = QtWidgets.QPushButton(self.file_frame)
        self.open_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.verticalLayout_10.addWidget(self.open_button)
        self.new_button = QtWidgets.QPushButton(self.file_frame)
        self.new_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.new_button.setFont(font)
        self.new_button.setObjectName("new_button")
        self.verticalLayout_10.addWidget(self.new_button)
        self.verticalLayout_8.addWidget(self.file_frame)
        self.horizontalLayout_4.addWidget(self.tools_bar)
        self.verticalLayout_2.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.examples.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_window.setText(_translate("MainWindow", "Application"))
        self.status_text.setText(_translate("MainWindow", "File name"))
        self.page_name.setText(_translate("MainWindow", "| Text Field"))
        self.home_button.setText(_translate("MainWindow", "Home Page"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.text_field.setPlaceholderText(_translate("MainWindow", "Write here"))
        self.words_label.setText(_translate("MainWindow", "words:"))
        self.words_count.setText(_translate("MainWindow", "0"))
        self.chars_label.setText(_translate("MainWindow", "chars:"))
        self.chars_count.setText(_translate("MainWindow", "0,"))
        self.selected_chars.setText(_translate("MainWindow", "0"))
        self.lines_label.setText(_translate("MainWindow", "lines:"))
        self.count_lines.setText(_translate("MainWindow", "1,"))
        self.current_lines.setText(_translate("MainWindow", "1"))
        self.css_pushButton.setText(_translate("MainWindow", "PushButton"))
        self.css_label.setText(_translate("MainWindow", "TextLabel"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.widget_box.setCurrentText(_translate("MainWindow", "Button"))
        self.widget_box.setItemText(0, _translate("MainWindow", "Button"))
        self.widget_box.setItemText(1, _translate("MainWindow", "Label"))
        self.widget_box.setItemText(2, _translate("MainWindow", "Horizontal Scroll Bar"))
        self.widget_box.setItemText(3, _translate("MainWindow", "Vertical Scroll Bar"))
        self.widget_box.setItemText(4, _translate("MainWindow", "Vertical Slider"))
        self.widget_box.setItemText(5, _translate("MainWindow", "Horizontal Slider"))
        self.widget_box.setItemText(6, _translate("MainWindow", "Line Edit"))
        self.widget_box.setItemText(7, _translate("MainWindow", "Radio Button"))
        self.widget_box.setItemText(8, _translate("MainWindow", "Check Box"))
        self.css_form.setPlaceholderText(_translate("MainWindow", "CSS Code"))
        self.findword_line.setPlaceholderText(_translate("MainWindow", "Find word"))
        self.font_size_label.setText(_translate("MainWindow", "Font size:"))
        self.underline_check_box.setText(_translate("MainWindow", "Underline"))
        self.italic_check_box.setText(_translate("MainWindow", "Italic"))
        self.bold_check_box.setText(_translate("MainWindow", "Bold"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.new_button.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# from PyQt5 import QtCore, QtGui, QtWidgets
# import source
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1280, 720)
#         MainWindow.setStyleSheet("QWidget{\n"
#                                  "selection-background-color: rgba(255, 192, 43, 125);\n"
#                                  "}\n"
#                                  "\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:handle:vertical {\n"
#                                  "background-color: rgb(121, 147, 171);\n"
#                                  "height: 15px;\n"
#                                  "border-radius:3px;\n"
#                                  "}\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:handle:vertical:pressed {\n"
#                                  "background-color: rgb(149, 172, 194);\n"
#                                  "}\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field  QScrollBar:sub-line:vertical {\n"
#                                  "background: none;\n"
#                                  "}\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:add-line:vertical {\n"
#                                  "background: none;\n"
#                                  "}\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:vertical {\n"
#                                  "border: none;\n"
#                                  "border-radius: 12px;\n"
#                                  "width: 6px;\n"
#                                  "background-color: rgb(176, 196, 222);\n"
#                                  "}\n"
#                                  "\n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:add-page:vertical, \n"
#                                  "QFrame#content QWidget#text_page QTextEdit#text_field QScrollBar:sub-page:vertical{\n"
#                                  "background-color: rgb(44, 52, 71, 50);\n"
#                                  "}")
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setStyleSheet("")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_2.setSpacing(0)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.title_window = QtWidgets.QFrame(self.centralwidget)
#         self.title_window.setStyleSheet("QFrame {\n"
#                                         "background-color: rgb(44, 52, 71);\n"
#                                         "border: none;\n"
#                                         "}\n"
#                                         "QPushButton {\n"
#                                         "border: none;\n"
#                                         "background-color: rgb(44, 52, 71);\n"
#                                         "}\n"
#                                         "QPushButton:hover {\n"
#                                         "background-color: rgb(86, 94, 110, 100);\n"
#                                         "}\n"
#                                         "QPushButton:pressed{\n"
#                                         "background: rgb(86, 94, 110, 150);\n"
#                                         "}\n"
#                                         "\n"
#                                         "")
#         self.title_window.setObjectName("title_window")
#         self.title = QtWidgets.QHBoxLayout(self.title_window)
#         self.title.setContentsMargins(0, 0, 0, 0)
#         self.title.setSpacing(0)
#         self.title.setObjectName("title")
#         self.side_full_button = QtWidgets.QPushButton(self.title_window)
#         self.side_full_button.setMinimumSize(QtCore.QSize(50, 50))
#         self.side_full_button.setMaximumSize(QtCore.QSize(50, 50))
#         self.side_full_button.setStyleSheet("border-image: url(:/icons/images/full_side2.png);")
#         self.side_full_button.setText("")
#         self.side_full_button.setObjectName("side_full_button")
#         self.title.addWidget(self.side_full_button)
#         self.status_title_bars = QtWidgets.QFrame(self.title_window)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.status_title_bars.sizePolicy().hasHeightForWidth())
#         self.status_title_bars.setSizePolicy(sizePolicy)
#         self.status_title_bars.setMinimumSize(QtCore.QSize(0, 50))
#         self.status_title_bars.setMaximumSize(QtCore.QSize(16777215, 50))
#         self.status_title_bars.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.status_title_bars.setObjectName("status_title_bars")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.status_title_bars)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setSpacing(0)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.title_bar = QtWidgets.QFrame(self.status_title_bars)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
#         self.title_bar.setSizePolicy(sizePolicy)
#         self.title_bar.setMinimumSize(QtCore.QSize(0, 25))
#         self.title_bar.setMaximumSize(QtCore.QSize(16777215, 25))
#         palette = QtGui.QPalette()
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
#         self.title_bar.setPalette(palette)
#         self.title_bar.setStyleSheet("QFrame {\n"
#                                      "background-color: rgb(44, 52, 71);\n"
#                                      "border: none;\n"
#                                      "}\n"
#                                      "QLabel {\n"
#                                      "color: rgb(255, 255, 255);\n"
#                                      "font: 75 10pt \"Century Gothic\";\n"
#                                      "padding-left: 5px;\n"
#                                      "}\n"
#                                      "\n"
#                                      "")
#         self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.title_bar.setObjectName("title_bar")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setSpacing(0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.name_window = QtWidgets.QLabel(self.title_bar)
#         self.name_window.setObjectName("name_window")
#         self.horizontalLayout.addWidget(self.name_window)
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout.addItem(spacerItem)
#         self.tittle_buttons = QtWidgets.QFrame(self.title_bar)
#         self.tittle_buttons.setMinimumSize(QtCore.QSize(0, 25))
#         self.tittle_buttons.setMaximumSize(QtCore.QSize(16777215, 50))
#         self.tittle_buttons.setStyleSheet("QPushButton:hover {\n"
#                                           "background-color: rgb(86, 94, 110, 150);\n"
#                                           "}\n"
#                                           "QPushButton:pressed{\n"
#                                           "background-color: rgb(86, 94, 110, 220);\n"
#                                           "}\n"
#                                           "QPushButton#close_button:hover {\n"
#                                           "background-color: rgb(255, 83, 86, 170)\n"
#                                           "}\n"
#                                           "QPushButton {\n"
#                                           "background-color: rgb(44, 52, 71);\n"
#                                           "border: none;\n"
#                                           "}")
#         self.tittle_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.tittle_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.tittle_buttons.setLineWidth(1)
#         self.tittle_buttons.setObjectName("tittle_buttons")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tittle_buttons)
#         self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_2.setSpacing(0)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.hide_button = QtWidgets.QPushButton(self.tittle_buttons)
#         self.hide_button.setMinimumSize(QtCore.QSize(25, 25))
#         self.hide_button.setMaximumSize(QtCore.QSize(25, 25))
#         palette = QtGui.QPalette()
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(44, 52, 71))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 192, 43, 125))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
#         self.hide_button.setPalette(palette)
#         self.hide_button.setText("")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/images/hide1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.hide_button.setIcon(icon)
#         self.hide_button.setFlat(False)
#         self.hide_button.setObjectName("hide_button")
#         self.horizontalLayout_2.addWidget(self.hide_button)
#         self.full_button = QtWidgets.QPushButton(self.tittle_buttons)
#         self.full_button.setMinimumSize(QtCore.QSize(25, 25))
#         self.full_button.setMaximumSize(QtCore.QSize(25, 25))
#         self.full_button.setText("")
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/images/full1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.full_button.setIcon(icon1)
#         self.full_button.setObjectName("full_button")
#         self.horizontalLayout_2.addWidget(self.full_button)
#         self.close_button = QtWidgets.QPushButton(self.tittle_buttons)
#         self.close_button.setMinimumSize(QtCore.QSize(25, 25))
#         self.close_button.setMaximumSize(QtCore.QSize(25, 25))
#         self.close_button.setText("")
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.close_button.setIcon(icon2)
#         self.close_button.setObjectName("close_button")
#         self.horizontalLayout_2.addWidget(self.close_button)
#         self.horizontalLayout.addWidget(self.tittle_buttons)
#         self.verticalLayout.addWidget(self.title_bar)
#         self.status_bar = QtWidgets.QFrame(self.status_title_bars)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.status_bar.sizePolicy().hasHeightForWidth())
#         self.status_bar.setSizePolicy(sizePolicy)
#         self.status_bar.setMinimumSize(QtCore.QSize(0, 25))
#         self.status_bar.setMaximumSize(QtCore.QSize(16777215, 25))
#         self.status_bar.setStyleSheet("QFrame{\n"
#                                       "background-color:rgb(64, 73, 89);\n"
#                                       "}\n"
#                                       "QLabel {\n"
#                                       "color: rgb(144, 154, 173);\n"
#                                       "font: 75 10pt \"Century Gothic\";\n"
#                                       "padding-left: 5px;\n"
#                                       "}\n"
#                                       "QLabel#page_name{\n"
#                                       "padding-right: 5px;\n"
#                                       "padding-left: 0px;\n"
#                                       "}")
#         self.status_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.status_bar.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.status_bar.setObjectName("status_bar")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.status_bar)
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_3.setSpacing(0)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.status_text = QtWidgets.QLabel(self.status_bar)
#         self.status_text.setObjectName("status_text")
#         self.horizontalLayout_3.addWidget(self.status_text)
#         spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout_3.addItem(spacerItem1)
#         self.page_name = QtWidgets.QLabel(self.status_bar)
#         self.page_name.setObjectName("page_name")
#         self.horizontalLayout_3.addWidget(self.page_name)
#         self.verticalLayout.addWidget(self.status_bar)
#         self.title.addWidget(self.status_title_bars)
#         self.verticalLayout_2.addWidget(self.title_window)
#         self.content = QtWidgets.QFrame(self.centralwidget)
#         self.content.setStyleSheet("")
#         self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.content.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.content.setObjectName("content")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
#         self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_4.setSpacing(0)
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.side_bar = QtWidgets.QFrame(self.content)
#         self.side_bar.setMinimumSize(QtCore.QSize(50, 0))
#         self.side_bar.setMaximumSize(QtCore.QSize(50, 16777215))
#         self.side_bar.setStyleSheet("QFrame {\n"
#                                     "background-color: rgb(44, 52, 71);\n"
#                                     "border: none;\n"
#                                     "}\n"
#                                     "")
#         self.side_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.side_bar.setObjectName("side_bar")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.side_bar)
#         self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_5.setSpacing(0)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.top_side_buttons = QtWidgets.QFrame(self.side_bar)
#         self.top_side_buttons.setMinimumSize(QtCore.QSize(150, 0))
#         self.top_side_buttons.setMaximumSize(QtCore.QSize(150, 16777215))
#         self.top_side_buttons.setStyleSheet("QPushButton {\n"
#                                             "border: none;\n"
#                                             "background-color: rgb(44, 52, 71);\n"
#                                             "color: rgb(255, 255, 255);\n"
#                                             "font: 75 10pt \"Century Gothic\";\n"
#                                             "text-align:left;\n"
#                                             "}\n"
#                                             "QPushButton:hover {\n"
#                                             "background-color: rgb(86, 94, 110, 100);\n"
#                                             "}\n"
#                                             "QPushButton:pressed{\n"
#                                             "background: rgb(86, 94, 110, 150);\n"
#                                             "}\n"
#                                             "")
#         self.top_side_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.top_side_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.top_side_buttons.setObjectName("top_side_buttons")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.top_side_buttons)
#         self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_6.setSpacing(0)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.home_button = QtWidgets.QPushButton(self.top_side_buttons)
#         self.home_button.setMinimumSize(QtCore.QSize(50, 50))
#         self.home_button.setMaximumSize(QtCore.QSize(50, 50))
#         self.home_button.setStyleSheet("QPushButton {\n"
#                                        "background:rgba(77, 88, 110, 50);\n"
#                                        "border-right: 4px solid rgb(77, 88, 110);   \n"
#                                        "}\n"
#                                        "QPushButton:hover {\n"
#                                        "background: rgba(86, 94, 110, 100);\n"
#                                        "} \n"
#                                        "QPushButton:pressed{\n"
#                                        "background: rgb(86, 94, 110, 150);\n"
#                                        "}\n"
#                                        "")
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.home_button.setIcon(icon3)
#         self.home_button.setIconSize(QtCore.QSize(50, 50))
#         self.home_button.setObjectName("home_button")
#         self.verticalLayout_6.addWidget(self.home_button)
#         self.settings_button = QtWidgets.QPushButton(self.top_side_buttons)
#         self.settings_button.setMinimumSize(QtCore.QSize(50, 50))
#         self.settings_button.setMaximumSize(QtCore.QSize(50, 50))
#         icon4 = QtGui.QIcon()
#         icon4.addPixmap(QtGui.QPixmap(":/icons/images/settings1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.settings_button.setIcon(icon4)
#         self.settings_button.setIconSize(QtCore.QSize(50, 50))
#         self.settings_button.setObjectName("settings_button")
#         self.verticalLayout_6.addWidget(self.settings_button)
#         self.verticalLayout_5.addWidget(self.top_side_buttons, 0, QtCore.Qt.AlignTop)
#         self.bottom_side_buttons = QtWidgets.QFrame(self.side_bar)
#         self.bottom_side_buttons.setMinimumSize(QtCore.QSize(150, 50))
#         self.bottom_side_buttons.setMaximumSize(QtCore.QSize(150, 50))
#         self.bottom_side_buttons.setStyleSheet("QPushButton{\n"
#                                                "border-radius: 15px;\n"
#                                                "background-color: rgb(64, 73, 89);\n"
#                                                "color: rgb(144, 154, 173);\n"
#                                                "font: 75 10pt \"Century Gothic\";\n"
#                                                "}\n"
#                                                "QPushButton:hover{\n"
#                                                "background-color: rgb(91, 104, 128, 180);\n"
#                                                "color: rgb(176, 188, 212);\n"
#                                                "font: 75 10pt \"Century Gothic\";\n"
#                                                "}\n"
#                                                "QPushButton:pressed{\n"
#                                                "background-color: rgb(91, 104, 128);\n"
#                                                "color: rgb(176, 188, 212);\n"
#                                                "font: 75 10pt \"Century Gothic\";\n"
#                                                "}")
#         self.bottom_side_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.bottom_side_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.bottom_side_buttons.setObjectName("bottom_side_buttons")
#         self.account_button_2 = QtWidgets.QPushButton(self.bottom_side_buttons)
#         self.account_button_2.setGeometry(QtCore.QRect(10, 10, 30, 30))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.account_button_2.sizePolicy().hasHeightForWidth())
#         self.account_button_2.setSizePolicy(sizePolicy)
#         self.account_button_2.setMinimumSize(QtCore.QSize(30, 30))
#         self.account_button_2.setMaximumSize(QtCore.QSize(30, 30))
#         self.account_button_2.setStyleSheet("")
#         self.account_button_2.setObjectName("account_button_2")
#         self.verticalLayout_5.addWidget(self.bottom_side_buttons)
#         self.horizontalLayout_4.addWidget(self.side_bar)
#         self.stackedWidget = QtWidgets.QStackedWidget(self.content)
#         self.stackedWidget.setStyleSheet("QWidget{\n"
#                                          "background-color: rgb(77, 88, 110);\n"
#                                          "}\n"
#                                          "\n"
#                                          "QFrame#content QWidget#text_page QTextEdit#text_field{\n"
#                                          "padding: 5px;\n"
#                                          "border: 0px;\n"
#                                          "border-radius: 10px;\n"
#                                          "color: white;\n"
#                                          "background-color: rgb(44, 52, 71, 50);\n"
#                                          "}\n"
#                                          "")
#         self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.stackedWidget.setObjectName("stackedWidget")
#         self.text_page = QtWidgets.QWidget()
#         self.text_page.setStyleSheet("QFrame#status_text_field{\n"
#                                      "padding: 5px;\n"
#                                      "color: white;\n"
#                                      "}\n"
#                                      "")
#         self.text_page.setObjectName("text_page")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.text_page)
#         self.verticalLayout_3.setContentsMargins(8, 8, 8, 3)
#         self.verticalLayout_3.setSpacing(2)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.text_field = QtWidgets.QTextEdit(self.text_page)
#         font = QtGui.QFont()
#         font.setFamily("Trebuchet MS")
#         font.setPointSize(12)
#         self.text_field.setFont(font)
#         self.text_field.setFontPointSize(12)
#         self.text_field.setStyleSheet("")
#         self.text_field.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.text_field.setTabStopWidth(80)
#         self.text_field.setCursorWidth(1)
#         self.text_field.setObjectName("text_field")
#         self.verticalLayout_3.addWidget(self.text_field)
#         self.status_text_field = QtWidgets.QFrame(self.text_page)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.status_text_field.sizePolicy().hasHeightForWidth())
#         self.status_text_field.setSizePolicy(sizePolicy)
#         self.status_text_field.setMinimumSize(QtCore.QSize(0, 35))
#         self.status_text_field.setMaximumSize(QtCore.QSize(16777215, 35))
#         self.status_text_field.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                              "color: rgb(255, 255, 255);\n"
#                                              "font: 75 10pt \"Century Gothic\";")
#         self.status_text_field.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.status_text_field.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.status_text_field.setObjectName("status_text_field")
#         self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.status_text_field)
#         self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_7.setSpacing(0)
#         self.horizontalLayout_7.setObjectName("horizontalLayout_7")
#         self.status_bar_2 = QtWidgets.QFrame(self.status_text_field)
#         self.status_bar_2.setObjectName("status_bar_2")
#         self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.status_bar_2)
#         self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_6.setSpacing(25)
#         self.horizontalLayout_6.setObjectName("horizontalLayout_6")
#         self.words_ = QtWidgets.QFrame(self.status_bar_2)
#         self.words_.setObjectName("words_")
#         self.words = QtWidgets.QHBoxLayout(self.words_)
#         self.words.setContentsMargins(0, 0, 0, 0)
#         self.words.setSpacing(4)
#         self.words.setObjectName("words")
#         self.words_label = QtWidgets.QLabel(self.words_)
#         self.words_label.setObjectName("words_label")
#         self.words.addWidget(self.words_label)
#         self.words_count = QtWidgets.QLabel(self.words_)
#         self.words_count.setObjectName("words_count")
#         self.words.addWidget(self.words_count)
#         self.horizontalLayout_6.addWidget(self.words_)
#         self.chars_ = QtWidgets.QFrame(self.status_bar_2)
#         self.chars_.setObjectName("chars_")
#         self.chars = QtWidgets.QHBoxLayout(self.chars_)
#         self.chars.setContentsMargins(0, 0, 0, 0)
#         self.chars.setSpacing(4)
#         self.chars.setObjectName("chars")
#         self.chars_label = QtWidgets.QLabel(self.chars_)
#         self.chars_label.setObjectName("chars_label")
#         self.chars.addWidget(self.chars_label)
#         self.chars_count = QtWidgets.QLabel(self.chars_)
#         self.chars_count.setObjectName("chars_count")
#         self.chars.addWidget(self.chars_count)
#         self.selected_chars = QtWidgets.QLabel(self.chars_)
#         self.selected_chars.setObjectName("selected_chars")
#         self.chars.addWidget(self.selected_chars)
#         self.horizontalLayout_6.addWidget(self.chars_)
#         self.lines = QtWidgets.QFrame(self.status_bar_2)
#         self.lines.setObjectName("lines")
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lines)
#         self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_5.setSpacing(4)
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#         self.lines_label = QtWidgets.QLabel(self.lines)
#         self.lines_label.setObjectName("lines_label")
#         self.horizontalLayout_5.addWidget(self.lines_label)
#         self.count_lines = QtWidgets.QLabel(self.lines)
#         self.count_lines.setObjectName("count_lines")
#         self.horizontalLayout_5.addWidget(self.count_lines)
#         self.current_lines = QtWidgets.QLabel(self.lines)
#         self.current_lines.setObjectName("current_lines")
#         self.horizontalLayout_5.addWidget(self.current_lines)
#         self.horizontalLayout_6.addWidget(self.lines)
#         self.horizontalLayout_7.addWidget(self.status_bar_2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
#         self.verticalLayout_3.addWidget(self.status_text_field)
#         self.stackedWidget.addWidget(self.text_page)
#         self.page_2 = QtWidgets.QWidget()
#         self.page_2.setObjectName("page_2")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.label_2 = QtWidgets.QLabel(self.page_2)
#         self.label_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_2.setObjectName("label_2")
#         self.verticalLayout_4.addWidget(self.label_2)
#         self.stackedWidget.addWidget(self.page_2)
#         self.horizontalLayout_4.addWidget(self.stackedWidget)
#         self.tools_bar = QtWidgets.QFrame(self.content)
#         self.tools_bar.setMinimumSize(QtCore.QSize(175, 0))
#         self.tools_bar.setMaximumSize(QtCore.QSize(25, 16777215))
#         self.tools_bar.setStyleSheet("QFrame {\n"
#                                      "background-color: rgb(44, 52, 71);\n"
#                                      "border: none;\n"
#                                      "}\n"
#                                      "")
#         self.tools_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.tools_bar.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.tools_bar.setObjectName("tools_bar")
#         self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tools_bar)
#         self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_8.setSpacing(0)
#         self.verticalLayout_8.setObjectName("verticalLayout_8")
#         self.co_button_frame = QtWidgets.QFrame(self.tools_bar)
#         self.co_button_frame.setMinimumSize(QtCore.QSize(0, 25))
#         self.co_button_frame.setMaximumSize(QtCore.QSize(16777215, 25))
#         self.co_button_frame.setStyleSheet("QPushButton {\n"
#                                            "border: none;\n"
#                                            "border-radius: 2px;\n"
#                                            "background-color: rgb(44, 52, 71);\n"
#                                            "color: rgb(255, 255, 255);\n"
#                                            "font: 75 10pt \"Century Gothic\";\n"
#                                            "text-align:left;\n"
#                                            "}\n"
#                                            "QPushButton:hover {\n"
#                                            "background: rgba(86, 94, 110, 100);\n"
#                                            "} \n"
#                                            "QPushButton:pressed{\n"
#                                            "background: rgb(86, 94, 110, 150);\n"
#                                            "}\n"
#                                            "")
#         self.co_button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.co_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.co_button_frame.setObjectName("co_button_frame")
#         self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.co_button_frame)
#         self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
#         self.horizontalLayout_8.setSpacing(0)
#         self.horizontalLayout_8.setObjectName("horizontalLayout_8")
#         self.close_open_tools_bar_but = QtWidgets.QPushButton(self.co_button_frame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.close_open_tools_bar_but.sizePolicy().hasHeightForWidth())
#         self.close_open_tools_bar_but.setSizePolicy(sizePolicy)
#         self.close_open_tools_bar_but.setMinimumSize(QtCore.QSize(15, 15))
#         self.close_open_tools_bar_but.setMaximumSize(QtCore.QSize(15, 15))
#         self.close_open_tools_bar_but.setStyleSheet("")
#         self.close_open_tools_bar_but.setText("")
#         icon5 = QtGui.QIcon()
#         icon5.addPixmap(QtGui.QPixmap(":/icons/images/arrow_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.close_open_tools_bar_but.setIcon(icon5)
#         self.close_open_tools_bar_but.setIconSize(QtCore.QSize(15, 15))
#         self.close_open_tools_bar_but.setObjectName("close_open_tools_bar_but")
#         self.horizontalLayout_8.addWidget(self.close_open_tools_bar_but)
#         self.verticalLayout_8.addWidget(self.co_button_frame, 0, QtCore.Qt.AlignLeft)
#         self.tools_frame = QtWidgets.QFrame(self.tools_bar)
#         self.tools_frame.setMinimumSize(QtCore.QSize(175, 0))
#         self.tools_frame.setMaximumSize(QtCore.QSize(175, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.tools_frame.setFont(font)
#         self.tools_frame.setStyleSheet("QCheckBox {\n"
#                                        "color: white;\n"
#                                        "}\n"
#                                        "QCheckBox:indicator{\n"
#                                        "background-color: rgb(176, 196, 222, 120);\n"
#                                        "border-radius: 3px;\n"
#                                        "width: 15px;\n"
#                                        "height: 15px;\n"
#                                        "}\n"
#                                        "QCheckBox:indicator:hover {\n"
#                                        "background-color: rgb(176, 196, 222, 200);\n"
#                                        "}\n"
#                                        "QCheckBox:indicator:checked {\n"
#                                        "border-image: url(:/icons/images/checked.png);\n"
#                                        "}\n"
#                                        "\n"
#                                        "QSlider::groove:horizontal {\n"
#                                        "height: 3px; \n"
#                                        "background-color: rgb(176, 196, 222, 180);\n"
#                                        "border-radius: 1px;\n"
#                                        "}\n"
#                                        "QSlider::handle:horizontal {\n"
#                                        "background-color: rgb(176, 196, 222);\n"
#                                        "width:10px;\n"
#                                        "margin-top: -3px;\n"
#                                        "margin-bottom: -3px;\n"
#                                        "border-radius: 4px;\n"
#                                        "}\n"
#                                        "\n"
#                                        "QLabel{\n"
#                                        "color:white;\n"
#                                        "}\n"
#                                        "\n"
#                                        "QLineEdit{\n"
#                                        "color: white;\n"
#                                        "padding:2px;\n"
#                                        "border: none;\n"
#                                        "border-radius: 5px;\n"
#                                        "background-color: rgb(176, 196, 222, 120);\n"
#                                        "}\n"
#                                        "\n"
#                                        "")
#         self.tools_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.tools_frame.setObjectName("tools_frame")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tools_frame)
#         self.verticalLayout_7.setContentsMargins(25, 25, 25, -1)
#         self.verticalLayout_7.setSpacing(20)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.findword_line = QtWidgets.QLineEdit(self.tools_frame)
#         self.findword_line.setMinimumSize(QtCore.QSize(125, 24))
#         self.findword_line.setMaximumSize(QtCore.QSize(125, 24))
#         font = QtGui.QFont()
#         font.setFamily("Trebuchet MS")
#         font.setPointSize(10)
#         self.findword_line.setFont(font)
#         self.findword_line.setObjectName("findword_line")
#         self.verticalLayout_7.addWidget(self.findword_line)
#         self.font_size_frame = QtWidgets.QFrame(self.tools_frame)
#         self.font_size_frame.setStyleSheet("QSpinBox{\n"
#                                            "color: white;\n"
#                                            "padding:2px;\n"
#                                            "border: none;\n"
#                                            "border-radius: 4px;\n"
#                                            "background-color: rgb(176, 196, 222, 120);\n"
#                                            "}")
#         self.font_size_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.font_size_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.font_size_frame.setObjectName("font_size_frame")
#         self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.font_size_frame)
#         self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_9.setObjectName("horizontalLayout_9")
#         self.font_size_label = QtWidgets.QLabel(self.font_size_frame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.font_size_label.sizePolicy().hasHeightForWidth())
#         self.font_size_label.setSizePolicy(sizePolicy)
#         self.font_size_label.setMinimumSize(QtCore.QSize(61, 10))
#         self.font_size_label.setMaximumSize(QtCore.QSize(61, 10))
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.font_size_label.setFont(font)
#         self.font_size_label.setObjectName("font_size_label")
#         self.horizontalLayout_9.addWidget(self.font_size_label)
#         self.font_spin_box = QtWidgets.QSpinBox(self.font_size_frame)
#         self.font_spin_box.setAlignment(QtCore.Qt.AlignCenter)
#         self.font_spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.font_spin_box.setSpecialValueText("")
#         self.font_spin_box.setMinimum(10)
#         self.font_spin_box.setMaximum(72)
#         self.font_spin_box.setProperty("value", 12)
#         self.font_spin_box.setObjectName("font_spin_box")
#         self.horizontalLayout_9.addWidget(self.font_spin_box)
#         self.verticalLayout_7.addWidget(self.font_size_frame)
#         self.font_style_frame = QtWidgets.QFrame(self.tools_frame)
#         self.font_style_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.font_style_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.font_style_frame.setObjectName("font_style_frame")
#         self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.font_style_frame)
#         self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_9.setSpacing(6)
#         self.verticalLayout_9.setObjectName("verticalLayout_9")
#         self.underline_check_box = QtWidgets.QCheckBox(self.font_style_frame)
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.underline_check_box.setFont(font)
#         self.underline_check_box.setObjectName("underline_check_box")
#         self.verticalLayout_9.addWidget(self.underline_check_box)
#         self.italic_check_box = QtWidgets.QCheckBox(self.font_style_frame)
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.italic_check_box.setFont(font)
#         self.italic_check_box.setObjectName("italic_check_box")
#         self.verticalLayout_9.addWidget(self.italic_check_box)
#         self.bold_check_box = QtWidgets.QCheckBox(self.font_style_frame)
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.bold_check_box.setFont(font)
#         self.bold_check_box.setObjectName("bold_check_box")
#         self.verticalLayout_9.addWidget(self.bold_check_box)
#         self.verticalLayout_7.addWidget(self.font_style_frame)
#         self.verticalLayout_8.addWidget(self.tools_frame)
#         spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.verticalLayout_8.addItem(spacerItem2)
#         self.file_frame = QtWidgets.QFrame(self.tools_bar)
#         self.file_frame.setMinimumSize(QtCore.QSize(175, 0))
#         self.file_frame.setMaximumSize(QtCore.QSize(175, 16777215))
#         self.file_frame.setStyleSheet("QPushButton{\n"
#                                       "border: none;\n"
#                                       "border-radius:10px;\n"
#                                       "padding:5px;\n"
#                                       "color:white;\n"
#                                       "background-color:rgba(64, 73, 89, 180);\n"
#                                       "}\n"
#                                       "QPushButton:hover{\n"
#                                       "background-color: rgb(86, 94, 110, 100);\n"
#                                       "}\n"
#                                       "QPushButton:hover:pressed{\n"
#                                       "background: rgb(86, 94, 110, 150);\n"
#                                       "}")
#         self.file_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.file_frame.setObjectName("file_frame")
#         self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.file_frame)
#         self.verticalLayout_10.setContentsMargins(40, 12, 40, 12)
#         self.verticalLayout_10.setObjectName("verticalLayout_10")
#         self.save_button = QtWidgets.QPushButton(self.file_frame)
#         self.save_button.setMinimumSize(QtCore.QSize(0, 0))
#         self.save_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.save_button.setFont(font)
#         self.save_button.setObjectName("save_button")
#         self.verticalLayout_10.addWidget(self.save_button)
#         self.open_button = QtWidgets.QPushButton(self.file_frame)
#         self.open_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.open_button.setFont(font)
#         self.open_button.setObjectName("open_button")
#         self.verticalLayout_10.addWidget(self.open_button)
#         self.new_button = QtWidgets.QPushButton(self.file_frame)
#         self.new_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Century Gothic")
#         font.setPointSize(10)
#         self.new_button.setFont(font)
#         self.new_button.setObjectName("new_button")
#         self.verticalLayout_10.addWidget(self.new_button)
#         self.verticalLayout_8.addWidget(self.file_frame)
#         self.horizontalLayout_4.addWidget(self.tools_bar)
#         self.verticalLayout_2.addWidget(self.content)
#         MainWindow.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(MainWindow)
#         self.stackedWidget.setCurrentIndex(0)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.name_window.setText(_translate("MainWindow", "Application"))
#         self.status_text.setText(_translate("MainWindow", "File name"))
#         self.page_name.setText(_translate("MainWindow", "| Text Field"))
#         self.home_button.setText(_translate("MainWindow", "Home Page"))
#         self.settings_button.setText(_translate("MainWindow", "Settings"))
#         self.account_button_2.setText(_translate("MainWindow", "KP"))
#         self.text_field.setPlaceholderText(_translate("MainWindow", "Write here"))
#         self.words_label.setText(_translate("MainWindow", "words:"))
#         self.words_count.setText(_translate("MainWindow", "0"))
#         self.chars_label.setText(_translate("MainWindow", "chars:"))
#         self.chars_count.setText(_translate("MainWindow", "0,"))
#         self.selected_chars.setText(_translate("MainWindow", "0"))
#         self.lines_label.setText(_translate("MainWindow", "lines:"))
#         self.count_lines.setText(_translate("MainWindow", "1,"))
#         self.current_lines.setText(_translate("MainWindow", "1"))
#         self.label_2.setText(_translate("MainWindow", "Page 2"))
#         self.findword_line.setPlaceholderText(_translate("MainWindow", "Find word"))
#         self.font_size_label.setText(_translate("MainWindow", "Font size:"))
#         self.underline_check_box.setText(_translate("MainWindow", "Underline"))
#         self.italic_check_box.setText(_translate("MainWindow", "Italic"))
#         self.bold_check_box.setText(_translate("MainWindow", "Bold"))
#         self.save_button.setText(_translate("MainWindow", "Save"))
#         self.open_button.setText(_translate("MainWindow", "Open"))
#         self.new_button.setText(_translate("MainWindow", "New"))
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
