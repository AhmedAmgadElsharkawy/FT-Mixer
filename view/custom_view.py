import pyqtgraph as pg

class CustomView(pg.ImageView):
    def __init__(self):
        super().__init__()
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()