import numpy as np

class OutputPortController():
    def __init__(self,output_port):
        self.output_port = output_port

    def change_mixer(self):
        window = self.output_port.main_window.viewports[0].ft_viewer
        if self.output_port.inner_region_mode_radio_button.isChecked():
            mask = np.zeros(np.shape(self.output_port.main_window.viewports[0].image_object.editedimgByte))
            mask[int(window.y1):int(window.y2)+1,int(window.x1):int(window.x2)+1] = 1
        else:    
            mask = np.ones(np.shape(self.output_port.main_window.viewports[0].image_object.editedimgByte))
            mask[int(window.y1):int(window.y2)+1,int(window.x1):int(window.x2)+1] = 0
        if self.output_port.magnitude_and_phase_radio.isChecked():
            magnitudeMix = 0
            phaseMix = 0
            for i in range(4):
                if self.output_port.main_window.viewports[i].image_object.imgPath:
                    if self.output_port.components[i].component_combobox.currentText() == "Magnitude":
                        magnitudeMix += self.output_port.components[i].component_slider.value() / 100 * np.abs(self.output_port.main_window.viewports[i].image_object.fShift)
                    else : 
                        phaseMix += self.output_port.components[i].component_slider.value() / 100 * np.angle(self.output_port.main_window.viewports[i].image_object.fShift)
            output =  np.clip(np.abs(np.fft.ifft2(((magnitudeMix*mask)*np.exp(1j * (phaseMix*mask))))),0,255)  
            self.output_port.output_viwer.setImage(output)
        else :
            realMix = 0
            imaginaryMix = 0
            for i in range(4):
                if self.output_port.main_window.viewports[i].image_object.imgPath:
                    if self.output_port.components[i].component_combobox.currentText() == "Real":
                        realMix += self.output_port.components[i].component_slider.value() / 100 * np.real(self.output_port.main_window.viewports[i].image_object.fShift)
                    else :
                        imaginaryMix += self.output_port.components[i].component_slider.value() / 100 * np.imag(self.output_port.main_window.viewports[i].image_object.fShift)
            output =  np.clip(np.abs(np.fft.ifft2((realMix*mask)+(imaginaryMix*mask)*1j)),0,255)  
            self.output_port.output_viwer.setImage(output)

    def set_to_real_and_Imaginary(self, checked):
        if checked:
            for i in range(4):
                self.output_port.components[i].component_combobox.clear()
                self.output_port.components[i].component_combobox.addItems(["Real","Imaginary"])
                self.output_port.components[i].component_slider.setValue(0)

    def set_to_magnitude_and_phase(self, checked):
        if checked:
            for i in range(4):
                self.output_port.components[i].component_combobox.clear()
                self.output_port.components[i].component_combobox.addItems(["Magnitude","Phase"])
                self.output_port.components[i].component_slider.setValue(0)

    def roi_changed(self):
        self.change_mixer()