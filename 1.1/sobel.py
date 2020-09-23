"""
COMP422 Project 1 Task 1.1: Edge Detection
William Wallace
11/08/2020
"""
# Source: https://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/ 

import numpy as np
import imageio
from matplotlib.pyplot import imread

def main():
    im = imageio.imread('test-pattern.tif')   
    final_image = apply_filter(im)            
    final_image[final_image < 20] = 0             
    final_image[final_image >= 20] = 255
    final_image = final_image.astype('uint8')    
    imageio.imwrite('sobel.jpg', final_image)   #Save the processed image as jpg format
  
def apply_filter(image):
    x_kernel = np.array([[-1,0,1],
                         [-2,0,2],
                         [-1,0,1]])

    y_kernel = np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]])

    row_result = apply_convolution(image, x_kernel)
    col_result = apply_convolution(image, y_kernel)

    filtered = np.sqrt(row_result * row_result + col_result * col_result)

    return filtered

def apply_convolution(image, kernel):
    y, x = image.shape
    y = y - 2
    x = x - 2
    new_img = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_img[i][j] = np.sum(image[i:i+3, j:j+3] *kernel)
    return new_img

# Execute program
main()