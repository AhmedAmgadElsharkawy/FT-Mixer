from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QComboBox,QSlider,QLabel
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from controller.image_viewer_controller import ImageViewerController



class CustomImageView(pg.ImageView):
    def __init__(self, image_viewer_controller,image_object):
        super().__init__()
        self.image_viewer_controller = image_viewer_controller
        self.image_object = image_object
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()

    def mouseDoubleClickEvent(self, event):
        self.image_object.load_image()
        if self.image_object.imgPath:
            self.image_viewer_controller.plot_image()

class CustomFTViewer(pg.ImageView):
    def __init__(self):
        super().__init__()
        self.ft_roi = pg.ROI(pos = self.getView().viewRect().center(), size = (300, 300), hoverPen='b', resizable= True, invertible= True, rotatable= False)
        self.addItem(self.ft_roi)
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()
        
class ImageViewer(QWidget):
    def __init__(self,main_window,image_object):
        super().__init__()
        self.image_viewer_controller = ImageViewerController(self)
        self.main_window = main_window
        self.image_object = image_object
        self.central_layout = QHBoxLayout(self)
        self.main_widget = QWidget()      
        self.main_widget_layout = QHBoxLayout(self.main_widget)
        self.central_layout.addWidget(self.main_widget)

        self.image_view_widget = CustomImageView(self.image_viewer_controller,self.image_object)
        self.main_widget_layout.addWidget(self.image_view_widget)


        self.ft_viewer = CustomFTViewer()
        self.main_widget_layout.addWidget(self.ft_viewer)



        self.image_controls_widget = QWidget()
        self.image_controls_widget_layout = QVBoxLayout(self.image_controls_widget)
        self.main_widget_layout.addWidget(self.image_controls_widget)
        ft_components_options = ["FT Magnitude", "FT Phase", "FT Real", "FT Imaginary"]
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

        self.ft_components_combobox.currentIndexChanged.connect(self.image_viewer_controller.select_ft_component)
        
        

        
        
        

    
            


        