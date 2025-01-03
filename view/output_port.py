from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton,QButtonGroup,QComboBox,QSlider,QSizePolicy,QGroupBox
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import numpy as np
from controller.output_port_controller import OutputPortController 
import logging
logger = logging.getLogger(__name__)

class Component(QWidget):
    def __init__(self,header, output_port):
        super().__init__()
        self.output_port = output_port
        self.central_widget_layout  = QVBoxLayout(self)
        self.component_main_widget = QWidget()
        self.component_main_widget_layout = QVBoxLayout(self.component_main_widget)
        self.component_main_widget.setObjectName("component_main_widget")
        
        self.central_widget_layout.addWidget(self.component_main_widget)
        self.header_widget = QWidget()
        self.header_widget_layout = QHBoxLayout(self.header_widget)
        self.header_widget_layout.setContentsMargins(0,0,0,0)
        self.header_label = QLabel(header)
        self.component_combobox = QComboBox()
        self.component_combobox.addItems(["Magnitude","Phase"])
        self.header_widget_layout.addWidget(self.header_label)
        self.header_widget_layout.addWidget(self.component_combobox)
        self.component_main_widget_layout.addWidget(self.header_widget)
        
        self.slider_container = QWidget()
        self.slider_container_layout = QHBoxLayout(self.slider_container)
        self.slider_container_layout.setContentsMargins(0,0,0,0)
        self.component_main_widget_layout.addWidget(self.slider_container)
        
        self.component_slider = QSlider(Qt.Horizontal)
        self.component_slider_label = QLabel("0%")
        self.component_slider.setRange(0,100)
        self.component_slider.setValue(0)
        self.component_slider.setSingleStep(1)
        # self.component_slider.setEnabled(False) 
        
        self.slider_container_layout.addWidget(self.component_slider)
        self.slider_container_layout.addSpacing(25)
        self.slider_container_layout.addWidget(self.component_slider_label)
        self.component_slider.setFixedWidth(250)
        self.component_slider.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.component_slider.valueChanged.connect(self.slider_change)
        self.component_combobox.currentIndexChanged.connect(self.output_port.output_controller.change_mixer)

        self.setStyleSheet("""
                           #component_main_widget{
                            border: 1px solid gray;
                           border-radius:7px;
                           }
                           """)
        
    def slider_change(self):
        logger.info("The component's slider has been changed")
        self.output_port.output_controller.change_mixer()
        self.component_slider_label.setText(f"{self.component_slider.value()}%")

class OutputPort(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.components_list = []
        self.main_window = main_window
        self.output_controller = OutputPortController(self)
        self.components = [Component("component1", self),Component("component2", self),Component("component3", self),Component("component4", self)]
        self.central_layout = QVBoxLayout(self)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.main_widget = QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.main_widget_layout.setContentsMargins(0,0,0,0)
        self.central_layout.addWidget(self.main_widget)
        self.main_widget.setFixedWidth(350)

        self.output_viwer = pg.ImageView()
        self.output_viwer.ui.histogram.hide() 
        self.output_viwer.ui.roiBtn.hide()    
        self.output_viwer.ui.menuBtn.hide()
        self.output_viwer.setFixedHeight(350)
        self.main_widget_layout.addWidget(self.output_viwer)

        self.choose_mode_widget = QWidget()
        self.choose_mode_widget.setFixedHeight(50)
        self.choose_mode_widget.setObjectName("choose_mode_widget")
        self.choose_mode_widget_layout = QHBoxLayout(self.choose_mode_widget)
        self.main_widget_layout.addWidget(self.choose_mode_widget)
        
        self.choose_mode_label = QLabel("Mixer Mode:")
        self.choose_mode_widget_layout.addWidget(self.choose_mode_label)

        self.magnitude_and_phase_radio = QRadioButton("Mag/Phase")
        self.real_and_imaginary_radio = QRadioButton("Real/imag")
        self.choose_mode_widget_layout.addWidget(self.magnitude_and_phase_radio)
        self.choose_mode_widget_layout.addWidget(self.real_and_imaginary_radio)
    
        self.choose_mode_radio_buttons_group = QButtonGroup()
        self.choose_mode_radio_buttons_group.setExclusive(True)
        self.choose_mode_radio_buttons_group.addButton(self.magnitude_and_phase_radio)
        self.choose_mode_radio_buttons_group.addButton(self.real_and_imaginary_radio)

        self.magnitude_and_phase_radio.setChecked(True)

        self.choose_mixer_region_widget = QWidget()
        self.choose_mixer_region_widget_layout = QHBoxLayout(self.choose_mixer_region_widget)
        self.choose_mixer_region_widget.setFixedHeight(50)
        self.choose_mixer_region_widget.setObjectName("choose_mixer_region_widget")
        self.main_widget_layout.addWidget(self.choose_mixer_region_widget)
        self.choose_mixer_region_label = QLabel("Mixer Region:")
        self.choose_mixer_region_widget_layout.addWidget(self.choose_mixer_region_label)

        self.inner_region_mode_radio_button = QRadioButton("Inner Mode")
        self.outter_region_mode_radio_button = QRadioButton("Outter Mode")
        self.choose_mixer_region_widget_layout.addWidget(self.inner_region_mode_radio_button)
        self.choose_mixer_region_widget_layout.addWidget(self.outter_region_mode_radio_button)
    
        self.choose_mixer_region_radio_buttons_group = QButtonGroup()
        self.choose_mixer_region_radio_buttons_group.setExclusive(True)
        self.choose_mixer_region_radio_buttons_group.addButton(self.inner_region_mode_radio_button)
        self.choose_mixer_region_radio_buttons_group.addButton(self.outter_region_mode_radio_button)

        self.inner_region_mode_radio_button.setChecked(True)

        self.components_widget = QWidget()
        self.components_widget.setObjectName("components_widget")
        self.components_widget_layout = QVBoxLayout(self.components_widget)
        self.components_widget_layout.setContentsMargins(0,0,0,0)
        self.main_widget_layout.addWidget(self.components_widget)

        for component in self.components:
            self.components_widget_layout.addWidget(component)
            component.setDisabled(True)

        self.magnitude_and_phase_radio.toggled.connect(self.output_controller.set_to_magnitude_and_phase)
        self.real_and_imaginary_radio.toggled.connect(self.output_controller.set_to_real_and_Imaginary)
        self.inner_region_mode_radio_button.toggled.connect(self.output_controller.roi_changed)
        self.outter_region_mode_radio_button.toggled.connect(self.output_controller.roi_changed)

        # self.choose_mode_radio_buttons_group.buttonClicked.connect(self.update_status)

        self.setStyleSheet("""
            #choose_mode_widget{
                border:1px solid gray;
                border-radius:7px;
            }
            #components_widget{
                 border:1px solid gray;
                border-radius:7px;          
                }
            #choose_mixer_region_widget{
                border:1px solid gray;
                border-radius:7px;
                }
        """)

    def enable_component_by_index(self,index):
        self.components[index].setEnabled(True)
        
