from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt


class OutputPort(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        
