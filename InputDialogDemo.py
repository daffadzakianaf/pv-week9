from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog
import sys

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("tampilan.ui", self)

        # Koneksi tombol ke fungsi
        self.btnChooseFromList.clicked.connect(self.showComboDialog)
        self.btnGetName.clicked.connect(self.showTextDialog)
        self.btnEnterInteger.clicked.connect(self.showIntegerDialog)

    def showComboDialog(self):
        languages = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages", languages, 0, False)
        if ok and item:
            self.lineEditList.setText(item)

    def showTextDialog(self):
        name, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and name:
            self.lineEditName.setText(name)

    def showIntegerDialog(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number:")
        if ok:
            self.lineEditInteger.setText(str(num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.show()
    sys.exit(app.exec())
