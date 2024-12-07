from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph as pg



class OutputPort(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.central_layout = QVBoxLayout(self)
        self.main_widget = QWidget()
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.central_layout.addWidget(self.main_widget)
        self.main_widget.setFixedWidth(350)

        self.output_viwer = pg.ImageView()
        self.output_viwer.ui.histogram.hide() 
        self.output_viwer.ui.roiBtn.hide()    
        self.output_viwer.ui.menuBtn.hide()
        self.main_widget_layout.addWidget(self.output_viwer)
        
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
        """)
        
