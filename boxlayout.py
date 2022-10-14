import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication(sys.argv)
win = QWidget()

layout = QHBoxLayout(win)

texts = ["One", "Two", "Three", "Four", "Five"]

for text in texts:
    but = QPushButton(text)

    layout.addWidget(but)
    layout.addStretch()
win.show()
sys.exit(app.exec_())
