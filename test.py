import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import median

TB = imread("Tuberculosis.png")
plt.imshow(TB, cmap = "gray")
plt.show()
