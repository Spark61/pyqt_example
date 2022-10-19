import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QWidget, \
    QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Bitte schreibe etwas in die Eingabezeile")

        self.btn = QPushButton("noch nicht aktiv")
        self.btn.setEnabled(False)

        self.input = QLineEdit("")
        self.input.textChanged.connect(self.text_change)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.addWidget(self.input)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def text_change(self):
        self.btn.setText("Jetzt kannst du hier klicken")
        self.btn.setEnabled(True)

        self.label.setText(self.input.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
