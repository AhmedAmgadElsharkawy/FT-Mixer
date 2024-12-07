from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout
import pyqtgraph as pg


class CustomImageView(pg.ImageView):
    def __init__(self, image_object):
        super().__init__()
        self.image_object = image_object

    def mouseDoubleClickEvent(self, event):
        self.image_object.load_image(self)
        

class ImageViewer(QWidget):
    def __init__(self,main_window,image_obejct):
        super().__init__()
        self.main_window = main_window
        self.central_layout = QHBoxLayout(self)
        self.main_widget = QWidget()      
        self.main_widget_layout = QHBoxLayout(self.main_widget)
        self.central_layout.addWidget(self.main_widget)

        self.image_view_widget = CustomImageView(image_obejct)
        self.image_view_widget.ui.histogram.hide() 
        self.image_view_widget.ui.roiBtn.hide()    
        self.image_view_widget.ui.menuBtn.hide()
        self.main_widget_layout.addWidget(self.image_view_widget)

        self.image_controls_widget = QWidget()
        self.image_controls_widget_layout = QVBoxLayout(self.image_controls_widget)
        self.main_widget_layout.addWidget(self.image_controls_widget)
        

    
            


        