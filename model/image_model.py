import numpy as np
import cv2
from PyQt5.QtWidgets import QFileDialog
import logging
logger = logging.getLogger(__name__)

class ImageModel():
    def __init__(self):
        self.imgPath =None
        self.imgByte =None
        self.imgShape =None
        self.sizedimgByte =None
        self.editedimgByte =None
        self.contrastedimgByte =None
        self.brightenedimgByte =None
        self.dft =None
        self.real =None
        self.imaginary =None
        self.magnitude =None
        self.phase =None
        self.fShift =None
        self.magnitudePlot =None
        self.phasePlot =None
        self.realPlot=None
        self.imaginaryPlot =None

    def image_process(self,imgPath: str):
        logger.info("Starting the initial image processing")
        self.imgPath = imgPath
        self.imgByte = cv2.imread(self.imgPath, flags=cv2.IMREAD_GRAYSCALE).T
        self.imgShape = self.imgByte.shape
        self.editedimgByte = self.imgByte.copy()
        self.contrastedimgByte = self.imgByte
        self.brightenedimgByte = self.imgByte
        self.sizedimgByte = self.imgByte
        self.calculateFFT(self.imgByte)

    def calculateFFT(self, img):
        logger.info("Calculating the FFT for this image")
        self.editedimgByte = img
        self.dft = np.fft.fft2(img)
        self.real = np.real(self.dft)
        self.imaginary = np.imag(self.dft)
        self.magnitude = np.abs(self.dft)
        self.phase = np.angle(self.dft)
        self.fShift = np.fft.fftshift(self.dft)
        self.magnitudePlot = 20 * np.log(np.abs(self.fShift))
        self.phasePlot = np.angle(self.fShift)
        self.realPlot = 20 * np.log(abs(np.real(self.fShift))+(1e-9))
        self.imaginaryPlot = np.imag(self.fShift)

    def load_image(self):
            filename, format = QFileDialog.getOpenFileName(None, "Load Image","*.jpg;;" "*.jpeg;;" "*.png;;")
            if filename:
                self.image_process(filename)
                