from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from view.image_viewer import ImageViewer
from model.image_model import ImageModel
from view.output_port import OutputPort
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.viewports = []
        self.image_obejcts = [ImageModel(), ImageModel(), ImageModel(), ImageModel()]
        self.setWindowTitle('FT-Mixer')
        self.setGeometry(20, 50, 1900, 950)
        
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.setSpacing(20)

        # Left Output Port
        self.left_output_port = OutputPort(self)
        self.main_layout.addWidget(self.left_output_port)

        # Central Images Viewers Widget
        self.images_viewers_widget = QWidget()
        self.images_viewers_widget.setObjectName("images_viewers_widget")
        self.images_viewers_widget_layout = QGridLayout(self.images_viewers_widget)
        self.images_viewers_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.image_viewer1 = ImageViewer(self, self.image_obejcts[0])
        self.image_viewer2 = ImageViewer(self, self.image_obejcts[1])
        self.image_viewer3 = ImageViewer(self, self.image_obejcts[2])
        self.image_viewer4 = ImageViewer(self, self.image_obejcts[3])

        self.image_viewer1.ft_viewer.sig_emitter.sig_ROI_changed.connect(lambda i=1, v=self.image_viewer1.ft_viewer: self.modify_all_regions(v.getRoi()))
        self.image_viewer2.ft_viewer.sig_emitter.sig_ROI_changed.connect(lambda i=2, v=self.image_viewer2.ft_viewer: self.modify_all_regions(v.getRoi()))
        self.image_viewer3.ft_viewer.sig_emitter.sig_ROI_changed.connect(lambda i=3, v=self.image_viewer3.ft_viewer: self.modify_all_regions(v.getRoi()))
        self.image_viewer4.ft_viewer.sig_emitter.sig_ROI_changed.connect(lambda i=4, v=self.image_viewer4.ft_viewer: self.modify_all_regions(v.getRoi()))

        self.viewports.append(self.image_viewer1.ft_viewer)
        self.viewports.append(self.image_viewer2.ft_viewer)
        self.viewports.append(self.image_viewer3.ft_viewer)
        self.viewports.append(self.image_viewer4.ft_viewer)

        self.images_viewers_widget_layout.addWidget(self.image_viewer1, 0, 0)
        self.images_viewers_widget_layout.addWidget(self.image_viewer2, 0, 1)
        self.images_viewers_widget_layout.addWidget(self.image_viewer3, 1, 0)
        self.images_viewers_widget_layout.addWidget(self.image_viewer4, 1, 1)

        self.main_layout.addWidget(self.images_viewers_widget)

        # Right Output Port
        self.right_output_port = OutputPort(self)
        self.main_layout.addWidget(self.right_output_port)

        # Apply Dark Theme Stylesheet
                # Apply Dark Theme Stylesheet with Disabled States
                # Apply Dark Theme Stylesheet with Disabled States
                # Apply Dark Theme Stylesheet with Disabled States
                # Apply Dark Theme Stylesheet with Disabled States
        self.setStyleSheet("""
            * {
                background-color: #121212;
                color: #E0E0E0;
                font-family: Arial;
            }
            QMainWindow {
                background-color: #121212;
            }
            QWidget {
                background-color: #1E1E1E;
            }
            QLabel {
                color: #E0E0E0;
                font-weight: bold;
                border: none;
            }
            QGridLayout {
                spacing: 10px;
            }

            QPushButton {
                background-color: #1E1E1E;
                color: #E0E0E0;
                border: 1px solid #444;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #252525;
            }
            QPushButton:disabled {
                background-color: #3E3E3E;
                color: #777;
                border: 1px solid #555;
            }

            QComboBox {
                background: #444;
                color: #E0E0E0;
                border: 1px solid #666;
                padding: 2px 5px;
                border-radius: 5px;
                min-width: 100px;
            }
            QComboBox QAbstractItemView {
                background: #333;
                color: #E0E0E0;
                selection-background-color: #555;
            }
            QComboBox QAbstractItemView::item {
                padding: 2px 5px;
                background: transparent;
            }
            QComboBox QAbstractItemView::item:selected {
                background: #555;
            }
            QComboBox:disabled {
                background: #2E2E2E;
                color: #777;
                border: 1px solid #444;
            }

            QSlider::groove:horizontal {
                height: 8px;
                background: #444;
                margin: 0px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: rgb(4,124,212);
                width: 12px;
                height: 12px;
                border-radius: 6px;
                margin: -6px 0;
                border: 1px solid #2a2a2a;
            }
            QSlider::handle:horizontal:hover {
                background: #777;
            }
            QSlider::handle:horizontal:disabled {
                background: #555;
                border: 1px solid #444;
            }

            /* RadioButton */
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
            }
            
            QRadioButton::indicator:unchecked {
                border: 1px solid #666;
                background: #FFFFFF;  /* White center when not selected */
                border-radius: 10px;
            }
            
            QRadioButton::indicator:checked {
                background: #047CD4;  /* Blue color when selected */
                border-radius: 10px;
            }
            
            QRadioButton::indicator:disabled {
                background: #555;
                border: 1px solid #444;
            }
        """)

    def modify_all_regions(self, roi: pg.ROI):
        new_state = roi.getState()
        for view in self.viewports:
            if view.getRoi() is not roi:
                view.getRoi().setState(new_state, update = False) # Set the state of the other views without sending update signal
                view.getRoi().stateChanged(finish = False) # Update the views after changing without sending stateChangeFinished signal
                view.region_update(view.getRoi(),finish = False)    


