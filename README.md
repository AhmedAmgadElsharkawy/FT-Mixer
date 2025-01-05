# FT-Mixer
Desktop app that demonstrates the importance of magnitude and phase components in 2D signals, specifically grayscale images. It allows users to view and manipulate the Fourier transform components (magnitude, phase, real, imaginary) of multiple images, customize the weights for mixing, select regions for each component, and visualize the real-time effects with adjustable brightness, contrast, and output port options.

## Table of Contents
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Contributors](#contributors)

## Demo
https://github.com/user-attachments/assets/d764fce9-4759-4a93-8a3f-32a21140cca3

## Prerequisites

- Python 3.6 or higher

## Installation

1. **Clone the repository:**

   ``````
   git clone https://github.com/AhmedAmgadElsharkawy/FT-Mixer.git
   ``````

2. **Install The Dependincies:**
    ``````
    pip install -r requirements.txt
    ``````

3. **Run The App:**

    ``````
    python main.py
    ``````

## Features
- **Multiple image viewing**: As the user can add up to 4 images at once, and view their (magnitude, phase, real, and imaginary plots).

- **Contrast & Brightness control**: The user can control the contrast & brightness of each image, and see the effect immediately.

- **Two major modes of mixing**: The user can mix images using two modes (magnitude & phase mode, and real & imaginary mode).

- **Percentage mixing**: The user can mix the images' parts he got from FT to get a new images, he can control percentage of each participating part with sliders.

- **Two major modes of region mixing**: User can select the region he wants to cut, he can also use the (Inner mode) for mixing only the area surrounded by the recatangle, or (Outer mode) for mixing the surroundings and ignoring the inner data.




## Contributors
- **AhmedAmgadElsharkawy**: [GitHub Profile](https://github.com/AhmedAmgadElsharkawy)
- **AbdullahMahmoudHanafy**: [GitHub Profile](https://github.com/AbdullahMahmoudHanafy)
- **Mohamed-185**: [GitHub Profile](https://github.com/Mohamed-185)
- **RawanAhmed444**: [GitHub Profile](https://github.com/RawanAhmed444)

