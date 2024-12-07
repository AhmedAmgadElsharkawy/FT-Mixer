

class ImageViewerController():
    def __init__(self,image_viewer):
        self.image_viewer = image_viewer

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
        pass

    def show_phase_components(self):
        pass

    def show_imaginary_components(self):
        pass

    def show_real_components(self):
        pass

    