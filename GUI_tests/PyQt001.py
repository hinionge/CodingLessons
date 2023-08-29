# 28.8.2023

# Well, this worked immediately



from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("Click here to close")
        button.clicked.connect(self.close)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()