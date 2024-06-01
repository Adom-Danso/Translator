from PyQt5 import QtCore, QtGui, QtWidgets
from error import Ui_Dialog
import translators as ts 
import sqlite3

# _ = ts.preaccelerate_and_speedtest()
conn = sqlite3.connect('database.db')
cur = conn.cursor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 405)
        MainWindow.setMinimumSize(QtCore.QSize(455, 375))
        MainWindow.setMaximumSize(QtCore.QSize(455, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("translation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #4A4A4A ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userInput = QtWidgets.QTextEdit(self.centralwidget)
        self.userInput.setGeometry(QtCore.QRect(5, 33, 445, 140))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(12)
        self.userInput.setFont(font)
        self.userInput.setStyleSheet("border: 1px solid gray;\n"
        "border-radius: 10px;\n"
        "padding: 0 8px;\n"
        "background: 6F6D6D;\n"
        "background-color: #6F6D6D;\n"
        "selection-background-color: darkgray; \n"
        "color: white;")
        self.userInput.setFrameShape(QtWidgets.QFrame.VLine)
        self.userInput.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.userInput.setLineWidth(1)
        self.userInput.setMidLineWidth(-1)
        self.userInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userInput.setObjectName("userInput")
        self.translated_output = QtWidgets.QTextEdit(self.centralwidget)
        self.translated_output.setGeometry(QtCore.QRect(5, 210, 445, 140))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(12)
        self.translated_output.setFont(font)
        self.translated_output.setStyleSheet("border: 1px solid gray;\n"
        "border-radius: 10px;\n"
        "padding: 0 8px;\n"
        "background: 6F6D6D;\n"
        "background-color: #6F6D6D;\n"
        "selection-background-color: darkgray; \n"
        "color: white;")
        self.translated_output.setFrameShape(QtWidgets.QFrame.VLine)
        self.translated_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.translated_output.setLineWidth(1)
        self.translated_output.setMidLineWidth(0)
        self.translated_output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.translated_output.setReadOnly(True)
        self.translated_output.setObjectName("translated_output")
        self.from_language = QtWidgets.QComboBox(self.centralwidget)
        self.from_language.setGeometry(QtCore.QRect(75, 5, 92, 17))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        self.from_language.setFont(font)
        self.from_language.setStyleSheet("QComboBox {color: white; background-color: #6F6D6D; padding: 2px; padding-left: 4px; border: 1px solid #6F6D6D; border-radius: 8px;}")
        self.from_language.setCurrentText("")
        self.from_language.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.from_language.setDuplicatesEnabled(False)
        self.from_language.setFrame(False)
        self.from_language.setObjectName("from_language")
        self.to_language = QtWidgets.QComboBox(self.centralwidget)
        self.to_language.setGeometry(QtCore.QRect(87, 183, 92, 17))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        self.to_language.setFont(font)
        self.to_language.setStyleSheet("QComboBox {color: white; background-color: #6F6D6D; padding: 2px; padding-left: 4px; border: 1px solid #6F6D6D; border-radius: 8px;}")
        self.to_language.setCurrentText("")
        self.to_language.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.to_language.setDuplicatesEnabled(False)
        self.to_language.setFrame(False)
        self.to_language.setObjectName("to_language")
        self.translation_label = QtWidgets.QLabel(self.centralwidget)
        self.translation_label.setGeometry(QtCore.QRect(10, 180, 74, 25))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.translation_label.setFont(font)
        self.translation_label.setStyleSheet("color: white;")
        self.translation_label.setObjectName("translation_label")
        self.language_label = QtWidgets.QLabel(self.centralwidget)
        self.language_label.setGeometry(QtCore.QRect(10, 5, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.language_label.setFont(font)
        self.language_label.setStyleSheet("color: white")
        self.language_label.setObjectName("language_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.translate())
        self.pushButton.setGeometry(QtCore.QRect(190, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" QPushButton {color: white;  border: 1px solid #6F6D6D; border-radius: 5px;} QPushButton:hover {color: #6F6D6D; background-color: white; }")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.from_language.addItems(self.get_languages())
        self.to_language.addItems(self.get_languages())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        self.userInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Gabriola\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.userInput.setPlaceholderText(_translate("MainWindow", "Type here to translate..."))
        self.translated_output.setPlaceholderText(_translate("MainWindow", "Translation..."))
        self.translation_label.setText(_translate("MainWindow", "Translate to"))
        self.language_label.setText(_translate("MainWindow", "Language"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        
    def get_languages(self):
        res = cur.execute("SELECT language FROM Languages")
        result = res.fetchall()
        languages = []
        for item in result:
            languages.append(item[0].capitalize())
        return languages
    
    def translate(self):
        text = self.userInput.toPlainText()
        
        from_language = cur.execute("SELECT shorthand FROM Languages WHERE language = :from_language", {'from_language': self.from_language.currentText().lower()}).fetchone()
        
        to_language = cur.execute("SELECT shorthand FROM Languages WHERE language = :from_language", {'from_language': self.to_language.currentText().lower()}).fetchone()
        
        if from_language != to_language:
            self.translated_output.setText(f"{ts.translate_text(text, translator='google', from_language=from_language[0], to_language=to_language[0], if_use_preacceleration=False)}")
        else:
            self.error_message()
    
    def error_message(self):
        self.Dialog =  QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
