import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtGui import QPixmap


class SettingsDialog(QMainWindow):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        loadUi("settings.ui", self)
        self.saveButton.clicked.connect(self.saveSettings)

    def saveSettings(self):
        print("save settings")
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test.ui", self)

        self.startGameButton.clicked.connect(self.startGame)
        self.settingsButton.clicked.connect(self.openSettings)

    def startGame(self):
        print("start")

    def openSettings(self):
        print("settings")
        settingsDialog.exec_()


app = QApplication(sys.argv)
mainwindow = MainWindow()
settingsDialog = SettingsDialog()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1366)
widget.setFixedHeight(768)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")