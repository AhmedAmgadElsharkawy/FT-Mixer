from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QComboBox,QSlider,QLabel
import pyqtgraph as pg
from PyQt5.QtCore import Qt



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
        ft_components_options = ["FT Magnitude", "FT Phase", "FT Real Components", "FT Imaginary Components"]
        self.ft_components_combobox = QComboBox()
        self.ft_components_combobox.addItems(ft_components_options)
        self.image_controls_widget_layout.addWidget(self.ft_components_combobox)

        self.brightness_control_widget = QWidget()
        self.brightness_control_widget_layout = QHBoxLayout(self.brightness_control_widget)
        self.contrast_control_widget = QWidget()
        self.contrast_control_widget_layout = QHBoxLayout(self.contrast_control_widget)
        self.image_controls_widget_layout.addWidget(self.brightness_control_widget)
        self.image_controls_widget_layout.addWidget(self.contrast_control_widget)

        self.brightness_label = QLabel("Brightness")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(-100, 100) 
        self.brightness_slider.setValue(0) 
        self.brightness_control_widget_layout.addWidget(self.brightness_label)
        self.brightness_control_widget_layout.addWidget(self.brightness_slider)
        
        self.contrast_label = QLabel("Contrast")
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setRange(1, 500)  
        self.contrast_slider.setValue(100)  
        self.contrast_control_widget_layout.addWidget(self.contrast_label)
        self.contrast_control_widget_layout.addWidget(self.contrast_slider)
        
        
        

        
        
        

    
            


        