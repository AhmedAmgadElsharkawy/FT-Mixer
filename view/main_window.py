from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtCore import Qt
from view.image_viewer import ImageViewer
from model.image_model import ImageModel
from view.output_port import OutputPort


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_obejcts = [ImageModel(),ImageModel(),ImageModel(),ImageModel()]
        self.setWindowTitle('FT-Mixer')
        self.setGeometry(20, 50, 1900, 950)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)


        self.images_viewers_widget = QWidget()
        self.images_viewers_widget.setObjectName("images_viewers_widget")
        self.images_viewers_widget_layout = QGridLayout(self.images_viewers_widget)
        self.images_viewers_widget_layout.setContentsMargins(0,0,0,0)
        
        
        self.image_viewer1 = ImageViewer(self,self.image_obejcts[0])
        self.image_viewer2 = ImageViewer(self,self.image_obejcts[1])
        self.image_viewer3 = ImageViewer(self,self.image_obejcts[2])
        self.image_viewer4 = ImageViewer(self,self.image_obejcts[3])


        self.images_viewers_widget_layout.addWidget(self.image_viewer1,0,0)
        self.images_viewers_widget_layout.addWidget(self.image_viewer2,0,1)
        self.images_viewers_widget_layout.addWidget(self.image_viewer3,1,0)
        self.images_viewers_widget_layout.addWidget(self.image_viewer4,1,1)

        self.left_output_port = OutputPort(self)
        self.main_layout.addWidget(self.left_output_port)
        self.main_layout.addWidget(self.images_viewers_widget)
        self.right_output_port = OutputPort(self)
        self.main_layout.addWidget(self.right_output_port)
        
        
 
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
            
        """)
        