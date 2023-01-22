import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Context menu")

        self.label = QLabel("RClick in this window!")
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        action_1 = QAction("Test 1", self)
        action_2 = QAction("Test 2", self)
        action_3 = QAction("Test 3", self)
        action_4 = QAction("Test 4", self)
        context.addAction(action_1)
        context.addAction(action_2)
        context.addAction(action_3)
        context.addAction(action_4)
        action_1.triggered.connect(self.slot_test_1)
        action_2.triggered.connect(self.slot_test_2)
        action_3.triggered.connect(self.slot_test_3)
        action_4.triggered.connect(self.slot_test_4)
        context.exec(e.globalPos())

    def slot_test_1(self):
        self.label.setText("Selected first item!")

    def slot_test_2(self):
        self.label.setText("Selected second item!")
        
    def slot_test_3(self):
        self.label.setText("Selected third item!")

    def slot_test_4(self):
        self.label.setText("Selected fourth item!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()