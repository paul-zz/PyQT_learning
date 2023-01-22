import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Direct Connection")

        self.text_edit = QLineEdit()
        self.label = QLabel()
        self.text_edit.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()