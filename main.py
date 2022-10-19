from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])
win = QMainWindow()
win.setGeometry(150, 100, 180, 80)
pub = QPushButton("Hallo", win)
win.setCentralWidget(pub)
win.show()
app.exec()
print("OK")
