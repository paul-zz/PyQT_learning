import sys
from random import choice
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "我的应用",
    "我的应用",
    "我的Qt窗口应用",
    "你好哦",
    "Oh no!"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我的应用")

        self.button = QPushButton("点击我更换标题")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.window_title_changed)

        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        self.setCentralWidget(self.button)

    def button_clicked(self):
        new_window_title = choice(window_titles)
        self.setWindowTitle(new_window_title)

    def window_title_changed(self, window_title):
        print("Title changed!")
        if window_title == "Oh no!":
            self.button.setText("出错了，别按了！")
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()