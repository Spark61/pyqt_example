import random
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget, QPushButton, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formular App")

        rules = ["Strebe nach Konsistenz", "Strebe nach universeller Bedienbarkeit", "Biete informatives Feedback an", "Gesalten sie Dialoge so, dass sie zu einem Abschluss führen", "Verhindere Fehler", "Erlaube die Umkehrung von Aktionen", "Gib dem Ntzer das Gefühl der Kontrolle", "Reduziere die Belastung fpr das Kurzzeitgedächtnis"]

        layout = QGridLayout()

        col = 0

        for rule in rules:
            label = QLabel(rule)

            layout.addWidget(label, 0, col)
            col+=1


        self.label = QLabel("BOX LAYOUT!")
        self.label2 = QLabel("BOX LAYOUT!")

        self.button = QPushButton("Drück mich :)")
        self.button.clicked.connect(self.click)

        layout.addWidget(self.button, 1, 0, 1,col)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def click(self):
        print("Hello World")

        text = self.label.text()
        self.label.setText("")

        for key in list(text):
            if random.randint(0, 1) == 1:
                key = key.upper()
            else:
                key = key.lower()

            self.label.setText(self.label.text() + key)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()