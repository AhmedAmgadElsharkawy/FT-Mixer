import pyqtgraph as pg

class CustomImageView(pg.ImageView):
    def __init__(self,double_click_handler):
        super().__init__()
        self.double_click_handler = double_click_handler
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()

    def mouseDoubleClickEvent(self, event):
        self.double_click_handler()