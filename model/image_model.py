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
        self.dft =None
        self.real =None
        self.imaginary =None
        self.magnitude =None
        self.phase =None
        self.fShift =None
        self.magnitudePlot =None
        self.phasePlot =None
        self.realPlot =None
        self.imaginaryPlot =None

    def image_process(self,imgPath: str):
        logger.info("Starting the initial image processing")
        self.imgPath = imgPath
        self.imgByte = cv2.imread(self.imgPath, flags=cv2.IMREAD_GRAYSCALE).T
        self.imgShape = self.imgByte.shape
        self.editedimgByte = self.imgByte.copy()
        self.sizedimgByte = self.imgByte.copy()
        self.calculateFFT(self.imgByte)

    def calculateFFT(self, img):
        logger.info("Calculating the FFT for this image")
        self.editedimgByte = img
        self.dft = np.fft.fft2(img)
        self.fShift = np.fft.fftshift(self.dft)
        self.real = np.real(self.fShift)
        self.imaginary = np.imag(self.fShift)
        self.magnitude = np.abs(self.fShift)
        self.phase = np.angle(self.fShift)
        self.magnitudePlot = 20 * np.log(self.magnitude)
        self.phasePlot = self.phase
        self.realPlot = 20 * np.log(abs(self.real)+(1e-9))
        self.imaginaryPlot = self.imaginary

    def calculateIFFT(self, data):
         return np.clip(np.abs(np.fft.ifft2(data)),0,255)

    def load_image(self):
        filename, format = QFileDialog.getOpenFileName(None, "Load Image","*.jpg;;" "*.jpeg;;" "*.png;;")
        if filename:
            self.image_process(filename)

    def get_fshift(self):
         return self.fShift
    
    def get_real(self):
         return self.real
    
    def get_imaginary(self):
         return self.imaginary
    
    def get_magnitude(self):
         return self.magnitude
    
    def get_phase(self):
         return self.phase
                