from PyQt5.QtCore import QObject, pyqtSignal
import pyqtgraph as pg
import numpy as np
from view.custom_view import CustomView


class SignalEmitter(QObject):
    sig_ROI_changed = pyqtSignal()

class CustomFTView(CustomView):
    def __init__(self):
        super().__init__()
        self.sig_emitter = SignalEmitter()
        self.ft_roi = pg.ROI(pos = self.getView().viewRect().center(), size = (300, 300), hoverPen='r', resizable= True, invertible= True, rotatable= False)
        self.addItem(self.ft_roi)
        self.add_scale_handles_ROI(self.ft_roi)
        self.ft_roi.sigRegionChangeFinished.connect(lambda: self.region_update(self.ft_roi,finish = True))

    def getRoi(self):
        return self.ft_roi

    def add_scale_handles_ROI(self, roi : pg.ROI):
        positions = np.array([[0,0], [1,0], [1,1], [0,1]])
        for pos in positions:        
            self.ft_roi.addScaleHandle(pos = pos, center = 1 - pos)

    def region_update(self,ft_roi , finish = False):
        if finish:
            self.sig_emitter.sig_ROI_changed.emit()
