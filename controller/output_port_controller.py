import numpy as np
import logging
logger = logging.getLogger(__name__)
from PyQt5.QtCore import QPointF

class OutputPortController():
    def __init__(self,output_port):
        self.output_port = output_port

    def change_mixer(self):
        root = self.output_port
        index = -1
        for i in range(4):
            if root.main_window.image_obejcts[i].imgPath:
                index = i
        if index == -1:
            return
        original_x1 = root.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().x()
        original_x2 = root.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().width() + original_x1
        original_y1 = root.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().y()
        original_y2 = root.main_window.viewports[index].ft_viewer.ft_roi.sceneBoundingRect().height() + original_y1

        # Map the scene points to the image's local space
        scene_point = QPointF(original_x1, original_y1)
        image_point = root.main_window.viewports[index].ft_viewer.imageItem.mapFromScene(scene_point)

        scene_point2 = QPointF(original_x2, original_y2)
        image_point2 = root.main_window.viewports[index].ft_viewer.imageItem.mapFromScene(scene_point2)

        mask_shape = np.shape(root.main_window.viewports[index].image_object.editedimgByte)
        mask_width,mask_height = mask_shape

        clamped_x1 = min(max(int(image_point.x()), 0), mask_width - 1)
        clamped_y1 = min(max(int(image_point.y()), 0), mask_height - 1)

        clamped_x2 = min(max(int(image_point2.x()), 0), mask_width - 1)
        clamped_y2 = min(max(int(image_point2.y()), 0), mask_height - 1)
        
        mask = self.creating_mask(root, index, clamped_x1, clamped_y1, clamped_x2, clamped_y2)
        if root.magnitude_and_phase_radio.isChecked():
            magChanged, phases_counter, magnitudeMix, phaseMix = self.magnitude_and_phase_initializations()
            for i in range(4):
                if root.main_window.viewports[i].image_object.imgPath:
                    if root.components[i].component_combobox.currentText() == "Magnitude":
                        mag = root.components[i].component_slider.value()
                        if mag != 0:
                            magChanged = True
                        magnitudeMix += mag / 100 * root.main_window.viewports[i].image_object.get_magnitude()
                    else :
                        if root.components[i].component_slider.value() > 0:
                            phases_counter += 1
                        phaseMix += root.components[i].component_slider.value() / 100 * root.main_window.viewports[i].image_object.get_phase()
            if not magChanged:
                magnitudeMix = mask
            if phases_counter != 0:
                phaseMix /= phases_counter
            result = (magnitudeMix*mask)*np.exp(1j * (phaseMix*mask))
        else :
            realMix = 0
            imaginaryMix = 0
            for i in range(4):
                if root.main_window.viewports[i].image_object.imgPath:
                    if root.components[i].component_combobox.currentText() == "Real":
                        realMix += root.components[i].component_slider.value() / 100 * root.main_window.viewports[i].image_object.get_real()
                    else :
                        imaginaryMix += root.components[i].component_slider.value() / 100 * root.main_window.viewports[i].image_object.get_imaginary()
            result =  (realMix*mask)+(imaginaryMix*mask)*1j
        
        output = root.main_window.viewports[i].image_object.calculateIFFT(result) 
        root.output_viwer.setImage(output)

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

    def creating_mask(self, root, index, x1, y1, x2, y2):
        if root.inner_region_mode_radio_button.isChecked():
            mask = np.zeros(np.shape(root.main_window.viewports[index].image_object.editedimgByte))
            mask[ x1: x2 + 1, y1: y2 + 1] = 1
        else:    
            mask = np.ones(np.shape(root.main_window.viewports[index].image_object.editedimgByte))
            mask[ x1: x2 + 1, y1: y2 + 1] = 0

        return mask

    def magnitude_and_phase_initializations(self):
        magChanged = False
        phases_counter = 0
        magnitudeMix = 0
        phaseMix = 0

        return magChanged, phases_counter, magnitudeMix, phaseMix