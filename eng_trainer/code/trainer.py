from PyQt5 import QtCore, QtGui, QtWidgets
import source


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1253, 815)
        MainWindow.setStyleSheet("QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:handle:vertical {\n"
                                 "background-color: rgb(145, 109, 161);\n"
                                 "height: 15px;\n"
                                 "border-radius:3px;\n"
                                 "}\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:handle:vertical:hover {\n"
                                 "background-color: rgb(170, 132, 186, 200);\n"
                                 "}\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:handle:vertical:pressed {\n"
                                 "background-color: rgb(170, 132, 186, 250);\n"
                                 "}\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words  QScrollBar:sub-line:vertical,\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:add-line:vertical {\n"
                                 "background: none;\n"
                                 "}\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:vertical {\n"
                                 "border: none;\n"
                                 "border-radius: 12px;\n"
                                 "width: 8px;\n"
                                 "background-color: rgb(176, 196, 222);\n"
                                 "}\n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:add-page:vertical, \n"
                                 "QFrame#is_loaded_menu QPlainTextEdit#list_of_words QScrollBar:sub-page:vertical {\n"
                                 "background-color:  rgb(73, 58, 79);\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 25))
        self.title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.title.setStyleSheet("QFrame{\n"
                                 "background: rgb(24, 22, 26);\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "color: white;\n"
                                 "}")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttons = QtWidgets.QFrame(self.title)
        self.buttons.setMinimumSize(QtCore.QSize(75, 25))
        self.buttons.setMaximumSize(QtCore.QSize(75, 25))
        self.buttons.setStyleSheet("QPushButton {\n"
                                   "background: rgb(24, 22, 26);\n"
                                   "border: none;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(122, 122, 122, 125);\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background-color: rgb(122, 122, 122, 200);\n"
                                   "}\n"
                                   "QPushButton#close_button:hover {\n"
                                   "background-color: rgb(242, 80, 80, 200);\n"
                                   "}\n"
                                   "")
        self.buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hide_button = QtWidgets.QPushButton(self.buttons)
        self.hide_button.setMinimumSize(QtCore.QSize(25, 25))
        self.hide_button.setMaximumSize(QtCore.QSize(25, 25))
        self.hide_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/hide1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_button.setIcon(icon)
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout.addWidget(self.hide_button)
        self.full_button = QtWidgets.QPushButton(self.buttons)
        self.full_button.setMinimumSize(QtCore.QSize(25, 25))
        self.full_button.setMaximumSize(QtCore.QSize(25, 25))
        self.full_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/full1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full_button.setIcon(icon1)
        self.full_button.setObjectName("full_button")
        self.horizontalLayout.addWidget(self.full_button)
        self.close_button = QtWidgets.QPushButton(self.buttons)
        self.close_button.setMinimumSize(QtCore.QSize(25, 25))
        self.close_button.setMaximumSize(QtCore.QSize(25, 25))
        self.close_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.horizontalLayout_2.addWidget(self.buttons)
        self.verticalLayout.addWidget(self.title)
        self.mainPages = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainPages.setStyleSheet("")
        self.mainPages.setObjectName("mainPages")
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setStyleSheet("QWidget#StartPage{\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 43, 79, 255), stop:1 rgba(91, 45, 100, 255));\n"
                                     "background-image:url(:/icons/icons/fon8.png);\n"
                                     "}\n"
                                     "QLabel#programLabel{\n"
                                     "color: white;\n"
                                     "}\n"
                                     "")
        self.StartPage.setObjectName("StartPage")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.StartPage)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(412, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.settings = QtWidgets.QStackedWidget(self.StartPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QtCore.QSize(0, 0))
        self.settings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settings.setStyleSheet("QWidget{\n"
                                    "background: rgb(70, 54, 77, 150);\n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "color: white;\n"
                                    "background: rgb(145, 109, 161);\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background: rgb(170, 132, 186, 200);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background: rgb(170, 132, 186, 250);\n"
                                    "}")
        self.settings.setObjectName("settings")
        self.not_loaded = QtWidgets.QWidget()
        self.not_loaded.setStyleSheet("")
        self.not_loaded.setObjectName("not_loaded")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.not_loaded)
        self.verticalLayout_5.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.not_loaded_text_frame = QtWidgets.QFrame(self.not_loaded)
        self.not_loaded_text_frame.setMinimumSize(QtCore.QSize(500, 0))
        self.not_loaded_text_frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.not_loaded_text_frame.setStyleSheet("QFrame{\n"
                                                 "background: rgb(100, 78, 110);\n"
                                                 "border-radius: 10px;\n"
                                                 "}\n"
                                                 "QLabel{\n"
                                                 "color:white;\n"
                                                 "}\n"
                                                 "QLabel#not_loaded_text{\n"
                                                 "border-radius: 5px;\n"
                                                 "background: rgb(73, 58, 79);\n"
                                                 "padding: 10px;\n"
                                                 "}")
        self.not_loaded_text_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.not_loaded_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.not_loaded_text_frame.setObjectName("not_loaded_text_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.not_loaded_text_frame)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.programTitle = QtWidgets.QLabel(self.not_loaded_text_frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(24)
        self.programTitle.setFont(font)
        self.programTitle.setTabletTracking(False)
        self.programTitle.setStyleSheet("")
        self.programTitle.setObjectName("programTitle")
        self.verticalLayout_4.addWidget(self.programTitle)
        self.not_loaded_text = QtWidgets.QLabel(self.not_loaded_text_frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.not_loaded_text.setFont(font)
        self.not_loaded_text.setStyleSheet("")
        self.not_loaded_text.setTextFormat(QtCore.Qt.PlainText)
        self.not_loaded_text.setScaledContents(False)
        self.not_loaded_text.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.not_loaded_text.setWordWrap(True)
        self.not_loaded_text.setObjectName("not_loaded_text")
        self.verticalLayout_4.addWidget(self.not_loaded_text)
        self.verticalLayout_5.addWidget(self.not_loaded_text_frame, 0, QtCore.Qt.AlignHCenter)
        self.loadButton = QtWidgets.QPushButton(self.not_loaded)
        self.loadButton.setMinimumSize(QtCore.QSize(110, 30))
        self.loadButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout_5.addWidget(self.loadButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.settings.addWidget(self.not_loaded)
        self.is_loaded = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_loaded.sizePolicy().hasHeightForWidth())
        self.is_loaded.setSizePolicy(sizePolicy)
        self.is_loaded.setStyleSheet("")
        self.is_loaded.setObjectName("is_loaded")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.is_loaded)
        self.verticalLayout_21.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_21.setSpacing(20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem4 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem4)
        self.settingsMainFrame = QtWidgets.QFrame(self.is_loaded)
        self.settingsMainFrame.setMinimumSize(QtCore.QSize(500, 0))
        self.settingsMainFrame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.settingsMainFrame.setStyleSheet("QFrame{\n"
                                             "background:none;\n"
                                             "}")
        self.settingsMainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsMainFrame.setObjectName("settingsMainFrame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.settingsMainFrame)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.settingsAndLoadedMenuFrame = QtWidgets.QFrame(self.settingsMainFrame)
        self.settingsAndLoadedMenuFrame.setMinimumSize(QtCore.QSize(1020, 0))
        self.settingsAndLoadedMenuFrame.setMaximumSize(QtCore.QSize(1020, 16777215))
        self.settingsAndLoadedMenuFrame.setStyleSheet("QFrame{\n"
                                                      "background: none;\n"
                                                      "}")
        self.settingsAndLoadedMenuFrame.setObjectName("settingsAndLoadedMenuFrame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.settingsAndLoadedMenuFrame)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.is_loaded_menu = QtWidgets.QFrame(self.settingsAndLoadedMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_loaded_menu.sizePolicy().hasHeightForWidth())
        self.is_loaded_menu.setSizePolicy(sizePolicy)
        self.is_loaded_menu.setMinimumSize(QtCore.QSize(500, 600))
        self.is_loaded_menu.setMaximumSize(QtCore.QSize(500, 16777215))
        self.is_loaded_menu.setStyleSheet("QFrame{\n"
                                          "background: rgb(100, 78, 110);\n"
                                          "border-radius: 10px;\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "color: white;\n"
                                          "}\n"
                                          "QPlainTextEdit{\n"
                                          "border-radius: 5px;\n"
                                          "background: rgb(73, 58, 79);\n"
                                          "padding: 7px;\n"
                                          "padding-left:5px;\n"
                                          "color: white;\n"
                                          "}")
        self.is_loaded_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.is_loaded_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.is_loaded_menu.setObjectName("is_loaded_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.is_loaded_menu)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.is_loaded_title_frame = QtWidgets.QFrame(self.is_loaded_menu)
        self.is_loaded_title_frame.setStyleSheet("")
        self.is_loaded_title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.is_loaded_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.is_loaded_title_frame.setObjectName("is_loaded_title_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.is_loaded_title_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.words_are_loaded = QtWidgets.QLabel(self.is_loaded_title_frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(24)
        self.words_are_loaded.setFont(font)
        self.words_are_loaded.setLineWidth(-1)
        self.words_are_loaded.setObjectName("words_are_loaded")
        self.horizontalLayout_3.addWidget(self.words_are_loaded)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.is_loaded_title_frame)
        self.list_of_words = QtWidgets.QPlainTextEdit(self.is_loaded_menu)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.list_of_words.setFont(font)
        self.list_of_words.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.list_of_words.setReadOnly(True)
        self.list_of_words.setPlainText("")
        self.list_of_words.setObjectName("list_of_words")
        self.verticalLayout_2.addWidget(self.list_of_words)
        self.horizontalLayout_16.addWidget(self.is_loaded_menu)
        self.settingsFrame = QtWidgets.QFrame(self.settingsAndLoadedMenuFrame)
        self.settingsFrame.setMinimumSize(QtCore.QSize(500, 0))
        self.settingsFrame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.settingsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsFrame.setObjectName("settingsFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.settingsFrame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.settings_menu = QtWidgets.QFrame(self.settingsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_menu.sizePolicy().hasHeightForWidth())
        self.settings_menu.setSizePolicy(sizePolicy)
        self.settings_menu.setMinimumSize(QtCore.QSize(500, 600))
        self.settings_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settings_menu.setStyleSheet("QFrame{\n"
                                         "background: rgb(100, 78, 110);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel{\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox {\n"
                                         "color: white;\n"
                                         "background:none;\n"
                                         "}\n"
                                         "QCheckBox:indicator{\n"
                                         "background-color: rgb(73, 58, 79, 150);\n"
                                         "border-radius: 3px;\n"
                                         "width: 14px;\n"
                                         "height: 14px;\n"
                                         "}\n"
                                         "QCheckBox:indicator:hover {\n"
                                         "background-color: rgb(73, 58, 79, 200);\n"
                                         "}\n"
                                         "QCheckBox:indicator:checked {\n"
                                         "border-image: url(:/icons/icons/checked.png);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox{\n"
                                         "background: rgb(73, 58, 79, 150);\n"
                                         "border-radius: 5px;\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPlainTextEdit{\n"
                                         "border-radius: 5px;\n"
                                         "background: rgb(73, 58, 79);\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "Line{\n"
                                         "background: rgb(145, 109, 161);\n"
                                         "}")
        self.settings_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settings_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_menu.setObjectName("settings_menu")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.settings_menu)
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_20.setSpacing(20)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.settingsTitleFrame = QtWidgets.QFrame(self.settings_menu)
        self.settingsTitleFrame.setStyleSheet("")
        self.settingsTitleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsTitleFrame.setObjectName("settingsTitleFrame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.settingsTitleFrame)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.settingsTitle = QtWidgets.QLabel(self.settingsTitleFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(24)
        self.settingsTitle.setFont(font)
        self.settingsTitle.setLineWidth(-1)
        self.settingsTitle.setObjectName("settingsTitle")
        self.horizontalLayout_15.addWidget(self.settingsTitle)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.verticalLayout_20.addWidget(self.settingsTitleFrame)
        self.settingsSubFrame = QtWidgets.QFrame(self.settings_menu)
        self.settingsSubFrame.setStyleSheet("QFrame{\n"
                                            "border-radius: 0px;\n"
                                            "}")
        self.settingsSubFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsSubFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsSubFrame.setObjectName("settingsSubFrame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.settingsSubFrame)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.autoSetMainFrame = QtWidgets.QFrame(self.settingsSubFrame)
        self.autoSetMainFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.autoSetMainFrame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.autoSetMainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.autoSetMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoSetMainFrame.setObjectName("autoSetMainFrame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.autoSetMainFrame)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame = QtWidgets.QFrame(self.autoSetMainFrame)
        self.frame.setMinimumSize(QtCore.QSize(0, 79))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 79))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.autoSetFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoSetFrame.sizePolicy().hasHeightForWidth())
        self.autoSetFrame.setSizePolicy(sizePolicy)
        self.autoSetFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.autoSetFrame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.autoSetFrame.setStyleSheet("QFrame{\n"
                                        "border-radius: 0px;\n"
                                        "margin:0px;\n"
                                        "}\n"
                                        "QPushButton{\n"
                                        "background:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "image: url(:/icons/icons/question1_hover.png);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "image: url(:/icons/icons/question1_pressed.png);\n"
                                        "}")
        self.autoSetFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.autoSetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoSetFrame.setObjectName("autoSetFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.autoSetFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.autoSetcheckBox = QtWidgets.QCheckBox(self.autoSetFrame)
        self.autoSetcheckBox.setMinimumSize(QtCore.QSize(15, 15))
        self.autoSetcheckBox.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.autoSetcheckBox.setFont(font)
        self.autoSetcheckBox.setChecked(True)
        self.autoSetcheckBox.setObjectName("autoSetcheckBox")
        self.horizontalLayout_4.addWidget(self.autoSetcheckBox)
        self.question_button = QtWidgets.QPushButton(self.autoSetFrame)
        self.question_button.setMinimumSize(QtCore.QSize(20, 20))
        self.question_button.setMaximumSize(QtCore.QSize(20, 20))
        self.question_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/question1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/question1.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/question1.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/question1.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.question_button.setIcon(icon3)
        self.question_button.setIconSize(QtCore.QSize(18, 18))
        self.question_button.setObjectName("question_button")
        self.horizontalLayout_4.addWidget(self.question_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_14.addWidget(self.autoSetFrame)
        self.questionFrame2 = QtWidgets.QFrame(self.frame)
        self.questionFrame2.setMinimumSize(QtCore.QSize(0, 60))
        self.questionFrame2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.questionFrame2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.questionFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.questionFrame2.setObjectName("questionFrame2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.questionFrame2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.questionFrame = QtWidgets.QFrame(self.questionFrame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionFrame.sizePolicy().hasHeightForWidth())
        self.questionFrame.setSizePolicy(sizePolicy)
        self.questionFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.questionFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.questionFrame.setStyleSheet("QFrame{\n"
                                         "background: rgb(73, 58, 79);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "")
        self.questionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.questionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.questionFrame.setObjectName("questionFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.questionFrame)
        self.verticalLayout_13.setContentsMargins(10, 5, 5, 5)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.questionLabel = QtWidgets.QLabel(self.questionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionLabel.sizePolicy().hasHeightForWidth())
        self.questionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.questionLabel.setFont(font)
        self.questionLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout_13.addWidget(self.questionLabel)
        self.verticalLayout_3.addWidget(self.questionFrame)
        self.verticalLayout_14.addWidget(self.questionFrame2)
        self.verticalLayout_15.addWidget(self.frame)
        self.verticalLayout_19.addWidget(self.autoSetMainFrame)
        self.settingsScrollArea = QtWidgets.QScrollArea(self.settingsSubFrame)
        self.settingsScrollArea.setStyleSheet("QAbstractScrollArea {\n"
                                              "background: rgb(73, 58, 79);\n"
                                              "border: 1px solid rgb(73, 58, 79);\n"
                                              "border-radius: 5px;\n"
                                              "padding: 2px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:add-line:vertical {\n"
                                              "margin: 0px 0px 0px 0px;\n"
                                              "height: 0px;\n"
                                              "width: 0px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:sub-line:vertical {\n"
                                              "margin: 0px 0px 0px 0px;\n"
                                              "height: 5px;\n"
                                              "width: 0px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:vertical {\n"
                                              "background: rgb(73, 58, 79);\n"
                                              "width: 12px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:handle:vertical {\n"
                                              "margin-bottom: 4px;\n"
                                              "margin-top: 4px;\n"
                                              "background-color: rgb(145, 109, 161);\n"
                                              "border-radius: 3px;\n"
                                              "margin-right: 4px;\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:handle:vertical:hover {\n"
                                              "background-color: rgb(170, 132, 186, 200);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar:handle:vertical:pressed {\n"
                                              "background-color: rgb(170, 132, 186, 250);\n"
                                              "}\n"
                                              "\n"
                                              "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                              "background: rgb(73, 58, 79);\n"
                                              "}\n"
                                              "")
        self.settingsScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.settingsScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.settingsScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settingsScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.settingsScrollArea.setObjectName("settingsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 464, 469))
        self.scrollAreaWidgetContents.setStyleSheet("QFrame{\n"
                                                    "padding: 0px;\n"
                                                    "margin:0px;\n"
                                                    "}\n"
                                                    "QWidget{\n"
                                                    "background: rgb(100, 78, 110);\n"
                                                    "}\n"
                                                    "\n"
                                                    "")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.userSettings = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.userSettings.setStyleSheet("QFrame{\n"
                                        "background: rgb(73, 58, 79);\n"
                                        "}\n"
                                        "QSpinBox{\n"
                                        "background: rgb(104, 77, 115);\n"
                                        "border-radius: 5px;\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QLabel{\n"
                                        "border-radius: none;\n"
                                        "}")
        self.userSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.userSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userSettings.setObjectName("userSettings")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.userSettings)
        self.verticalLayout_22.setContentsMargins(7, 6, 6, 7)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.userCommonSettingsFrame = QtWidgets.QFrame(self.userSettings)
        self.userCommonSettingsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.userCommonSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userCommonSettingsFrame.setObjectName("userCommonSettingsFrame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.userCommonSettingsFrame)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.numWordsFrame = QtWidgets.QFrame(self.userCommonSettingsFrame)
        self.numWordsFrame.setObjectName("numWordsFrame")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.numWordsFrame)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.amountUserLabel = QtWidgets.QLabel(self.numWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.amountUserLabel.setFont(font)
        self.amountUserLabel.setObjectName("amountUserLabel")
        self.horizontalLayout_17.addWidget(self.amountUserLabel)
        self.spinBoxAmountWords = QtWidgets.QSpinBox(self.numWordsFrame)
        self.spinBoxAmountWords.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.spinBoxAmountWords.setFont(font)
        self.spinBoxAmountWords.setStyleSheet("")
        self.spinBoxAmountWords.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxAmountWords.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxAmountWords.setMinimum(1)
        self.spinBoxAmountWords.setObjectName("spinBoxAmountWords")
        self.horizontalLayout_17.addWidget(self.spinBoxAmountWords)
        self.amountUserWord = QtWidgets.QLabel(self.numWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.amountUserWord.setFont(font)
        self.amountUserWord.setObjectName("amountUserWord")
        self.horizontalLayout_17.addWidget(self.amountUserWord)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.verticalLayout_17.addWidget(self.numWordsFrame)
        self.numVarFrame = QtWidgets.QFrame(self.userCommonSettingsFrame)
        self.numVarFrame.setObjectName("numVarFrame")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.numVarFrame)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.amountVarLabel = QtWidgets.QLabel(self.numVarFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.amountVarLabel.setFont(font)
        self.amountVarLabel.setObjectName("amountVarLabel")
        self.horizontalLayout_18.addWidget(self.amountVarLabel)
        self.spinBoxAmountVar = QtWidgets.QSpinBox(self.numVarFrame)
        self.spinBoxAmountVar.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.spinBoxAmountVar.setFont(font)
        self.spinBoxAmountVar.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxAmountVar.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxAmountVar.setMinimum(1)
        self.spinBoxAmountVar.setProperty("value", 4)
        self.spinBoxAmountVar.setObjectName("spinBoxAmountVar")
        self.horizontalLayout_18.addWidget(self.spinBoxAmountVar)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.verticalLayout_17.addWidget(self.numVarFrame)
        self.userTimeFrame = QtWidgets.QFrame(self.userCommonSettingsFrame)
        self.userTimeFrame.setObjectName("userTimeFrame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.userTimeFrame)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.userTimeLabel = QtWidgets.QLabel(self.userTimeFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.userTimeLabel.setFont(font)
        self.userTimeLabel.setObjectName("userTimeLabel")
        self.horizontalLayout_19.addWidget(self.userTimeLabel)
        self.userTimeSpinBox = QtWidgets.QSpinBox(self.userTimeFrame)
        self.userTimeSpinBox.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.userTimeSpinBox.setFont(font)
        self.userTimeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.userTimeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.userTimeSpinBox.setObjectName("userTimeSpinBox")
        self.horizontalLayout_19.addWidget(self.userTimeSpinBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.verticalLayout_17.addWidget(self.userTimeFrame)
        self.verticalLayout_22.addWidget(self.userCommonSettingsFrame)
        self.tableFrame = QtWidgets.QFrame(self.userSettings)
        self.tableFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableFrame.setObjectName("tableFrame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tableFrame)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.tableWidget = QtWidgets.QTableWidget(self.tableFrame)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QFrame{\n"
                                       "padding: 0px;\n"
                                       "margin: 0px;\n"
                                       "}\n"
                                       "QTableWidget {\n"
                                       "color: white;\n"
                                       "background: rgb(73, 58, 79);\n"
                                       "}\n"
                                       "QTableWidget::item {\n"
                                       "selection-background: rgb(104, 77, 115);\n"
                                       "color: white;\n"
                                       "margin: 1px;\n"
                                       "border-radius: 4px;\n"
                                       "background: rgb(104, 77, 115, 175);\n"
                                       "padding-left: 4px;\n"
                                       "}\n"
                                       "QTableWidget::item:hover {\n"
                                       "background: rgb(104, 77, 115, 225);\n"
                                       "}\n"
                                       "QTableWidget QLineEdit {\n"
                                       "background-color: rgb(104, 77, 115);\n"
                                       "border: 0px;\n"
                                       "border-radius: 4px;\n"
                                       "color: white;\n"
                                       "}\n"
                                       "QHeaderView:section{\n"
                                       "border-radius: 4px;\n"
                                       "margin:1px;\n"
                                       "border: none;\n"
                                       "background: rgb(51, 39, 56);\n"
                                       "color: white;\n"
                                       "font-family: \"Yu Gothic UI Semilight\";\n"
                                       "font-size: 18px;\n"
                                       "}\n"
                                       "QHeaderView {\n"
                                       "border: 0px;\n"
                                       "}")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(224)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_18.addWidget(self.tableWidget)
        self.errorLabelFrame = QtWidgets.QFrame(self.tableFrame)
        self.errorLabelFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.errorLabelFrame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.errorLabelFrame.setBaseSize(QtCore.QSize(0, 0))
        self.errorLabelFrame.setStyleSheet("QLabel{\n"
                                           "color: rgb(237, 38, 38);\n"
                                           "}")
        self.errorLabelFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.errorLabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorLabelFrame.setObjectName("errorLabelFrame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.errorLabelFrame)
        self.verticalLayout_24.setContentsMargins(0, 0, 2, 10)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.errorLabel = QtWidgets.QLabel(self.errorLabelFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_24.addWidget(self.errorLabel)
        self.verticalLayout_18.addWidget(self.errorLabelFrame, 0, QtCore.Qt.AlignRight)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem11)
        self.verticalLayout_22.addWidget(self.tableFrame)
        self.applyButtonFrame = QtWidgets.QFrame(self.userSettings)
        self.applyButtonFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.applyButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.applyButtonFrame.setObjectName("applyButtonFrame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.applyButtonFrame)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.applyButton = QtWidgets.QPushButton(self.applyButtonFrame)
        self.applyButton.setMinimumSize(QtCore.QSize(110, 0))
        self.applyButton.setSizeIncrement(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet("QPushButton{\n"
                                       "color: white;\n"
                                       "background: rgb(145, 109, 161);\n"
                                       "border-radius: 10px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background: rgb(170, 132, 186, 200);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "background: rgb(170, 132, 186, 250);\n"
                                       "}")
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_20.addWidget(self.applyButton)
        self.verticalLayout_22.addWidget(self.applyButtonFrame)
        self.verticalLayout_16.addWidget(self.userSettings)
        self.settingsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_19.addWidget(self.settingsScrollArea)
        self.verticalLayout_20.addWidget(self.settingsSubFrame)
        self.horizontalLayout_14.addWidget(self.settings_menu)
        self.horizontalLayout_16.addWidget(self.settingsFrame)
        self.verticalLayout_12.addWidget(self.settingsAndLoadedMenuFrame)
        self.verticalLayout_21.addWidget(self.settingsMainFrame, 0, QtCore.Qt.AlignHCenter)
        self.buttons_is_loaded_frame = QtWidgets.QFrame(self.is_loaded)
        self.buttons_is_loaded_frame.setStyleSheet("QFrame{\n"
                                                   "background:none;\n"
                                                   "}")
        self.buttons_is_loaded_frame.setObjectName("buttons_is_loaded_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.buttons_is_loaded_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.startButton = QtWidgets.QPushButton(self.buttons_is_loaded_frame)
        self.startButton.setMinimumSize(QtCore.QSize(110, 30))
        self.startButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_5.addWidget(self.startButton)
        self.loadButton_2 = QtWidgets.QPushButton(self.buttons_is_loaded_frame)
        self.loadButton_2.setMinimumSize(QtCore.QSize(110, 30))
        self.loadButton_2.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.loadButton_2.setFont(font)
        self.loadButton_2.setObjectName("loadButton_2")
        self.horizontalLayout_5.addWidget(self.loadButton_2)
        self.optionsButton = QtWidgets.QPushButton(self.buttons_is_loaded_frame)
        self.optionsButton.setMinimumSize(QtCore.QSize(110, 30))
        self.optionsButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.optionsButton.setFont(font)
        self.optionsButton.setObjectName("optionsButton")
        self.horizontalLayout_5.addWidget(self.optionsButton)
        self.verticalLayout_21.addWidget(self.buttons_is_loaded_frame, 0, QtCore.Qt.AlignHCenter)
        spacerItem13 = QtWidgets.QSpacerItem(20, 43, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem13)
        self.settings.addWidget(self.is_loaded)
        self.results = QtWidgets.QWidget()
        self.results.setStyleSheet("padding:0px;")
        self.results.setObjectName("results")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.results)
        self.verticalLayout_11.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem14 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem14)
        self.resultsFrame = QtWidgets.QFrame(self.results)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsFrame.sizePolicy().hasHeightForWidth())
        self.resultsFrame.setSizePolicy(sizePolicy)
        self.resultsFrame.setMinimumSize(QtCore.QSize(500, 700))
        self.resultsFrame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.resultsFrame.setStyleSheet("QFrame{\n"
                                        "background: rgb(100, 78, 110);\n"
                                        "border-radius: 10px;\n"
                                        "padding:0px;\n"
                                        "}\n"
                                        "QPlainTextEdit{\n"
                                        "border-radius: 5px;\n"
                                        "background: rgb(73, 58, 79);\n"
                                        "color: white;\n"
                                        "}")
        self.resultsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultsFrame.setObjectName("resultsFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.resultsFrame)
        self.verticalLayout_10.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.resultsTitleFrame = QtWidgets.QFrame(self.resultsFrame)
        self.resultsTitleFrame.setStyleSheet("QLabel{\n"
                                             "color:white;\n"
                                             "}")
        self.resultsTitleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultsTitleFrame.setObjectName("resultsTitleFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.resultsTitleFrame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.resultsTittle = QtWidgets.QLabel(self.resultsTitleFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(20)
        self.resultsTittle.setFont(font)
        self.resultsTittle.setLineWidth(-1)
        self.resultsTittle.setObjectName("resultsTittle")
        self.horizontalLayout_11.addWidget(self.resultsTittle)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.verticalLayout_10.addWidget(self.resultsTitleFrame, 0, QtCore.Qt.AlignTop)
        self.resultsScrollArea = QtWidgets.QScrollArea(self.resultsFrame)
        self.resultsScrollArea.setStyleSheet("QAbstractScrollArea {\n"
                                             "background: rgb(73, 58, 79);\n"
                                             "border: 1px solid rgb(73, 58, 79);\n"
                                             "border-radius: 5px;\n"
                                             "padding: 2px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:add-line:vertical {\n"
                                             "margin: 0px 0px 0px 0px;\n"
                                             "height: 0px;\n"
                                             "width: 0px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:sub-line:vertical {\n"
                                             "margin: 0px 0px 0px 0px;\n"
                                             "height: 5px;\n"
                                             "width: 0px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:vertical {\n"
                                             "background: rgb(88, 66, 99);\n"
                                             "width: 6px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical {\n"
                                             "background-color: rgb(145, 109, 161);\n"
                                             "border-radius: 3px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical:hover {\n"
                                             "background-color: rgb(170, 132, 186, 200);\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical:pressed {\n"
                                             "background-color: rgb(170, 132, 186, 250);\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                             "background: rgb(88, 66, 99);\n"
                                             "}\n"
                                             "")
        self.resultsScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsScrollArea.setWidgetResizable(True)
        self.resultsScrollArea.setObjectName("resultsScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 464, 607))
        self.scrollAreaWidgetContents_2.setStyleSheet("QFrame{\n"
                                                      "padding: 0px;\n"
                                                      "margin:0px;\n"
                                                      "}\n"
                                                      "QWidget{\n"
                                                      "background: rgb(100, 78, 110);\n"
                                                      "}\n"
                                                      "")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.resultsEndFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.resultsEndFrame.setStyleSheet("QFrame{\n"
                                           "background: rgb(73, 58, 79);\n"
                                           "border-radius: 0px;\n"
                                           "}\n"
                                           "QLabel{\n"
                                           "color: white;\n"
                                           "}\n"
                                           "QPlainTextEdit{\n"
                                           "border-radius: 5px;\n"
                                           "background: rgb(88, 66, 99);\n"
                                           "padding: 7px;\n"
                                           "padding-left:5px;\n"
                                           "color: white;\n"
                                           "}")
        self.resultsEndFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsEndFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultsEndFrame.setObjectName("resultsEndFrame")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.resultsEndFrame)
        self.verticalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_30.setSpacing(10)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.labelTimePass = QtWidgets.QLabel(self.resultsEndFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.labelTimePass.setFont(font)
        self.labelTimePass.setObjectName("labelTimePass")
        self.verticalLayout_30.addWidget(self.labelTimePass)
        self.labelAmountWords = QtWidgets.QLabel(self.resultsEndFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.labelAmountWords.setFont(font)
        self.labelAmountWords.setObjectName("labelAmountWords")
        self.verticalLayout_30.addWidget(self.labelAmountWords)
        self.wordsFrameRes = QtWidgets.QFrame(self.resultsEndFrame)
        self.wordsFrameRes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wordsFrameRes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wordsFrameRes.setObjectName("wordsFrameRes")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.wordsFrameRes)
        self.verticalLayout_29.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_29.setSpacing(15)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.errorFrameRes = QtWidgets.QFrame(self.wordsFrameRes)
        self.errorFrameRes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.errorFrameRes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorFrameRes.setObjectName("errorFrameRes")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.errorFrameRes)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.errorLabelRes = QtWidgets.QLabel(self.errorFrameRes)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.errorLabelRes.setFont(font)
        self.errorLabelRes.setObjectName("errorLabelRes")
        self.verticalLayout_28.addWidget(self.errorLabelRes)
        self.errorTextEdit = QtWidgets.QPlainTextEdit(self.errorFrameRes)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.errorTextEdit.setFont(font)
        self.errorTextEdit.setStyleSheet("")
        self.errorTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.errorTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.errorTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.errorTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.errorTextEdit.setReadOnly(True)
        self.errorTextEdit.setPlainText("")
        self.errorTextEdit.setObjectName("errorTextEdit")
        self.verticalLayout_28.addWidget(self.errorTextEdit)
        self.verticalLayout_29.addWidget(self.errorFrameRes)
        self.correctFrameRes = QtWidgets.QFrame(self.wordsFrameRes)
        self.correctFrameRes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.correctFrameRes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.correctFrameRes.setObjectName("correctFrameRes")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.correctFrameRes)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.correctLabelRes = QtWidgets.QLabel(self.correctFrameRes)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.correctLabelRes.setFont(font)
        self.correctLabelRes.setObjectName("correctLabelRes")
        self.verticalLayout_27.addWidget(self.correctLabelRes)
        self.correctTextEdit = QtWidgets.QPlainTextEdit(self.correctFrameRes)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.correctTextEdit.setFont(font)
        self.correctTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.correctTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.correctTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.correctTextEdit.setReadOnly(True)
        self.correctTextEdit.setPlainText("")
        self.correctTextEdit.setObjectName("correctTextEdit")
        self.verticalLayout_27.addWidget(self.correctTextEdit)
        self.verticalLayout_29.addWidget(self.correctFrameRes)
        self.verticalLayout_29.setStretch(0, 1)
        self.verticalLayout_29.setStretch(1, 1)
        self.verticalLayout_30.addWidget(self.wordsFrameRes)
        self.verticalLayout_26.addWidget(self.resultsEndFrame)
        self.resultsScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.addWidget(self.resultsScrollArea)
        self.verticalLayout_11.addWidget(self.resultsFrame, 0, QtCore.Qt.AlignHCenter)
        self.buttons_results_frame = QtWidgets.QFrame(self.results)
        self.buttons_results_frame.setStyleSheet("QFrame{\n"
                                                 "background:none;\n"
                                                 "}")
        self.buttons_results_frame.setObjectName("buttons_results_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.buttons_results_frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.menuButton = QtWidgets.QPushButton(self.buttons_results_frame)
        self.menuButton.setMinimumSize(QtCore.QSize(110, 30))
        self.menuButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.menuButton.setFont(font)
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_13.addWidget(self.menuButton)
        self.restartButton = QtWidgets.QPushButton(self.buttons_results_frame)
        self.restartButton.setMinimumSize(QtCore.QSize(110, 30))
        self.restartButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.restartButton.setFont(font)
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout_13.addWidget(self.restartButton)
        self.verticalLayout_11.addWidget(self.buttons_results_frame, 0, QtCore.Qt.AlignHCenter)
        spacerItem16 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem16)
        self.settings.addWidget(self.results)
        self.horizontalLayout_6.addWidget(self.settings)
        spacerItem17 = QtWidgets.QSpacerItem(412, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.mainPages.addWidget(self.StartPage)
        self.GamePage = QtWidgets.QWidget()
        self.GamePage.setObjectName("GamePage")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.GamePage)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sideBar = QtWidgets.QFrame(self.GamePage)
        self.sideBar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.sideBar.setStyleSheet("QFrame{\n"
                                   "background: rgb(42, 35, 48);\n"
                                   "}\n"
                                   "QLabel{\n"
                                   "color: white;\n"
                                   "}\n"
                                   "QPushButton{\n"
                                   "color: white;\n"
                                   "background: rgb(145, 109, 161);\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background: rgb(170, 132, 186, 200);\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background: rgb(170, 132, 186, 250);\n"
                                   "}\n"
                                   "")
        self.sideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBar.setObjectName("sideBar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.sideBar)
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.statsFrame = QtWidgets.QFrame(self.sideBar)
        self.statsFrame.setStyleSheet("Line{\n"
                                      "background: rgb(74, 63, 84);\n"
                                      "}")
        self.statsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statsFrame.setObjectName("statsFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.statsFrame)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_2 = QtWidgets.QFrame(self.statsFrame)
        self.line_2.setMinimumSize(QtCore.QSize(0, 2))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.TimeFrame = QtWidgets.QFrame(self.statsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.TimeFrame.setFont(font)
        self.TimeFrame.setObjectName("TimeFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.TimeFrame)
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.time1 = QtWidgets.QLabel(self.TimeFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.time1.setFont(font)
        self.time1.setObjectName("time1")
        self.horizontalLayout_7.addWidget(self.time1)
        self.time_num = QtWidgets.QLabel(self.TimeFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.time_num.setFont(font)
        self.time_num.setObjectName("time_num")
        self.horizontalLayout_7.addWidget(self.time_num)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.verticalLayout_6.addWidget(self.TimeFrame)
        self.wordsNumFrame = QtWidgets.QFrame(self.statsFrame)
        self.wordsNumFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wordsNumFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wordsNumFrame.setObjectName("wordsNumFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.wordsNumFrame)
        self.horizontalLayout_12.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.wordsNumTitle = QtWidgets.QLabel(self.wordsNumFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.wordsNumTitle.setFont(font)
        self.wordsNumTitle.setObjectName("wordsNumTitle")
        self.horizontalLayout_12.addWidget(self.wordsNumTitle)
        self.wordsNumAmount = QtWidgets.QLabel(self.wordsNumFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.wordsNumAmount.setFont(font)
        self.wordsNumAmount.setObjectName("wordsNumAmount")
        self.horizontalLayout_12.addWidget(self.wordsNumAmount)
        spacerItem19 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem19)
        self.verticalLayout_6.addWidget(self.wordsNumFrame)
        self.correctWordsFrame = QtWidgets.QFrame(self.statsFrame)
        self.correctWordsFrame.setObjectName("correctWordsFrame")
        self.correcr_words_frame = QtWidgets.QHBoxLayout(self.correctWordsFrame)
        self.correcr_words_frame.setContentsMargins(5, 0, 0, 0)
        self.correcr_words_frame.setSpacing(5)
        self.correcr_words_frame.setObjectName("correcr_words_frame")
        self.correct_words = QtWidgets.QLabel(self.correctWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.correct_words.setFont(font)
        self.correct_words.setObjectName("correct_words")
        self.correcr_words_frame.addWidget(self.correct_words)
        self.correct_words_num = QtWidgets.QLabel(self.correctWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.correct_words_num.setFont(font)
        self.correct_words_num.setObjectName("correct_words_num")
        self.correcr_words_frame.addWidget(self.correct_words_num)
        self.verticalLayout_6.addWidget(self.correctWordsFrame)
        self.invalidWordsFrame = QtWidgets.QFrame(self.statsFrame)
        self.invalidWordsFrame.setObjectName("invalidWordsFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.invalidWordsFrame)
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.invalid_label = QtWidgets.QLabel(self.invalidWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.invalid_label.setFont(font)
        self.invalid_label.setObjectName("invalid_label")
        self.horizontalLayout_8.addWidget(self.invalid_label)
        self.invalid_num = QtWidgets.QLabel(self.invalidWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.invalid_num.setFont(font)
        self.invalid_num.setObjectName("invalid_num")
        self.horizontalLayout_8.addWidget(self.invalid_num)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem20)
        self.verticalLayout_6.addWidget(self.invalidWordsFrame)
        self.line = QtWidgets.QFrame(self.statsFrame)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_7.addWidget(self.statsFrame)
        spacerItem21 = QtWidgets.QSpacerItem(20, 497, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem21)
        self.finishPushButton = QtWidgets.QPushButton(self.sideBar)
        self.finishPushButton.setMinimumSize(QtCore.QSize(110, 30))
        self.finishPushButton.setMaximumSize(QtCore.QSize(110, 30))
        self.finishPushButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.finishPushButton.setFont(font)
        self.finishPushButton.setObjectName("finishPushButton")
        self.verticalLayout_7.addWidget(self.finishPushButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addWidget(self.sideBar)
        self.mainBlock = QtWidgets.QFrame(self.GamePage)
        self.mainBlock.setStyleSheet("QFrame{\n"
                                     "background: rgb(47, 36, 54);\n"
                                     "background-image: url(:/icons/icons/fon_game.png);\n"
                                     "}\n"
                                     "QFrame#answersFrame, QFrame#wordNameFrame{\n"
                                     "background: rgb(33, 24, 38, 90);\n"
                                     "border-radius: 25px;\n"
                                     "}")
        self.mainBlock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBlock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBlock.setObjectName("mainBlock")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.mainBlock)
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.wordNameFrame = QtWidgets.QFrame(self.mainBlock)
        self.wordNameFrame.setMinimumSize(QtCore.QSize(0, 200))
        self.wordNameFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.wordNameFrame.setStyleSheet("QLabel{\n"
                                         "background: none;\n"
                                         "color: white;\n"
                                         "}")
        self.wordNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wordNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wordNameFrame.setObjectName("wordNameFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.wordNameFrame)
        self.horizontalLayout_10.setContentsMargins(35, 20, 20, 20)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wordName = QtWidgets.QLabel(self.wordNameFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(48)
        self.wordName.setFont(font)
        self.wordName.setStyleSheet("")
        self.wordName.setObjectName("wordName")
        self.horizontalLayout_10.addWidget(self.wordName)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem22)
        self.verticalLayout_8.addWidget(self.wordNameFrame)
        self.answersFrame = QtWidgets.QFrame(self.mainBlock)
        self.answersFrame.setStyleSheet("QPushButton{\n"
                                        "text-align:left;\n"
                                        "padding-left: 20px;\n"
                                        "color:white;\n"
                                        "background: rgb(33, 24, 38, 150);\n"
                                        "border:none;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background: rgb(33, 24, 38, 225);\n"
                                        "}")
        self.answersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answersFrame.setObjectName("answersFrame")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.answersFrame)
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.scrollAreaAnswers = QtWidgets.QScrollArea(self.answersFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaAnswers.sizePolicy().hasHeightForWidth())
        self.scrollAreaAnswers.setSizePolicy(sizePolicy)
        self.scrollAreaAnswers.setStyleSheet("QFrame{\n"
                                             "background-image: none;\n"
                                             "background: rgb(0, 0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QAbstractScrollArea {\n"
                                             "background: rgb(0, 0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:add-line:vertical {\n"
                                             "margin: 0px 0px 0px 0px;\n"
                                             "height: 0px;\n"
                                             "width: 0px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:sub-line:vertical {\n"
                                             "margin: 0px 0px 0px 0px;\n"
                                             "height: 5px;\n"
                                             "width: 0px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:vertical {\n"
                                             "background: rgb(33, 24, 38, 0);\n"
                                             "width: 12px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical {\n"
                                             "margin-bottom: 4px;\n"
                                             "margin-top: 4px;\n"
                                             "margin-left: 2px;\n"
                                             "background-color: rgb(170, 132, 186);\n"
                                             "border-radius: 3px;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical:hover {\n"
                                             "background-color: rgb(170, 132, 186, 200);\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:handle:vertical:pressed {\n"
                                             "background-color: rgb(170, 132, 186, 250);\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                             "background: rgb(33, 24, 38, 0);\n"
                                             "}")
        self.scrollAreaAnswers.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaAnswers.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollAreaAnswers.setWidgetResizable(True)
        self.scrollAreaAnswers.setObjectName("scrollAreaAnswers")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 941, 508))
        self.scrollAreaWidgetContents_3.setStyleSheet("QWidget{\n"
                                                      "background: rgb(33, 24, 38, 0);\n"
                                                      "border: none;\n"
                                                      "}")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.buttonsFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.buttonsFrame.setStyleSheet("QPushButton{\n"
                                        "text-align:left;\n"
                                        "padding-left: 20px;\n"
                                        "color:white;\n"
                                        "background: rgb(33, 24, 38, 150);\n"
                                        "border:none;\n"
                                        "border-radius: 15px;\n"
                                        "font-family: \"Yu Gothic UI Semilight\";\n"
                                        "font-size: 24px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background: rgb(33, 24, 38, 225);\n"
                                        "}")
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.buttonsFrame)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_9.addWidget(self.buttonsFrame, 0, QtCore.Qt.AlignTop)
        self.scrollAreaAnswers.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_23.addWidget(self.scrollAreaAnswers)
        self.verticalLayout_8.addWidget(self.answersFrame)
        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 3)
        self.horizontalLayout_9.addWidget(self.mainBlock)
        self.mainPages.addWidget(self.GamePage)
        self.verticalLayout.addWidget(self.mainPages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainPages.setCurrentIndex(0)
        self.settings.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.programTitle.setText(_translate("MainWindow", "English Words Trainer"))
        self.not_loaded_text.setText(_translate("MainWindow", "Загрузите слова из текстового файла."))
        self.loadButton.setText(_translate("MainWindow", "LOAD"))
        self.words_are_loaded.setText(_translate("MainWindow", "Слова загружены"))
        self.settingsTitle.setText(_translate("MainWindow", "Настройки"))
        self.autoSetcheckBox.setText(_translate("MainWindow", "Автоматические настройки"))
        self.questionLabel.setText(_translate("MainWindow",
                                              "Программа выберет максимальное количество слов, 4 варианта ответа и неограниченное время на выполнение."))
        self.amountUserLabel.setText(_translate("MainWindow", "Количество слов"))
        self.amountUserWord.setText(_translate("MainWindow", "/ 200 "))
        self.amountVarLabel.setText(_translate("MainWindow", "Количество вариантов"))
        self.userTimeLabel.setText(_translate("MainWindow", "Время выполнения в минутах"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Слова"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ответы"))
        self.errorLabel.setText(_translate("MainWindow", "Ошибка загрузки"))
        self.applyButton.setText(_translate("MainWindow", "APPLY"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.loadButton_2.setText(_translate("MainWindow", "LOAD"))
        self.optionsButton.setText(_translate("MainWindow", "OPTIONS"))
        self.resultsTittle.setText(_translate("MainWindow", "Результаты"))
        self.labelTimePass.setText(_translate("MainWindow", "Использованное время: 4:53"))
        self.labelAmountWords.setText(_translate("MainWindow", "Количество Слов: 15"))
        self.errorLabelRes.setText(_translate("MainWindow", "Ошибок: 4"))
        self.correctLabelRes.setText(_translate("MainWindow", "Правильных ответов: 15"))
        self.menuButton.setText(_translate("MainWindow", "MENU"))
        self.restartButton.setText(_translate("MainWindow", "RESTART"))
        self.time1.setText(_translate("MainWindow", "Время:"))
        self.time_num.setText(_translate("MainWindow", "00:00"))
        self.wordsNumTitle.setText(_translate("MainWindow", "Прогресс:"))
        self.wordsNumAmount.setText(_translate("MainWindow", "1/60 слов"))
        self.correct_words.setText(_translate("MainWindow", "Правильных ответов:"))
        self.correct_words_num.setText(_translate("MainWindow", "0"))
        self.invalid_label.setText(_translate("MainWindow", "Ошибок:"))
        self.invalid_num.setText(_translate("MainWindow", "0"))
        self.finishPushButton.setText(_translate("MainWindow", "FINISH"))
        self.wordName.setText(_translate("MainWindow", "Text"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
