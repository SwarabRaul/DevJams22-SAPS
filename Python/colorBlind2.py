# imports
import numpy as np
import cv2
from colorblind import colorblind
import matplotliwb.pyplot as plt

# load image
img = cv2.imread('./Images/tiger.jpeg')
img = img[..., ::-1]

# simulate protanopia
simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='protanopia')

cv2.imwrite('pro_tiger.jpeg', simulated_img)


# correct using daltonization
daltonized_img = colorblind.daltonize_correct(img, colorblind_type='protanopia')
cv2.imwrite('dal_tiger.jpeg', daltonized_img)

# correct using hsv correction
hsv_img = colorblind.hsv_color_correct(img, colorblind_type='protanopia')
cv2.imwrite('hsv_tiger.jpeg', hsv_img)
