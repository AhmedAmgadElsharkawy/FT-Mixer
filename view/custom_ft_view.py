from PyQt5.QtCore import QObject, pyqtSignal
import pyqtgraph as pg
import numpy as np


class SignalEmitter(QObject):
    sig_ROI_changed = pyqtSignal()

class CustomFTViewer(pg.ImageView):
    def __init__(self):
        super().__init__()
        self.sig_emitter = SignalEmitter()
        self.ft_roi = pg.ROI(pos = self.getView().viewRect().center(), size = (300, 300), hoverPen='r', resizable= True, invertible= True, rotatable= False)
        self.addItem(self.ft_roi)
        self.add_scale_handles_ROI(self.ft_roi)
        self.ui.histogram.hide() 
        self.ui.roiBtn.hide()    
        self.ui.menuBtn.hide()
        self.ft_roi.sigRegionChangeFinished.connect(lambda: self.region_update(self.ft_roi,finish = True))
        self.y1 = 0
        self.y2 = 1
        self.x1 = 0
        self.x2 = 1

    def getRoi(self):
        return self.ft_roi

    def add_scale_handles_ROI(self, roi : pg.ROI):
        positions = np.array([[0,0], [1,0], [1,1], [0,1]])
        for pos in positions:        
            self.ft_roi.addScaleHandle(pos = pos, center = 1 - pos)

    def region_update(self,ft_roi , finish = False):
        if finish:
            self.sig_emitter.sig_ROI_changed.emit()
        bounds = ft_roi.sceneBoundingRect()
        self.x1, self.y1, self.x2, self.y2 = bounds.x(), bounds.y(), bounds.x() + bounds.width(), bounds.y() + bounds.height()
        