"""
COMP422 Project 1 Task 1.2: Noise Cancellation
William Wallace
15/08/2020
"""

import numpy as np
from matplotlib.pyplot import imread
import imageio

def main():
    """ Gets the job done """
    im = imageio.imread('ckt-board-saltpep.tif')
    final_image = apply_mean_filt(im)
    final_image = final_image.astype('uint8')
    imageio.imwrite('meanfiltered.jpg', final_image)
    final_image = apply_med_filt(im)
    final_image = final_image.astype('uint8')
    imageio.imwrite('medianfiltered.jpg', final_image)

#Source: https://www.researchgate.net/figure/Median-Filter-implementation-using-Python_fig9_332574579 
def apply_med_filt(image):
    y, x = image.shape
    y = y-2
    x = x-2
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.median(image[i:i+3, j:j+3])
    return new_image

def apply_mean_filt(image):
    mask = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
    output = apply_convolution(image, mask)
    return output

def apply_convolution(image, kernel):
    y, x = image.shape
    x = x-2
    y = y-2
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(image[i:i+3, j:j+3] * kernel)
    return new_image

main()