import pyqtgraph as pg
from view.custom_view import CustomView

class CustomImageView(CustomView):
    def __init__(self,double_click_handler):
        super().__init__()
        self.double_click_handler = double_click_handler

    def mouseDoubleClickEvent(self, event):
        self.double_click_handler()