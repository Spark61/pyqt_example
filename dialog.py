from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFontDialog, \
    QColorDialog, QFileDialog


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("MiniProg")
        self.setWindowIcon(QIcon("sample.png"))

        self.pfo = QPushButton("Schriftart", self)
        self.pfo.move(50, 20)
        self.pfo.clicked.connect(self.clickedFont)

        self.pco = QPushButton("Wähle Farbe", self)
        self.pco.move(300, 20)
        self.pco.clicked.connect(self.clickedColor)

        self.colLabel = QLabel("etwas Farbe:", self)
        self.colLabel.setGeometry(50, 45, 600, 50)

        self.pfi = QPushButton("Wähle Datei", self)
        self.pfi.move(550, 20)
        self.pfi.clicked.connect(self.clickedFile)

        self.imgLabel = QLabel("das Bild:", self)
        self.imgLabel.setGeometry(50, 100, 600, 500)

    def clickedFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.pfo.setFont(font)

    def clickedColor(self):
        col = QColorDialog.getColor()
        print(col)
        if col.isValid():
            print("col")
            print(col.name())
            self.colLabel.setStyleSheet("QWidget {background-color: %s}" % col.name())

    def clickedFile(self):
        fname, types = QFileDialog.getOpenFileName(self, "öffne", "E:\\", "nur Bilder (*,jpg *.png)")
        self.imgLabel.setPixmap(QPixmap(fname))
        print(fname, types)


app = QApplication([])
w = Fenster()
w.show()
app.exec()
