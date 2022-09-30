import cv2
from daltonize import daltonize
import numpy as ny

fig = 'Images\App1.png'

sim_fig = daltonize.simulate_mpl(fig, copy=True)
daltonized_fig = daltonize.daltonize_mpl(fig, copy=True)