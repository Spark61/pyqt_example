import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, \
    QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Ganz viel text")

        self.btn = QPushButton("Bitte klicke hier")
        self.btn.clicked.connect(self.click)

        self.box = QComboBox()

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.addWidget(self.box)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def click(self):
        for i in range(10):
            self.box.addItem("LF " + str(i + 1))
        self.btn.setEnabled(False)
        # self.box.currentTextChanged.connect(self.change)

        self.box.currentTextChanged.connect(self.label.setText)

    def change(self):
        self.label.setText(self.box.currentText())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
