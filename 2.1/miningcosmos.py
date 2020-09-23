import numpy as np
import scipy.signal
from matplotlib.pyplot import imread
import imageio

"""
COMP422 Project 1 Task 2.1: Mining Space Images
William Wallace
20/08/2020

@buglist Note: I received warnings after executing this program because the input image’s
values were of type float64, and imwrite(), convert  elements to uint8 leading to lossy conversion.
  
I attempted to fix this problem using the astype() function but failed to fix it in time before 
submitting the assignment. 
"""


def main():
    image = imageio.imread('hubble.tif')
    image = image.astype('int32')
    
    
    # Smooth with 3*3 mask filter 
    output1 = mean_filt1(image)
    #output1 = mag0.astype('uint8')
    imageio.imwrite('mapf1.jpg', output1)    
    
    # Smooth with 5*5 mask
    output5 = mean_filt2(image)
    #output5 = output5.astype('uint8')
    imageio.imwrite('mapf2.jpg', output5)      
    
    #3x3 mask, 50 threshold 
    output2 = mean_filt1(image)
    map50 = apply_threshold(output2, 50)
    #map50 = map50.astype('uint8')
    imageio.imwrite('map50thresh.jpg', map50)   
    
    #3x3 mask, 100 threshold 
    output3 = mean_filt1(image)
    map100 = apply_threshold(output3, 100)
    #map100 = map100.astype('uint8')
    imageio.imwrite('map100thresh.jpg', map100)    
    
    #3x3 mask, 200 threshold 
    output4 = mean_filt1(image)
    map200 = apply_threshold(output4, 200)
    #map200 = map200.astype('uint8')
    imageio.imwrite('map200thresh.jpg', map200)   
    
    #No mask for smoothing, 200 threshold 
    map200_ws = apply_threshold(image, 200)
    #map200_ws = map200_ws.astype('uint8')
    imageio.imwrite('map200thresh_no_smoothing.jpg', map200_ws)  

def apply_convolution(img, kernel):
    y, x = img.shape
    x = x-2
    y = y-2
    
    output_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            output_image[i][j] = np.sum(img[i:i+3, j:j+3] * kernel)
    return output_image

def mean_filt1(image):
    kernel = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
    output = apply_convolution(image, kernel)
    return output

def mean_filt2(image):
    kernel = [[1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25]]
    output = scipy.signal.convolve2d(image, kernel, mode='same', boundary = 'symm', fillvalue=0)
    return output

def apply_threshold(image, thresh):
    image[image < thresh] = 0
    image[image >= thresh] = 1
    return image

main()