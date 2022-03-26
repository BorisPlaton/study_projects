from trainer import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import re
from ctypes import *
import random


class Functions(QMainWindow):

    # GEOMETRY OF THE WINDOW (HEIGHT AND WIDTH)
    window_width = windll.user32.GetSystemMetrics(0)
    window_height = windll.user32.GetSystemMetrics(1)

    def __init__(self):
        super(Functions, self).__init__()

    def closeApp(self):
        """CLOSES THE APPLICATION"""
        self.close()

    def hideApp(self):
        """HIDES THE APPLICATION"""
        self.showMinimized()

    def fullSizeApp(self):
        """MAKES FULL OR NORMAL SIZE OF THE APPLICATION"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def titlePressEvent(self, event):
        """SAVES A COORDINATES WHERE YOU PRESSED THE MOUSE ON THE TITLE BAR"""
        self.clickPosition = event.globalPos()

    def moveWindow(self, event):
        """DRAGS WINDOW WHEN YOU PRESSED THE TITLE BAR"""
        # YOU CAN DRAG THE WINDOW ONLY WHEN YOU ARE PRESSING ON THE TITLE BAR BY LEFT MOUSE BUTTON
        if event.buttons() == Qt.LeftButton:
            # CHECKS ISN'T WINDOW A MAXIMUM SIZE
            if not self.isMaximized():
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
            else:
                self.showNormal()
                self.resize(1280, 720)
                # START AND END OF THE WINDOW
                x0 = event.globalPos().x() - self.width() // 2
                x1 = event.globalPos().x() + self.width() // 2
                if 0 < x0 and x1 < Functions.window_width:
                    self.move(x0, event.globalPos().y())
                elif x1 > Functions.window_width:
                    self.move(Functions.window_width - self.width(), event.globalPos().y())
                else:
                    self.move(0, event.globalPos().y())
                self.clickPosition = event.globalPos()
                event.accept()

    def openMenuHorizontalAnimation(self, max_size, min_size, frame_name):
        """ANIMATION OF OPEN/CLOSE IN THE HORIZONTAL DIRECTION"""

        animation_side_bar = QPropertyAnimation(frame_name, b"minimumWidth", self)
        animation_side_bar.setDuration(500)
        animation_side_bar.setEasingCurve(QEasingCurve.OutCirc)

        if frame_name.width() == min_size:
            self.__opening_H = True
            animation_side_bar.setStartValue(min_size)
            animation_side_bar.setEndValue(max_size)
            animation_side_bar.start()
        elif frame_name.width() == max_size:
            self.__opening_H = False
            animation_side_bar.setStartValue(max_size)
            animation_side_bar.setEndValue(min_size)
            animation_side_bar.start()
        else:
            # IF BUTTON HAD PRESSED WHEN ANIMATION HAD BEEN PROCESSING
            if self.__opening_H:
                self.openMenuHorizontalAnimation(frame_name.width(), min_size, frame_name)
            else:
                self.openMenuHorizontalAnimation(max_size, frame_name.width(), frame_name)

    def openMenuVerticalAnimation(self, max_size, min_size, frame_name):
        """ANIMATION OF OPEN/CLOSE IN THE VERTICAL DIRECTION"""

        animation_side_bar = QPropertyAnimation(frame_name, b"maximumHeight", self)
        animation_side_bar.setDuration(250)
        animation_side_bar.setEasingCurve(QEasingCurve.OutCirc)

        if frame_name.height() == min_size:
            self.__opening_V = True
            animation_side_bar.setStartValue(min_size)
            animation_side_bar.setEndValue(max_size)
            animation_side_bar.start()
        elif frame_name.height() == max_size:
            self.__opening_V = False
            animation_side_bar.setStartValue(max_size)
            animation_side_bar.setEndValue(min_size)
            animation_side_bar.start()
        else:
            # IF BUTTON HAD PRESSED WHEN ANIMATION HAD BEEN PROCESSING
            if self.__opening_V:
                self.openMenuVerticalAnimation(frame_name.height(), min_size, frame_name)
            else:
                self.openMenuVerticalAnimation(max_size, frame_name.height(), frame_name)


class NotEnoughWords(BaseException):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotEnoughWords Error, {self.message}'
        else:
            return 'NotEnoughWords Error'


class InvalidAmountVars(BaseException):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotEnoughWords Error, {self.message}'
        else:
            return 'NotEnoughWords Error'


class TextFile:

    def __init__(self):
        self.__words_text_dictionary = {}
        self.__words_list = []
        self.__text_lines = 0
        self.__error_line = 0
        self.__error_text = ""
        self.__text = ""

    def loadFile(self, file_path):
        """LOADS A FILE AND CREATES THE DICTIONARY WITH ENG/RUS WORDS"""
        current_line = 1
        self.__words_text_dictionary.clear()
        self.__words_list.clear()
        self.__error_line = 0
        self.__text_lines = 0
        self.__error_text = ""
        self.__text = ""

        with open(file_path, encoding="utf-8") as f:
            self.__text = f.readlines()

        for i in self.__text:
            try:
                # CHECKING LINE ON THE VALIDATION
                eng_word, answer = re.findall(r"^([a-zA-Z]+)\s*[|—-]\s*([а-яА-Я]+)\s*$", i)[0]
                self.__words_text_dictionary[eng_word] = answer
                self.__words_list.append(Word(eng_word, answer))
                current_line += 1

            # IF SOME LINE HAS MISTAKE
            except IndexError:
                # IF IT IS A EMPTY LINE
                if re.findall(r"^\s*\n", i):
                    current_line += 1
                # IN THE ANOTHER CASE WILL STOP A CYCLE AND SAVE AN INFORMATION ABOUT AN ERROR
                else:
                    self.__words_text_dictionary.clear()
                    self.__error_line = current_line
                    self.__error_text = f"Ошибка загрузки файла. Проверьте строку №{self.__error_line}:\n\"{i.split()[0]}\""
                    break

        if self.isFileLoaded():
            Word.words.clear()
            Word.answers.clear()
            for eng_word, rus_word in self.__words_text_dictionary.items():
                Word.words.append(eng_word)
                Word.answers.append(rus_word)
            self.__text_lines = current_line

    def isFileLoaded(self):
        """RETURNS TRUE IF A FILE IS LOADED"""
        if self.__words_text_dictionary:
            return True

    def setError(self, text):
        self.__words_text_dictionary.clear()
        self.__error_line = None
        self.__error_text = text

    def returnError(self):
        """RETURNS A LINE AND A TEXT OF THE ERROR"""
        return self.__error_line, self.__error_text

    def returnText(self):
        """RETURNS A LOADED TEXT"""
        text = ""
        for word, translation in self.__words_text_dictionary.items():
            text += f"{word} — {translation}\n"
        return text, len(self.__words_text_dictionary)

    @property
    def wordsList(self):
        """RETURNS A LIST WITH INSTANCES OF WORD CLASS"""
        return self.__words_list


class Word:
    """CLASS CREATED FOR STORING INFO ABOUT A WORD(AN ORIGINAL NAME, AN ANSWER AND VARIANTS OF THE ANSWER) """

    words = []
    answers = []

    def __init__(self, word, answer):
        self.__name = word
        self.__answer = answer
        self.__variants = None
        self.__variants_amount = 0
        # Word.words.append(self.__name)
        # Word.answers.append(self.__answer)

    def allWords(self):
        return Word.words

    def allAnswers(self):
        return Word.answers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, word):
        self.__name = word

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, word):
        self.__answer = word

    @property
    def variants(self):
        return self.__variants

    def set_variants(self, variants):
        self.__variants = variants

    def set_variants_amount(self, variants_amount):
        self.__variants_amount = variants_amount

    def check(self, variants_amount):
        if self.__variants_amount == variants_amount:
            return True
        else:
            return False

    def __repr__(self):
        """FOR EASILY UNDERSTANDING"""
        return f"{self.__name, self.__answer, self.__variants, self.__variants_amount}"


class Settings:

    def __init__(self, table=QTableWidget):
        super(Settings, self).__init__()
        self.__table = table
        self.__words_dict = {}
        self.__error_rows = set()
        self.__data = {
            "file": None,
            "amountWords": None,
            "amountVar": None,
            "time": None,
        }

    def setStandardSettings(self):
        """CREATES A NEW SETTINGS, CHANGES A TABLE OF WORDS AND INSTANCES OF WORD CLASS"""
        self.__table.setRowCount(0)
        self.__table.setRowCount(self.Data["amountWords"])
        self.__words_dict.clear()
        height = 0
        for row, word in enumerate(self.__data["file"]):
            word_english = QTableWidgetItem(f"{word.name} - {word.answer}")
            variants = ""
            for variant in word.variants:
                variants += f"{variant}, "
            word_english.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
            variants_ = QTableWidgetItem(variants[: -2])
            variants_.setTextAlignment(Qt.TextWordWrap)
            variants_.setTextAlignment(Qt.AlignVCenter)
            self.__words_dict[row] = word
            self.__table.setItem(row, 0, word_english)
            self.__table.setItem(row, 1, variants_)
            self.__table.resizeRowToContents(row)
            self.__table.setRowHeight(row, self.__table.rowHeight(row) + 12)
            height += self.__table.rowHeight(row)
        if (height + self.__table.horizontalHeader().height()) > 312:
            self.__table.horizontalHeader().setDefaultSectionSize(219)
            self.__table.setFixedHeight(height + self.__table.horizontalHeader().height() + 2)
        else:
            self.__table.setFixedHeight(312)
            self.__table.horizontalHeader().setDefaultSectionSize(224)

    @property
    def Data(self):
        """MAIN INFO ABOUT A SETTINGS"""
        return self.__data

    @Data.setter
    def Data(self, data):
        """CHANGES A DATA PROPERTY'S INFO"""
        self.__data["file"] = data["file"]
        self.__data["amountWords"] = data["amountWords"]
        self.__data["time"] = data["time"]
        if data["amountVar"] == "default":
            self.__setMinVarAmount()
        elif isinstance(data["amountVar"], int):
            if not self.__data["amountVar"] == data["amountVar"]:
                self.__data["amountVar"] = data["amountVar"]
                self.setVarAmount(self.__data["amountVar"])

    def updateData(self, data):
        """UPDATES self.__data IF data IS CORRECT"""
        self.__validate_data(data)
        if self.__validation:
            self.__data["amountWords"] = data["amountWords"]
            if not self.__data["amountVar"] == data["amountVar"]:
                self.__data["amountVar"] = data["amountVar"]
                self.setVarAmount(self.__data["amountVar"])
            self.__data["time"] = data["time"]

            if data["file"]:
                for row, variants in data["file"].items():
                    self.__words_dict[row].set_variants(variants)

            height = 0
            for row, word in self.__words_dict.items():
                variants = ""
                for variant in word.variants:
                    variants += f"{variant}, "
                variants_ = QTableWidgetItem(variants[: -2])
                variants_.setTextAlignment(Qt.TextWordWrap)
                variants_.setTextAlignment(Qt.AlignVCenter)
                self.__table.setItem(row, 1, variants_)
                self.__table.resizeRowToContents(row)
                self.__table.setRowHeight(row, self.__table.rowHeight(row) + 12)
                height += self.__table.rowHeight(row)
            if (height + self.__table.horizontalHeader().height()) > 312:
                self.__table.horizontalHeader().setDefaultSectionSize(219)
                self.__table.setFixedHeight(height + self.__table.horizontalHeader().height() + 2)
            else:
                self.__table.setFixedHeight(height + self.__table.horizontalHeader().height())
                self.__table.horizontalHeader().setDefaultSectionSize(224)

    def updateDataStatus(self):
        """RETURNS TRUE IF DATA WAS SUCCESSFULLY VALIDATED"""
        if self.__validation:
            return True

    def giveUpdateInfo(self):
        """RETURNS A DICT CONTAINS STATUSES OF DATA VALIDATION"""
        return self.__validation_status

    def errorRows(self):
        """RETURNS A LIST CONTAINS ROWS WHICH HAVE AN INCORRECT INPUT"""
        return self.__error_rows

    def __validate_data(self, data):
        """CHECKS A DATA ON THE CORRECT INPUT"""
        self.__error_rows.clear()
        self.__validation_status = {
            "file": False,
            "amountWords": False,
            "amountVar": False,
            "time": False,
        }
        self.__validation = True
        if data["amountWords"] > 1:
            self.__validation_status["amountWords"] = True
        if data["amountVar"] < len(self.__words_dict):
            self.__validation_status["amountVar"] = True
        if data["file"]:
            for row, variants in data["file"].items():
                if not len(variants) + 1 == data["amountVar"]:
                    self.__validation_status["file"] = False
                    self.__error_rows.add(row)
                elif self.__words_dict[row].answer in variants:
                    self.__validation_status["file"] = False
                    self.__error_rows.add(row)
                if not len(self.__error_rows):
                    self.__validation_status["file"] = True
        else:
            self.__validation_status["file"] = True
        if isinstance(data["time"], int):
            self.__validation_status["time"] = True
        for status in self.__validation_status.items():
            if not status[1]:
                self.__validation = False
                break

    def __setMinVarAmount(self):
        """ANALYZING A MINIMAL AMOUNT OF THE VARIANTS"""
        if self.__data["amountWords"] < 2:
            raise NotEnoughWords
        elif 1 < self.__data["amountWords"] < 5:
            self.__data["amountVar"] = self.__data["amountWords"]
        else:
            self.__data["amountVar"] = 4
        # SETS AN AMOUNT OF THE VARIANTS OF A WORD
        self.setVarAmount(self.__data["amountVar"])

    def setVarAmount(self, num):
        """SETS AN AMOUNT OF THE VARIANTS"""
        for word in self.__data["file"]:
            used_words = set()
            step = 0
            used_words.add(word.answer)
            while step < self.__data["amountVar"] - 1:
                variant = random.choice(Word.answers)
                if not (variant in used_words):
                    used_words.add(variant)
                    step += 1
            word.set_variants_amount(num)
            used_words.remove(word.answer)
            word.set_variants(tuple(used_words))
        self.__data["amountVar"] = num

    def gameData(self):
        """DATA ARE USED ONLY FOR GAME"""
        return {
            "file": self.__data["file"][:self.__data["amountWords"]],
            "amountWords": self.__data["amountWords"],
            "amountVar": self.__data["amountVar"],
            "time": self.__data["time"]
        }


class Timer:

    def __init__(self):
        self.__sec_str = "00"
        self.__min_str = "00"
        self.__time = f"{self.__min_str}:{self.__sec_str}"
        self.__sec = 0
        self.__min = 0
        self.__time_limit = -1
        self.__total_time = 0

    def setTimeRange(self, time_):
        self.__time_limit = time_ * 60

    def stop(self):
        """STOP ALL PROCESSES"""
        self.__sec_str = "00"
        self.__min_str = "00"
        self.__time = f"{self.__min_str}:{self.__sec_str}"
        self.__sec = 0
        self.__min = 0
        self.__time_limit = -1
        self.__total_time = 0

    @property
    def currentTime(self):
        """INCREASES THE TIME ONLY WHEN IT IS CALLED / GIVES A STR FORMAT TIME"""
        self.__secChange()
        return self.__time

    def __setCurrentTime(self, time_):
        """SETS A STRING FORMAT TO THE TIME"""
        self.__time = time_

    def __secChange(self):
        """INCREASE SECONDS"""
        self.__sec += 1
        self.__total_time += 1
        if self.__sec < 10:
            self.__sec_str = f"0{self.__sec}"
        elif 10 <= self.__sec < 60:
            self.__sec_str = f"{self.__sec}"
        elif self.__sec == 60:
            self.__sec_str = "00"
            self.__sec = 0
            self.__minChange()
        if self.__total_time == self.__time_limit:
            raise GameOverError
        self.__setCurrentTime(f"{self.__min_str}:{self.__sec_str}")

    def __minChange(self):
        """INCREASE MINUTES"""
        self.__min += 1
        if self.__min < 10:
            self.__min_str = f"0{self.__min}"
        elif 10 <= self.__min < 60:
            self.__min = f"{self.__min}"
        elif self.__min == 60:
            self.__min_str = "00"
            self.__min = 0
        self.__setCurrentTime(f"{self.__min_str}:{self.__sec_str}")


class GameOverError(BaseException):
    """WHEN TIME IS PASSED OR ALL WORDS ARE USED"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotEnoughWords Error, {self.message}'
        else:
            return 'NotEnoughWords Error'


class Game:
    """KEEPS ALL INFORMATION ABOUT WORDS ARE USED"""

    def __init__(self):
        self.__data = {
            "file": [],
            "amountVar": 0,
            "amountWords": 0,
            "time": 0,
        }
        self.__used_words = set()
        self.__correct_answers = 0
        self.__mistakes = 0
        self.__step = 0

    def collectData(self, data):
        """DATA THAT NEED FOR PLAYING"""
        self.__data = data

    @property
    def Data(self):
        return self.__data

    def Words(self):
        self.__used_words.add(self.__data["file"])

    @property
    def correct(self):
        return self.__correct_answers

    def correctIncrease(self):
        self.__correct_answers += 1

    @property
    def mistake(self):
        return self.__mistakes

    def mistakeIncrease(self):
        self.__mistakes += 1

    def nextWord(self):
        while True:
            if not self.__data["amountWords"] == len(self.__used_words):
                word = random.choice(self.__data["file"])
                if word not in self.__used_words:
                    self.__used_words.add(word)
                    self.__step += 1
                    return word, self.__step
            else:
                raise GameOverError

    def end(self):
        """DELETE ALL DATA"""
        self.__data = {
            "file": [],
            "amountVar": 0,
            "amountWords": 0,
            "time": 0,
        }
        self.__used_words = set()
        self.__correct_answers = 0
        self.__mistakes = 0
        self.__step = 0


class MainWindow(Functions):

    def __init__(self):
        # INITIALIZATION OF AN APPLICATION
        super(MainWindow, self).__init__()
        self.app = Ui_MainWindow()
        self.app.setupUi(self)
        self.resize(1440, 880)
        self.app.settings.setCurrentIndex(0)
        self.app.settingsMainFrame.setMinimumWidth(500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("English Words Trainer")
        self.app.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.app.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.app.tableWidget.setWordWrap(True)
        self.show()

        # INITIALIZING CLASSES
        self.timer = Timer()
        self.settingsMenu = Settings(self.app.tableWidget)
        self.textFile = TextFile()
        self.__game = Game()
        self.__errorStatus = {
            "file": {},
            "amountVar": None,
            "amountWords": None,
            "time": None,
        }
        self.time_delay = QTimer()
        self.time_delay.timeout.connect(lambda: self.changeTime())
        self.__answersButton = {}
        self.wait = True
        self.correct_answers = []
        self.incorrect_answers = []

        # SETTING UP THE TITLE BUTTONS
        self.app.close_button.clicked.connect(self.closeApp)
        self.app.hide_button.clicked.connect(self.hideApp)
        self.app.full_button.clicked.connect(self.fullSizeApp)

        # SETTING UP THE TITLE BAR
        self.app.title.mousePressEvent = self.titlePressEvent
        self.app.title.mouseMoveEvent = self.moveWindow

        # SETTING UP THE LOAD BUTTON
        self.app.loadButton.clicked.connect(self.fileLoading)
        self.app.loadButton_2.clicked.connect(self.fileLoading)

        # SETTING UP THE OPTIONS BUTTON
        self.app.optionsButton.clicked.connect(
            lambda: self.openMenuHorizontalAnimation(1020, 500, self.app.settingsMainFrame))
        self.app.question_button.clicked.connect(
            lambda: self.openMenuVerticalAnimation(79, 20, self.app.autoSetMainFrame))
        self.app.autoSetcheckBox.clicked.connect(self.autoSettings)

        # APPLY BUTTON
        self.app.applyButton.clicked.connect(self.applySettings)

        # START BUTTON
        self.app.startButton.clicked.connect(self.startGame)

        # END THE GAME
        self.app.finishPushButton.clicked.connect(self.endGame)

        # A RESULTS MENU'S BUTTONS
        self.app.menuButton.clicked.connect(lambda: self.app.settings.setCurrentIndex(1))
        self.app.restartButton.clicked.connect(lambda: self.startGame())

    def endGame(self):
        """SHOWS RESULTS AND STOPS ALL PROCESSES"""
        # CHANGING LABELS IN THE RESULTS MENU
        self.app.mainPages.setCurrentIndex(0)
        self.app.settings.setCurrentIndex(2)
        self.app.labelTimePass.setText("Использованное время: " + self.timer.currentTime)
        self.timer.stop()
        self.time_delay.stop()

        self.app.labelAmountWords.setText("Количество Слов: " + str(self.__game.Data["amountWords"]))
        self.app.errorLabelRes.setText("Ошибок: " + str(self.__game.mistake))

        text = ""
        for mistake in self.incorrect_answers:
            text += f"{mistake}\n"
        self.app.errorTextEdit.setPlainText(text)

        self.app.correctLabelRes.setText("Правильных ответов: " + str(self.__game.correct))
        text = ""
        for correct in self.correct_answers:
            text += f"{correct}\n"
        self.app.correctTextEdit.setPlainText(text)

        self.__game.end()

        for _, button in self.__answersButton.items():
            button.deleteLater()

        self.__answersButton.clear()
        self.correct_answers.clear()
        self.incorrect_answers.clear()
        text = ""

    def startGame(self):
        """CHANGE PAGE AND START GAME"""
        self.__game.collectData(self.settingsMenu.gameData())

        # FILLING ANSWER BUTTONS
        for num in range(self.__game.Data["amountVar"]):
            button = QPushButton(self)
            button.setMinimumHeight(125)
            button.setMaximumHeight(125)
            button.setFont(QFont("Yu Gothic UI Semilight", 24))
            self.__answersButton[num] = button
            button.clicked.connect(self.answerButton)
            self.app.verticalLayout_25.addWidget(button)

        # IF A TIME PARAMETER EQUAL ZERO IT MEANS INFINITY TIME EXECUTING
        if not self.__game.Data["time"] == 0:
            self.timer.setTimeRange(self.__game.Data["time"])
        self.app.time_num.setText("00:00")
        self.time_delay.start(1000)

        self.setWords()
        self.app.settingsMainFrame.setMinimumWidth(500)
        self.app.settingsScrollArea.ensureVisible(0, 0)
        self.app.mainPages.setCurrentIndex(1)

    def setWords(self):
        """SETS NEW WORDS AT THE BUTTONS AND AT THE wordName LABEL"""
        try:
            variants = []
            self.current_word, step = self.__game.nextWord()

            # VARIANTS (TEXT FOR BUTTONS)
            variants.append(self.current_word.answer)
            for var in self.current_word.variants:
                variants.append(var)
            self.app.wordName.setText(self.current_word.name)
            self.app.correct_words_num.setText(str(self.__game.correct))
            self.app.invalid_num.setText(str(self.__game.mistake))
            self.app.wordsNumAmount.setText(f"""{step}/{self.__game.Data["amountWords"]} слов""")

            for _, button in self.__answersButton.items():
                var = random.choice(variants)
                button.setText(var)
                button.setStyleSheet("""
                                        """)
                variants.remove(var)
                button.setEnabled(True)
        except GameOverError:
            if not self.app.mainPages.currentIndex() == 0:
                self.endGame()

    def answerButton(self):
        """ANALYZE A USER ANSWER"""
        if self.sender().text() == self.current_word.answer:
            self.correct_answers.append(str(self.current_word.name))
            self.__game.correctIncrease()
        else:
            self.incorrect_answers.append(str(self.current_word.name))
            self.__game.mistakeIncrease()
        for _, button in self.__answersButton.items():
            button.setEnabled(False)
            if button.text() != self.current_word.answer:
                button.setStyleSheet("""
                QPushButton{
                    background:rgb(235, 64, 52);
                }
                """)
            else:
                button.setStyleSheet("""
                QPushButton{
                    background:rgb(60, 227, 57);
                }
                """)

        # GIVES TIME TO WATCH ANSWERS
        QTimer().singleShot(2000, lambda: self.setWords())

    def changeTime(self):
        """CHANGES A TIME SCALE AT THE SIDE BAR"""
        try:
            self.app.time_num.setText(self.timer.currentTime)
        except GameOverError:
            if not self.app.mainPages.currentIndex() == 0:
                self.endGame()

    def applySettings(self):
        """APPLIES SETTINGS SELECTED BY USER OR GIVES A MESSAGE SAID DATA IS WRONG"""
        self.settingsMenu.updateData(self.__dict_of_changes)
        if self.settingsMenu.updateDataStatus():
            self.__dict_of_changes = {
                "file": {},
                "amountWords": self.app.spinBoxAmountWords.value(),
                "amountVar": self.app.spinBoxAmountVar.value(),
                "time": self.app.userTimeSpinBox.value(),
            }
            self.app.errorLabelFrame.setMaximumHeight(0)
        else:
            self.__errorStatus = self.settingsMenu.giveUpdateInfo()
            for error, status in self.__errorStatus.items():
                if not status:
                    if error == "amountWords":
                        self.app.spinBoxAmountWords.setStyleSheet("""
                            QSpinBox{
                                background: rgb(173, 63, 55);
                            }
                        """)
                    elif error == "amountVar":
                        self.app.spinBoxAmountVar.setStyleSheet("""
                            QSpinBox{
                                background: rgb(173, 63, 55);
                            }
                        """)
                    elif error == "time":
                        self.app.userTimeSpinBox.setStyleSheet("""
                            QSpinBox{
                                background: rgb(173, 63, 55);
                            }
                        """)
                    elif error == "file":
                        for row in self.settingsMenu.errorRows():
                            self.app.tableWidget.item(row, 1).setText("#############")

                self.app.errorLabelFrame.setMaximumHeight(33)

    def fileLoading(self):
        """IF A FILE IS LOADED WILL OPEN NEW PAGE"""
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open File",
            directory="",
            filter="Text Files (*.txt)"
        )
        # IF A FILE WAS SELECTED
        if file_path:
            self.textFile.loadFile(file_path)
            # IF A TEXT IN THE FILE WAS SUCCESSFUL VALIDATED
            if self.textFile.isFileLoaded():
                self.settingsMenu.Data = {
                    "file": self.textFile.wordsList,
                    "amountWords": len(Word.words),
                    "amountVar": "default",
                    "time": 0,
                }

                self.app.spinBoxAmountWords.setMinimum(2)
                self.app.spinBoxAmountWords.setMaximum(self.settingsMenu.Data["amountWords"])
                self.app.spinBoxAmountWords.setValue(self.settingsMenu.Data["amountWords"])
                self.app.amountUserWord.setText(f"""/ {self.settingsMenu.Data["amountWords"]}""")

                self.app.spinBoxAmountVar.setMinimum(2)
                self.app.spinBoxAmountVar.setMaximum(self.settingsMenu.Data["amountWords"])
                self.app.spinBoxAmountVar.setValue(self.settingsMenu.Data["amountVar"])

                self.app.userTimeSpinBox.setValue(0)

                self.settingsMenu.setStandardSettings()

                self.app.autoSetcheckBox.setChecked(True)

                # SWITCH TO THE LOADED MENU
                self.app.settings.setCurrentIndex(1)
                text, words_count = self.textFile.returnText()
                # SETTING A LIST OF THE LOADED WORDS (ONLY FOR READING)
                self.app.list_of_words.setPlainText(text)
                # SETTING A CONSTANTS
                try:
                    self.autoSettings()
                    # IF SOME OPTION CHANGES WILL CHANGE A AUTO_SET_CHECK_BOX'S CONDITION
                    self.app.tableWidget.itemChanged.connect(self.changeSettings)
                    self.app.spinBoxAmountWords.valueChanged.connect(
                        lambda: self.changeSettings(self.app.spinBoxAmountWords.value()))
                    self.app.spinBoxAmountVar.valueChanged.connect(
                        lambda: self.changeSettings(self.app.spinBoxAmountVar.value()))
                    self.app.userTimeSpinBox.valueChanged.connect(
                        lambda: self.changeSettings(self.app.userTimeSpinBox.value()))

                except NotEnoughWords:
                    self.app.settingsMainFrame.setMinimumWidth(500)
                    self.app.settings.setCurrentIndex(0)
                    self.textFile.setError("Слишком мало слов.")
                    _, error_text = self.textFile.returnError()
                    self.app.not_loaded_text.setText(error_text)
            # IN ANOTHER CASE
            else:
                # IF A FILE WAS OPENED IN THE IS_LOADED_MENU
                if self.app.settings.currentIndex() == 1:
                    self.app.settingsMainFrame.setMinimumWidth(500)
                    self.app.settings.setCurrentIndex(0)
                _, error_text = self.textFile.returnError()
                self.app.not_loaded_text.setText(error_text)

    def autoSettings(self):
        """SETTINGS GIVEN BY A PROGRAM"""
        if self.app.autoSetcheckBox.isChecked():
            self.settingsMenu.Data = {
                "file": self.textFile.wordsList,
                "amountWords": len(Word.words),
                "amountVar": "default",
                "time": 0,
            }

            self.app.spinBoxAmountWords.setMinimum(2)
            self.app.spinBoxAmountWords.setMaximum(self.settingsMenu.Data["amountWords"])
            self.app.spinBoxAmountWords.setValue(self.settingsMenu.Data["amountWords"])
            self.app.amountUserWord.setText(f"""/ {self.settingsMenu.Data["amountWords"]}""")

            self.app.spinBoxAmountVar.setMinimum(2)
            self.app.spinBoxAmountVar.setMaximum(self.settingsMenu.Data["amountWords"])
            self.app.spinBoxAmountVar.setValue(self.settingsMenu.Data["amountVar"])

            self.app.userTimeSpinBox.setValue(0)

            self.settingsMenu.setStandardSettings()

            self.__dict_of_changes = {
                "file": {},
                "amountWords": self.settingsMenu.Data["amountWords"],
                "amountVar": self.settingsMenu.Data["amountVar"],
                "time": 0,
            }
            self.app.autoSetcheckBox.setChecked(True)

        if self.app.errorLabelFrame.height() > 0:
            self.app.errorLabelFrame.setMaximumHeight(0)

    def changeSettings(self, value):
        """ADDS CHANGES IN SETTINGS MENU IN self.__dict_of_changes"""
        self.app.autoSetcheckBox.setChecked(False)
        if self.sender() == self.app.spinBoxAmountWords:

            if not self.__errorStatus["amountWords"]:
                self.app.spinBoxAmountWords.setStyleSheet("")
                self.__errorStatus["amountWords"] = True
            self.__dict_of_changes["amountWords"] = value

        elif self.sender() == self.app.spinBoxAmountVar:

            if not self.__errorStatus["amountVar"]:
                self.app.spinBoxAmountVar.setStyleSheet("")
                self.__errorStatus["amountVar"] = True
            self.__dict_of_changes["amountVar"] = value

        elif self.sender() == self.app.userTimeSpinBox:

            if not self.__errorStatus["time"]:
                self.app.userTimeSpinBox.setStyleSheet("")
                self.__errorStatus["time"] = True
            self.__dict_of_changes["time"] = value

        elif self.sender() == self.app.tableWidget:

            # VALIDATES VARIANTS WRITTEN BY USER
            variants_set = set()
            for word in value.text().split(","):
                try:
                    variant = re.findall(r"[а-яА-Я]+", word.rstrip())[0]
                    if variant:
                        variants_set.add(variant)
                except IndexError:
                    continue
            self.__dict_of_changes["file"].update({value.row(): tuple(variants_set)})
            variants_set.clear()
            # MAKES A CORRECT SIZE OF THE CELL
            self.app.tableWidget.resizeRowToContents(value.row())
            self.app.tableWidget.setFixedHeight(self.app.tableWidget.height())
        if self.app.errorLabelFrame.height() == 30:
            self.app.errorLabelFrame.setMaximumHeight(0)


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Application")
sys.exit(app.exec_())
