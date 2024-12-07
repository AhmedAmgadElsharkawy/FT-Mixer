from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt
import pyqtgraph as pg



class OutputPort(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.central_layout = QVBoxLayout(self)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.main_widget = QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.central_layout.addWidget(self.main_widget)
        self.main_widget.setFixedWidth(350)

        self.output_viwer = pg.ImageView()
        self.output_viwer.ui.histogram.hide() 
        self.output_viwer.ui.roiBtn.hide()    
        self.output_viwer.ui.menuBtn.hide()
        self.main_widget_layout.addWidget(self.output_viwer)

        self.choose_mode_widget = QWidget()
        self.choose_mode_widget.setObjectName("choose_mode_widget")
        self.choose_mode_widget_layout = QHBoxLayout(self.choose_mode_widget)
        self.main_widget_layout.addWidget(self.choose_mode_widget)
        
        self.choose_mode_label = QLabel("Choose Mode:")
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

        # self.choose_mode_radio_buttons_group.buttonClicked.connect(self.update_status)
        
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
            #main_widget{
                border:1px solid gray;
                border-radius:10px
            }
            #choose_mode_widget{
                border:1px solid gray;
                border-radius:7px
            }
        """)
        
