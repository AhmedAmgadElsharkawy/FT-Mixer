from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FT-Mixer')
        self.setGeometry(50, 50, 1800, 950)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)
        
 
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
        """)
        