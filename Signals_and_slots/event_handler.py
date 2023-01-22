import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Event Handler")

        self.label = QLabel("Click in this window!")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mousePressEvent L")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent M")
        elif e.button() == Qt.RightButton:
            self.label.setText("mousePressEvent R")
            
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()