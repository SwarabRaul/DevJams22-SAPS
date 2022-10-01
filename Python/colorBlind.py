import numpy as np
import cv2
from colorblind import colorblind
import matplotlib.pyplot as plt

# load image
img = cv2.imread('Images/Test/WebApp/WebApp 7.png')
img = img[..., ::-1]

# simulate protanopia
simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='protanopia')
cv2.imwrite('Images/Conv/protanopia.png', simulated_img)


# correct using daltonization
daltonized_img = colorblind.daltonize_correct(img, colorblind_type='protanopia')
cv2.imwrite('Images/Conv/daltonization.png', daltonized_img)

# correct using hsv correction
hsv_img = colorblind.hsv_color_correct(img, colorblind_type='protanopia')
cv2.imwrite('Images/Conv/hsv.png', hsv_img)
