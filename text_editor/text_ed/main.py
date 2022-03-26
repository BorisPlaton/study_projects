from text import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import re
from ctypes import *


class CSSWidget(QWidget):

    def __init__(self, dict_widgets):
        super(CSSWidget, self).__init__()
        self.widgets_name = dict_widgets
        self.current_index = 1

    def getCurrentWidget(self, index):
        return self.widgets_name[index]


class FileDialog(QFileDialog):
    """FILE SYSTEM(SAVE, NEW, OPEN)"""

    def __init__(self):
        super(FileDialog, self).__init__()

    def saveFile(self, text, condition="New", file_place=""):
        """SAVES FILE"""
        if condition == "New":
            file_path, _ = QFileDialog.getSaveFileName(
                parent=self,
                caption="New File",
                directory="",
                filter="Text Files (*.txt)"
            )
            if file_path:
                with open(file_path, "w") as f:
                    f.write(text)
                file_name = FileDialog.file_name(file_path)
                is_file_saved = True
                return file_name, file_path, is_file_saved
        elif condition == "Same":
            with open(file_place, "w") as f:
                f.write(text)

    def openFile(self, saved, opened):
        """OPENS DIALOG MENU"""
        # IF TEXT ISN'T SAVED WILL ASK YOU TO OPEN NEW FILE
        if (not saved and opened) or (not opened and not saved):
            if FileDialog.__message("You didn't save this one. Are you sure to open new file?", "Open File"):
                file_path = self.__opening()
                if file_path:
                    file_name = FileDialog.file_name(file_path)
                    is_file_saved = True
                    return file_name, file_path, is_file_saved
        # OPENS WITHOUT AN QUESTION
        else:
            file_path = self.__opening()
            if file_path:
                file_name = FileDialog.file_name(file_path)
                is_file_saved = True
                return file_name, file_path, is_file_saved

    def newFile(self, saved, opened):
        """CREATES A NEW FILE IN CURRENT DIRECTION"""
        # IF TEXT ISN'T SAVED WILL ASK YOU TO CREATE NEW FILE
        if (not saved and opened) or (not opened and not saved):
            if FileDialog.__message("You didn't save this one. Are you sure to create new file?", "New File"):
                file_path = self.__creating()
                if file_path:
                    file_name = FileDialog.file_name(file_path)
                    is_file_saved = True
                    file = open(file_path, "w")
                    file.close()
                    return file_name, file_path, is_file_saved
        # CREATES WITHOUT AN QUESTION
        else:
            file_path = self.__creating()
            if file_path:
                file_name = FileDialog.file_name(file_path)
                is_file_saved = True
                file = open(file_path, "w")
                file.close()
                return file_name, file_path, is_file_saved

    def __creating(self):
        """CREATES A FILEDIALOG WINDOW"""
        file_path, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption="New File",
            directory="",
            filter="Text Files (*.txt)"
        )
        return file_path

    def __opening(self):
        """RETURNS A PATH TO THE FILE"""
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open File",
            directory="",
            filter="Text Files (*.txt)"
        )
        return file_path

    @staticmethod
    def __message(text, title):
        """SHOW MESSAGE"""
        msg = QMessageBox()
        pm = QPixmap(1, 1)
        pm.fill(QColor(0, 0, 0, 0))
        msg.setWindowFlags(Qt.SubWindow)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.exec_()
        if msg.standardButton(msg.clickedButton()) == QMessageBox.Yes:
            return True

    @staticmethod
    def file_name(path):
        """RETURNS A FILE NAME"""
        pattern = r".+\/(.+).txt"
        file_name = re.findall(pattern, path)[0]
        return file_name


class SearchHighLight(QSyntaxHighlighter):
    """SEARCHING WORDS IN THE TEXT FIELD"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def find_word(self, pattern):
        """"""
        self.pattern = pattern
        self.format_pattern = QTextCharFormat()
        self.format_pattern.setBackground(QColor(61, 227, 114, 125))

    def highlightBlock(self, text):
        for match in re.finditer(self.pattern, text.lower()):
            start, end = match.span()
            self.setFormat(start, end - start, self.format_pattern)


class MainWindow(QMainWindow):

    def __init__(self):
        # INITIALIZATION OF AN APPLICATION
        super(MainWindow, self).__init__()
        self.app = Ui_MainWindow()
        self.app.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

        # FOR CSS PAGE
        self.css_page = CSSWidget(
            {0: self.app.css_pushButton,
             1: self.app.css_label,
             2: self.app.horizontalScrollBar,
             3: self.app.verticalScrollBar,
             4: self.app.verticalSlider,
             5: self.app.horizontalSlider,
             6: self.app.radio_button,
             7: self.app.lineEdit,
             8: self.app.checkBox
             }
        )
        self.css_widget_index = 0

        # FOR FILE DIALOG
        self.__is_file_saved = True
        self.__is_file_open = False
        self.__file_new = False
        self.__file_name = ""
        self.__file_path = ""

        # INSTANCE OF QSyntaxHighlighter
        self.searcher = SearchHighLight()

        # GEOMETRY OF THE WINDOW (HEIGHT AND WIDTH)
        self.window_width = windll.user32.GetSystemMetrics(0)
        self.window_height = windll.user32.GetSystemMetrics(1)

        """CONNECTING COMMANDS"""
        # CLOSING THE APP
        self.app.close_button.clicked.connect(self.close)

        # CHANGING A WINDOW SIZE
        self.app.full_button.clicked.connect(self.change_size_app)

        # HIDE THE WINDOW
        self.app.hide_button.clicked.connect(self.showMinimized)

        # DRAGGING THE WINDOW
        self.app.title_bar.mouseMoveEvent = self.moveWindow

        # OPENING THE SIDE BAR MENU
        self.app.side_full_button.clicked.connect(lambda: self.oc_side_bar_menu(50, 150))

        # OPENING THE TOOLS BAR
        self.app.close_open_tools_bar_but.clicked.connect(
            lambda: self.animation_open_bar(self.app.tools_bar, 25, 175, 350, QEasingCurve.OutCirc))

        # CHANGING THE PAGES
        self.current_page = self.app.home_button
        self.current_page.setStyleSheet("""
        QPushButton {
            background:rgba(77, 88, 110, 50);
            border-right: 4px solid rgb(77, 88, 110);   
        }
        QPushButton:hover {
            background: rgba(86, 94, 110, 100);
        }
        QPushButton:pressed{
            background: rgba(86, 94, 110, 150);
        }
        """)
        # OPENING THE TOOL BAR
        self.app.settings_button.clicked.connect(lambda: self.change_page(1))
        self.app.home_button.clicked.connect(lambda: self.change_page(0))

        # ANALYZING THE TEXT IN THE TEXT_FIELD AND CHANGING VALUES IN THE STATUS BAR
        self.app.text_field.textChanged.connect(self.words_count_function)
        self.app.text_field.cursorPositionChanged.connect(self.analyze_previous_char)

        # CHANGING A VALUE OF THE SELECTED CHARS IN THE STATUS BAR
        self.app.text_field.selectionChanged.connect(self.selectionText)

        # MAKING A STYLED TEXT
        self.app.italic_check_box.clicked.connect(lambda: self.style_text(style="italic"))
        self.app.bold_check_box.clicked.connect(lambda: self.style_text(style="bold"))
        self.app.underline_check_box.clicked.connect(lambda: self.style_text(style="underline"))
        self.app.font_spin_box.valueChanged.connect(lambda: self.style_text(size=self.app.font_spin_box.value()))

        # SEARCHING WORDS IN THE TEXT FIELD
        self.app.findword_line.textChanged.connect(self.search_words)

        # OPENING A NEW TEXT FILE
        self.app.open_button.clicked.connect(self.open_file)

        # CREATING A NEW TEXT FILE
        self.app.new_button.clicked.connect(self.create_new_file)

        # SAVING A CURRENT FILE
        self.app.save_button.clicked.connect(self.save_file)

        # SWITCHING PAGES AT THE CSS PAGE
        self.app.widget_box.currentIndexChanged.connect(self.switch_css_page)

        # SETTING CSS CODE ON WIDGET IN CSS PAGE
        self.app.css_form.textChanged.connect(self.set_css_code)

    def set_css_code(self):
        """SETS CSS STYLE"""
        css = self.app.css_form.toPlainText()
        self.css_page.getCurrentWidget(self.css_widget_index).setStyleSheet(css)

    def switch_css_page(self, index):
        """CHANGES PAGES"""
        self.css_page.getCurrentWidget(self.css_widget_index).setStyleSheet("")
        self.css_widget_index = index
        self.app.examples.setCurrentIndex(self.css_widget_index)

    def save_file(self):
        """SAVES A TEXT IN THE TEXT FIELD"""
        file_dialog = FileDialog()
        if self.app.status_text.text() != self.__file_name:
            file_status_pack = file_dialog.saveFile(self.app.text_field.toPlainText())
            if file_status_pack:
                (self.__file_name, self.__file_path,
                 self.__is_file_saved), self.__is_file_open, self.__file_new = file_status_pack, True, True
                self.app.status_text.setText(self.__file_name)
        else:
            file_dialog.saveFile(self.app.text_field.toPlainText(), condition="Same", file_place=self.__file_path)
            self.__is_file_saved = True

    def create_new_file(self):
        """CREATES A NEW FILE"""
        file_dialog = FileDialog()
        file_status_pack = file_dialog.newFile(self.__is_file_saved, self.__is_file_open)
        if file_status_pack:
            (self.__file_name, self.__file_path,
             self.__is_file_saved), self.__is_file_open, self.__file_new = file_status_pack, True, True
            self.app.status_text.setText(self.__file_name)

    def open_file(self):
        """OPENS A FILE AND PUT A TEXT IN THE TEXT FIELD"""
        file_dialog = FileDialog()
        file_status_pack = file_dialog.openFile(self.__is_file_saved, self.__is_file_open)
        if file_status_pack:
            (self.__file_name, self.__file_path,
             self.__is_file_saved), self.__is_file_open, self.__file_new = file_status_pack, True, True
            self.app.status_text.setText(self.__file_name)
            with open(self.__file_path) as f:
                text = f.read()
                self.app.text_field.setText(text)

    def search_words(self):
        """LOOKS FOR THE WORDS AT THE TEXT FIELD AND HIGHLIGHT THEM"""
        pattern = self.app.findword_line.text().lower()
        self.searcher.find_word(pattern)
        self.searcher.setDocument(self.app.text_field.document())

    def analyze_previous_char(self):
        """ANALYSING A PREVIOUS CHARACTER BEFORE THE CURSOR VIA ANALYZE_TEXT FUNC AND CURRENT SELECTED LINE"""
        cursor_line = self.app.text_field.toPlainText()[:self.app.text_field.textCursor().position()]
        self.app.current_lines.setText(str(cursor_line.count("\n") + 1))
        cursor = self.app.text_field.textCursor()
        cursor.movePosition(QTextCursor.PreviousCharacter, QTextCursor.KeepAnchor, 1)
        self.analyze_text(cursor.selection().toHtml())

    def analyze_text(self, text=""):
        """MAKING ANALYZE OF THE SELECTED TEXT ON STYLES"""
        # SETTING PATTERNS FOR REGULAR EXPRESSION
        italic = r"<span style=\" (.*font-style:italic;.*)\">"
        bold = r"<span style=\" (.*font-weight:800;.*)\">"
        underline = r"<span style=\" (.*text-decoration: underline;.*)\">"
        size = r"<span style=\" font-size:(\d*)pt;\">"

        # LOOKS FOR ITALIC STYLE
        if re.findall(italic, text):
            self.app.italic_check_box.setChecked(True)
        else:
            self.app.italic_check_box.setChecked(False)

        # LOOKS FOR UNDERLINE STYLE
        if re.findall(underline, text):
            self.app.underline_check_box.setChecked(True)
        else:
            self.app.underline_check_box.setChecked(False)

        # LOOKS FOR BOLD STYLE
        if re.findall(bold, text):
            self.app.bold_check_box.setChecked(True)
        else:
            self.app.bold_check_box.setChecked(False)

        # SET FONT SIZE
        font_list = re.findall(size, text)
        if len(font_list) == 1:
            self.app.font_spin_box.setValue(int(font_list[0]))
        elif len(font_list) == 0:
            self.app.text_field.setFontPointSize(self.app.font_spin_box.value())

    def selectionText(self):
        """COUNTING AMOUNT SELECTED CHARS AND PUTTING IN STATUS BAR"""
        cursor = self.app.text_field.textCursor()
        len_chars = len(cursor.selectedText())
        self.app.selected_chars.setText(str(len_chars))
        if cursor.hasSelection():
            selected = cursor.selection().toHtml()
            self.analyze_text(selected)

    def style_text(self, *, style="", size=0):
        """DEFINES STYLE OF TEXT"""
        # IN CASE WHEN SETS FONT STYLE
        if style:
            style_cond = True
            if not self.sender().isChecked():
                style_cond = False
            if style == "italic":
                self.app.text_field.setFontItalic(style_cond)
            elif style == "bold":
                if style_cond:
                    self.app.text_field.setFontWeight(100)
                else:
                    self.app.text_field.setFontWeight(0)
            elif style == "underline":
                self.app.text_field.setFontUnderline(style_cond)
            self.app.text_field.setFocus()

        # IN CASE WHEN SETS FONT SIZE
        elif size:
            self.app.text_field.setFontPointSize(size)

    def animation_open_bar(self, widget, start, end, duration, type_curve):
        """OPENING TOOL BAR"""
        animation_side_bar = QPropertyAnimation(widget, b"minimumWidth", self)
        animation_side_bar.setDuration(duration)
        animation_side_bar.setEasingCurve(type_curve)
        icon = QIcon()
        # DEFINE START PLACE FOR SIDE BAR
        if widget.minimumWidth() == start:
            icon.addPixmap(QPixmap(":/icons/images/arrow_close.png"), QIcon.Normal, QIcon.Off)
            animation_side_bar.setStartValue(start)
            animation_side_bar.setEndValue(end)
        else:
            icon.addPixmap(QPixmap(":/icons/images/arrow_open2.png"), QIcon.Normal, QIcon.Off)
            animation_side_bar.setStartValue(end)
            animation_side_bar.setEndValue(start)
        self.app.close_open_tools_bar_but.setIcon(icon)
        self.app.close_open_tools_bar_but.setIconSize(QSize(15, 15))
        animation_side_bar.start()

    def words_count_function(self):
        """SHOWS COUNT OF WORDS"""
        # COPIES TEXT FROM TEXT_FIELD
        words_text_field_str = self.app.text_field.toPlainText()
        lines = words_text_field_str.count("\n") + 1
        # PATTERN FROM REGULAR EXPRESSION
        pattern = r"\s?\S{1,}\s?"
        # COUNTS LENGTH LIST WORDS / ALSO DOESN'T TAKE SPACE CHARS
        words = len([i for i in re.findall(pattern, words_text_field_str) if i != ""])

        # CHANGE CONDITION OF FILE
        if not self.__file_new:
            self.__is_file_saved = False
        else:
            self.__file_new = False
        # CHANGES WORDS_COUNT ON WORDS CONST
        self.app.words_count.setText(str(words))
        # CHANGES CHARS_COUNT ON LENGTH words_text_field_str
        self.app.chars_count.setText(str(len(words_text_field_str)) + ",")
        # CHANGES COUNT_LINES ON COUNT \n IN words_text_field_str
        self.app.count_lines.setText(str(lines) + ",")

    def change_page(self, page_index):
        """CHANGES THE CURRENT PAGE ON SELECTED"""
        # CHANGE STYLE SHEET OF CHOSEN BUTTON
        self.current_page.setStyleSheet("")
        self.current_page = self.sender()
        self.current_page.setStyleSheet("""
        QPushButton {
            background:rgba(77, 88, 110, 50);
            border-right: 4px solid rgb(77, 88, 110);   
        }
        QPushButton:hover {
            background: rgba(86, 94, 110, 100);
        }
        QPushButton:pressed{
            background: rgba(86, 94, 110, 150);
        }
        """)

        # CHANGE PAGE
        self.app.stackedWidget.setCurrentIndex(page_index)

    def oc_side_bar_menu(self, standard, extended):
        """OPEN/CLOSE THE SIDE BAR MENU"""

        # ANIMATION FOR SIDE BAR
        animation_side_bar = QPropertyAnimation(self.app.side_bar, b"minimumWidth")
        animation_side_bar.setDuration(300)
        animation_side_bar.setEasingCurve(QEasingCurve.OutCirc)

        # ANIMATION FOR STANDARD BUTTONS
        animation_settings_button = QPropertyAnimation(self.app.settings_button, b"minimumWidth")
        animation_settings_button.setDuration(300)
        animation_settings_button.setEasingCurve(QEasingCurve.OutCirc)
        animation_home_button = QPropertyAnimation(self.app.home_button, b"minimumWidth")
        animation_home_button.setDuration(300)
        animation_home_button.setEasingCurve(QEasingCurve.OutCirc)

        # DO PARALLEL ANIMATION
        group_animation = QParallelAnimationGroup(self)
        group_animation.addAnimation(animation_side_bar)
        group_animation.addAnimation(animation_home_button)
        group_animation.addAnimation(animation_settings_button)

        if self.app.side_bar.width() == standard:

            # DEFINE START PLACE FOR THE SIDE BAR
            animation_side_bar.setStartValue(standard)
            animation_side_bar.setEndValue(extended)

            # DEFINE START PLACE FOR THE SETTING BUTTON
            animation_settings_button.setStartValue(standard)
            animation_settings_button.setEndValue(extended)

            # DEFINE START PLACE FOR THE HOME BUTTON
            animation_home_button.setStartValue(standard)
            animation_home_button.setEndValue(extended)

        else:

            # DEFINE START PLACE FOR SIDE BAR
            animation_side_bar.setStartValue(extended)
            animation_side_bar.setEndValue(standard)

            # DEFINE START PLACE FOR THE SETTING BUTTON
            animation_settings_button.setStartValue(extended)
            animation_settings_button.setEndValue(standard)

            # DEFINE START PLACE FOR THE HOME BUTTON
            animation_home_button.setStartValue(extended)
            animation_home_button.setEndValue(standard)

        # START ANIMATION
        group_animation.start()

    def mousePressEvent(self, event):
        """SAVES COORDINATES WHERE YOU PRESSED THE MOUSE"""
        self.clickPosition = event.globalPos()

    def moveWindow(self, event):
        """DRAGS WINDOW WHEN YOU PRESSED THE TITLE BAR"""
        # YOU CAN DRAG THE WINDOW ONLY WHEN YOU ARE PRESSING ON THE TITLE BAR BY LEFT MOUSE BUTTON
        if event.buttons() == Qt.LeftButton:
            # CHECKS ISN'T WINDOW MAXIMUM SIZE
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

                if 0 < x0 and x1 < self.window_width:
                    self.move(x0, event.globalPos().y())
                elif x1 > self.window_width:
                    self.move(self.window_width - self.width(), event.globalPos().y())
                else:
                    self.move(0, event.globalPos().y())
                self.clickPosition = event.globalPos()
                event.accept()

    def change_size_app(self):
        """CHANGES WINDOW SIZE"""
        if self.isMaximized():
            # MAKES PREVIOUS SIZE OF WINDOW
            self.showNormal()
        else:
            # MAKES MAXIMUM WINDOW SIZE
            self.setWindowState(Qt.WindowMaximized)


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Application")
window.setWindowIcon(QIcon(r"C:\Users\Kirill\Desktop\text_ed\images\icons.ico"))
sys.exit(app.exec_())
