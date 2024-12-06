from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
        """)
        