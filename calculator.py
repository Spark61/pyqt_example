from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("ui/Calculator.png"))

        self.calc = uic.loadUi('ui/calculator.ui', self)  # Load the .ui file

        number_btns = [
            "btn_0", "btn_1", "btn_2", "btn_3", "btn_4", "btn_5", "btn_6", "btn_7", "btn_8", "btn_9",
        ]

        for btn in number_btns:
            getattr(self, btn).clicked.connect(self.btn_press)


        operator_btns = [
            "btn_plus", "btn_minus", "btn_mult", "btn_div",
        ]
        for btn in operator_btns:
            getattr(self, btn).clicked.connect(self.operator_btn_press)


        self.btn_point.clicked.connect(self.add_point)
        self.btn_floor.clicked.connect(self.floor_div)
        self.btn_modulo.clicked.connect(self.modulo)
        self.btn_ac.clicked.connect(self.clear_all)
        self.btn_equal.clicked.connect(self.calculate)

        self.show()  # Show the GUI

    def modulo(self):
        if self.label_2.text()[-1] != " ":
            self.show_value(" % ")

    def floor_div(self):
        if self.label_2.text()[-1] != " ":
            self.show_value(" // ")

    def keyPressEvent(self, event: QKeyEvent):
        print(event.key())

        if event.key() == Qt.Key_0:
            self.show_value("0")
        if event.key() == Qt.Key_1:
            self.show_value("1")
        if event.key() == Qt.Key_2:
            self.show_value("2")
        if event.key() == Qt.Key_3:
            self.show_value("3")
        if event.key() == Qt.Key_4:
            self.show_value("4")
        if event.key() == Qt.Key_5:
            self.show_value("5")
        if event.key() == Qt.Key_6:
            self.show_value("6")
        if event.key() == Qt.Key_7:
            self.show_value("7")
        if event.key() == Qt.Key_8:
            self.show_value("8")
        if event.key() == Qt.Key_9:
            self.show_value("9")
        if event.key() == 40:
            self.show_value("(")
        if event.key() == 41:
            self.show_value(")")
        if event.key() == 94:
            self.show_value("^")
        if event.key() == Qt.Key_Plus and self.label_2.text()[-1] != " ":
            self.show_value(" + ")
        if event.key() == Qt.Key_Minus and self.label_2.text()[-1] != " ":
            self.show_value(" - ")
        if event.key() == 42 and self.label_2.text()[-1] != " ":  # *
            self.show_value(" * ")
        if event.key() == Qt.Key_Slash and self.label_2.text()[-1] != " ":
            self.show_value(" / ")
        if event.key() == 16777216:  # Escape
            self.clear_all()
        if event.key() == 46:  # Point
            self.add_point()
        if event.key() == Qt.Key_Equal or event.key() == 16777220:
            self.calculate()
        if event.key() == Qt.Key_Backspace:
            self.label_2.setText(self.label_2.text().strip()[:-1].strip())

    def add_point(self):
        if "." in self.label_2.text().split(" ")[-1]:
            return

        if self.label_2.text().split(" ")[-1] == "":
            self.show_value("0.")
        else:
            self.show_value(".")

    def clear_all(self):
        self.label_1.setText("0")
        self.label_2.setText("")

    def operator_btn_press(self):
        content = self.sender().text()

        if self.label_2.text()[-1] != " ":
            self.show_value(content)

    def btn_press(self):
        self.show_value(self.sender().text())

    def show_value(self, content):
        self.label_2.setText(self.label_2.text() + content)

    def calculate(self):
        if self.label_2.text() == "":
            self.label_1.setText("0")
        else:
            content = self.label_2.text().replace("^", "**")

            self.label_1.setText(str(eval(content)))


app = QApplication([])
w = MainWindow()
w.show()
app.exec()
