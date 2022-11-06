import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

TB = imread("Tuberculosis.png")
plt.imshow(TB, cmap = "gray")
plt.show()
git config --global user.email "3190103326@zju.edu.cn"
git config --global user.name "Wenjing Yang"