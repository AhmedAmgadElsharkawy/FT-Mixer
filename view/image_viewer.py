from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QComboBox,QSlider,QLabel
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from controller.image_viewer_controller import ImageViewerController
import numpy as np



class CustomImageView(pg.ImageView):
    def __init__(self,double_click_handler):
        super().__init__()
        self.double_click_handler = double_click_handler
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()

    def mouseDoubleClickEvent(self, event):
        self.double_click_handler()
        

class CustomFTViewer(pg.ImageView):
    def __init__(self):
        super().__init__()
        self.ft_roi = pg.ROI(pos = self.getView().viewRect().center(), size = (300, 300), hoverPen='r', resizable= True, invertible= True, rotatable= False)
        self.addItem(self.ft_roi)
        self.add_scale_handles_ROI(self.ft_roi)
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()

    def add_scale_handles_ROI(self, roi : pg.ROI):
        positions = np.array([[0,0], [1,0], [1,1], [0,1]])
        for pos in positions:        
            self.ft_roi.addScaleHandle(pos = pos, center = 1 - pos)
        
class ImageViewer(QWidget):
    def __init__(self,main_window,image_object):
        super().__init__()
        self.main_window = main_window
        self.image_object = image_object
        self.central_layout = QVBoxLayout(self)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.main_widget = QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.central_layout.addWidget(self.main_widget)

        self.viwers_widget = QWidget()
        self.viwers_widget_layout = QHBoxLayout(self.viwers_widget)
        self.viwers_widget_layout.setContentsMargins(0,0,0,0)
        self.main_widget_layout.addWidget(self.viwers_widget)

        self.image_view_widget = CustomImageView(self.double_click_image_handler)
        self.viwers_widget_layout.addWidget(self.image_view_widget)


        self.ft_viewer = CustomFTViewer()
        self.ft_viewer.setObjectName("ft_viewer")
        self.viwers_widget_layout.addWidget(self.ft_viewer)



        self.image_controls_widget = QWidget()
        self.image_controls_widget.setObjectName("image_controls_widget")
        self.image_controls_widget_layout = QVBoxLayout(self.image_controls_widget)
        self.image_controls_widget_layout.setContentsMargins(0,0,0,0)
        self.main_widget_layout.addWidget(self.image_controls_widget)

        self.component_combobox_container = QWidget()
        self.component_combobox_container.setObjectName("component_combobox_container")
        self.component_combobox_container_layout = QHBoxLayout(self.component_combobox_container)
        # self.component_combobox_container_layout.setContentsMargins(0,0,0,0)
        self.image_controls_widget_layout.addWidget(self.component_combobox_container)
        ft_components_options = ["FT Magnitude", "FT Phase", "FT Real", "FT Imaginary"]
        self.ft_components_combobox = QComboBox()
        self.ft_components_combobox.addItems(ft_components_options)
        self.component_combobox_label = QLabel("Choose FT Component") 
        self.component_combobox_container_layout.addWidget(self.component_combobox_label)
        self.component_combobox_container_layout.addWidget(self.ft_components_combobox)

        self.sliders_widget = QWidget()
        self.sliders_widget.setObjectName("sliders_widget")
        self.sliders_widget_layout = QHBoxLayout(self.sliders_widget) 
        # self.sliders_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.image_controls_widget_layout.addWidget(self.sliders_widget)


        self.brightness_control_widget = QWidget()
        self.brightness_control_widget_layout = QHBoxLayout(self.brightness_control_widget)
        self.brightness_control_widget_layout.setContentsMargins(0,0,0,0)
        self.contrast_control_widget = QWidget()
        self.contrast_control_widget_layout = QHBoxLayout(self.contrast_control_widget)
        self.contrast_control_widget_layout.setContentsMargins(0,0,0,0)
        self.sliders_widget_layout.addWidget(self.brightness_control_widget)
        self.sliders_widget_layout.addWidget(self.contrast_control_widget)

        self.brightness_label = QLabel("Brightness")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(-100, 100) 
        self.brightness_slider.setValue(0) 
        self.brightness_control_widget_layout.addWidget(self.brightness_label)
        self.brightness_control_widget_layout.addStretch()
        self.brightness_control_widget_layout.addWidget(self.brightness_slider)
        self.brightness_slider.setFixedWidth(150)
        
        self.contrast_label = QLabel("Contrast")
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setRange(1, 300)  
        self.contrast_slider.setValue(100)  
        self.contrast_control_widget_layout.addWidget(self.contrast_label)
        self.contrast_control_widget_layout.addStretch()
        self.contrast_control_widget_layout.addWidget(self.contrast_slider)
        self.contrast_slider.setFixedWidth(150)
        self.image_viewer_controller = ImageViewerController(self)
        self.contrast_slider.valueChanged.connect(self.image_viewer_controller.change_contrast_and_brightness)
        self.brightness_slider.valueChanged.connect(self.image_viewer_controller.change_contrast_and_brightness)
        
        self.setStyleSheet("""
            #main_widget{
                border:1px solid gray;
                border-radius:10px;
                           }
                #component_combobox_container{
                     border:1px solid gray;
                border-radius:5px;      
                           }
                #sliders_widget{
                        border:1px solid gray;
                border-radius:5px;   
                        }
        """)
    
    def double_click_image_handler(self):
        self.image_object.load_image()
        if self.image_object.imgPath:
            self.image_viewer_controller.plot_image()


        
        
        

    
            


        