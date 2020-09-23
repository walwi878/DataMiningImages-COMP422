"""
COMP422 Project 1 Task 1.3: Image Enhancement
William Wallace
12/08/2020
"""

import numpy as np
from matplotlib.pyplot import imread
import imageio

def main():
    img = imageio.imread('blurry-moon.tif')
    img = img.astype('uint8')
    final_image = lap_filt1(img)
    #final_image = final_image.astype('uint8')
    imageio.imwrite('first_laplacian_filter.jpg', final_image)

def apply_convolution(image, kernel):
    y, x = image.shape
    x = x-2
    y = y-2
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(image[i:i+3, j:j+3] * kernel)
    return new_image

#Source: https://www.tutorialspoint.com/dip/laplacian_operator.htm
#Source: https://www.olympus-lifescience.com/en/microscope-resource/primer/java/digitalimaging/processing/convolutionkernels/
#Source: https://bohr.wlu.ca/hfan/cp467/12/notes/cp467_12_lecture6_sharpening.pdf 
def lap_filt1(image):
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    
    output = apply_convolution(image, kernel)
    return output

def lap_filt2(image):
    kernel = [[1, -2, 1], [-2, 5, -2], [1, -2, 1]]
    output = apply_convolution(image, kernel)
    return output

#Execute program
main()