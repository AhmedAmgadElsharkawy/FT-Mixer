import cv2
import numpy as np
class ImageViewerController():
    def __init__(self,image_viewer):
        self.image_viewer = image_viewer
        self.image_viewer.ft_components_combobox.currentIndexChanged.connect(self.select_ft_component)


    def plot_image(self):
        # height, width = self.imgByte.shape
        # image_view_widget.getView().setLimits(xMin=0, xMax=width, yMin=0, yMax=height)
        self.image_viewer.image_view_widget.setImage(self.image_viewer.image_object.editedimgByte)
        self.image_viewer.enable_controls()
        self.image_viewer.main_window.enable_component_outports_sliders_by_index(self.image_viewer.image_viewer_index)
        self.select_ft_component()

    def select_ft_component(self):
        selected_text = self.image_viewer.ft_components_combobox.currentText()
        match selected_text:
            case "FT Magnitude":
                self.show_magnitude_components()

            case "FT Phase":
                self.show_phase_components()

            case "FT Imaginary":
                self.show_imaginary_components()

            case "FT Real":
                self.show_real_components()
            case _:
                return
    
    def show_magnitude_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.magnitudePlot)

    def show_phase_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.phasePlot)


    def show_imaginary_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.imaginaryPlot)


    def show_real_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.realPlot)

    def change_contrast_and_brightness(self):
        if self.image_viewer.image_object.imgPath is not None:
            alpha = self.image_viewer.contrast_slider.value() / 100
            beta = self.image_viewer.brightness_slider.value()

            contrasted_image = cv2.convertScaleAbs(self.image_viewer.image_object.sizedimgByte, alpha=alpha, beta=beta)
            self.image_viewer.image_object.calculateFFT(contrasted_image)
            self.image_viewer.image_view_widget.setImage(contrasted_image)
            self.select_ft_component()
            self.image_viewer.main_window.left_output_port.output_controller.change_mixer()
            self.image_viewer.main_window.right_output_port.output_controller.change_mixer()

    def get_minimum_dimension(self, viewports):
        minWidth = 10000
        minHeight = 10000
        for i in range(len(viewports)):
            if viewports[i].image_object.imgPath:
                minWidth = min(minWidth, viewports[i].image_object.imgShape[0])
                minHeight = min(minHeight, viewports[i].image_object.imgShape[1])
        
        return minWidth, minHeight
                

    def unify_images_size(self, viewports):
        minWidth, minHeight = self.get_minimum_dimension(viewports)
        resized_images = [... ,... ,..., ... ]

        for i in range(len(viewports)):
            if viewports[i].image_object.imgPath and np.shape(viewports[i].image_object.imgByte) != (minWidth, minHeight):
                resized_images[i] = cv2.resize(viewports[i].image_object.imgByte, (minWidth, minHeight))
        
        for i in range(len(resized_images)):
            if viewports[i].image_object.imgPath and np.shape(viewports[i].image_object.imgByte) != (minWidth, minHeight):
                viewports[i].image_view_widget.setImage(resized_images[i])
                viewports[i].image_object.sizedimgByte = resized_images[i]
                viewports[i].image_object.calculateFFT(resized_images[i])

    