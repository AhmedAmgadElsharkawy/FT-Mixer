import numpy as np
import logging
logger = logging.getLogger(__name__)
from PyQt5.QtCore import QPointF

class OutputPortController():
    def __init__(self,output_port):
        self.output_port = output_port

    def change_mixer(self):
        index = -1
        for i in range(4):
            if self.output_port.main_window.image_obejcts[i].imgPath:
                index = i
        if index == -1:
            return
        original_x1 = self.output_port.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().x()
        original_x2 = self.output_port.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().width() + original_x1
        original_y1 = self.output_port.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().y()
        original_y2 = self.output_port.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().height() + original_y1

        # Map the scene points to the image's local space
        scene_point = QPointF(original_x1, original_y1)
        image_point = self.output_port.main_window.viewports[index].ft_viewer.imageItem.mapFromScene(scene_point)

        scene_point2 = QPointF(original_x2, original_y2)
        image_point2 = self.output_port.main_window.viewports[index].ft_viewer.imageItem.mapFromScene(scene_point2)

        mask_shape = np.shape(self.output_port.main_window.viewports[index].image_object.editedimgByte)
        mask_width,mask_height = mask_shape

        clamped_x1 = min(max(int(image_point.x()), 0), mask_width - 1)
        clamped_y1 = min(max(int(image_point.y()), 0), mask_height - 1)

        clamped_x2 = min(max(int(image_point2.x()), 0), mask_width - 1)
        clamped_y2 = min(max(int(image_point2.y()), 0), mask_height - 1)
        
        # window = self.output_port.main_window.viewports[index].ft_viewer
        if self.output_port.inner_region_mode_radio_button.isChecked():
            mask = np.zeros(np.shape(self.output_port.main_window.viewports[index].image_object.editedimgByte))
            mask[ clamped_x1:clamped_x2 + 1,clamped_y1:clamped_y2 + 1] = 1
        else:    
            mask = np.ones(np.shape(self.output_port.main_window.viewports[index].image_object.editedimgByte))
            mask[ clamped_x1:clamped_x2 + 1,clamped_y1:clamped_y2 + 1] = 0
        if self.output_port.magnitude_and_phase_radio.isChecked():
            magChanged, phases_counter, magnitudeMix, phaseMix = self.magnitude_and_phase_initializations()
            for i in range(4):
                if self.output_port.main_window.viewports[i].image_object.imgPath:
                    if self.output_port.components[i].component_combobox.currentText() == "Magnitude":
                        mag = self.output_port.components[i].component_slider.value()
                        if mag != 0:
                            magChanged = True
                        magnitudeMix += mag / 100 * self.output_port.main_window.viewports[i].image_object.get_magnitude()
                    else :
                        if self.output_port.components[i].component_slider.value() > 0:
                            phases_counter += 1
                        phaseMix += self.output_port.components[i].component_slider.value() / 100 * self.output_port.main_window.viewports[i].image_object.get_phase()
            if not magChanged:
                magnitudeMix = mask
            if phases_counter != 0:
                phaseMix /= phases_counter
            result = (magnitudeMix*mask)*np.exp(1j * (phaseMix*mask))
        else :
            realMix = 0
            imaginaryMix = 0
            for i in range(4):
                if self.output_port.main_window.viewports[i].image_object.imgPath:
                    if self.output_port.components[i].component_combobox.currentText() == "Real":
                        realMix += self.output_port.components[i].component_slider.value() / 100 * self.output_port.main_window.viewports[i].image_object.get_real()
                    else :
                        imaginaryMix += self.output_port.components[i].component_slider.value() / 100 * self.output_port.main_window.viewports[i].image_object.get_imaginary()
            result =  (realMix*mask)+(imaginaryMix*mask)*1j
        
        output = self.output_port.main_window.viewports[i].image_object.calculateIFFT(result) 
        self.output_port.output_viwer.setImage(output)

    def set_to_real_and_Imaginary(self, checked):
        if checked:
            for i in range(4):
                self.output_port.components[i].component_combobox.clear()
                self.output_port.components[i].component_combobox.addItems(["Real","Imaginary"])
                self.output_port.components[i].component_slider.setValue(0)
            logger.info("Output mode has been changed to real_&_imaginary mode")

    def set_to_magnitude_and_phase(self, checked):
        if checked:
            for i in range(4):
                self.output_port.components[i].component_combobox.clear()
                self.output_port.components[i].component_combobox.addItems(["Magnitude","Phase"])
                self.output_port.components[i].component_slider.setValue(0)
            logger.info("Output mode has been changed to magnitude_&_phase mode")

    def roi_changed(self):
        self.change_mixer()

    def magnitude_and_phase_initializations(self):
        magChanged = False
        phases_counter = 0
        magnitudeMix = 0
        phaseMix = 0

        return magChanged, phases_counter, magnitudeMix, phaseMix