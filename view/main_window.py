from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt
from view.image_viewer import ImageViewer
from model.image_model import ImageModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_obejcts = [ImageModel(),ImageModel(),ImageModel(),ImageModel()]
        self.setWindowTitle('FT-Mixer')
        self.setGeometry(50, 50, 1800, 950)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)
        self.image_viewer1 = ImageViewer(self,self.image_obejcts[0])
        self.main_layout.addWidget(self.image_viewer1)
        
 
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
        """)
        