"""
COMP422 Project 1 Task 2.2: Face Detection
William Wallace
25/08/2020
"""

import scipy.signal
import imageio
import csv
import glob

def main():
    train_example = []
    for filen in glob.glob('*.pgm'):
        img = imageio.imread(filen)
        img = img.astype('int32')
        train_example.append((extricate(img) + [1])) 
    with open("C:/Users/William/Documents/William'sFolderOfEverything/2020/COMP422/project1-images/project1-images/2.2/testing_face.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(train_example)    
    

# Gets the max value and location of pixels in the middle area and assumes them to be nose features.
def nose(img):   
    section = []
    for row in img[7:12]:
        for col in row[7:12]:
            section.append(col)
    return (max(section), section.index(max(section)) % 5)

# Gets the data from the top left of the image
def bot_left(img):
    section = []
    for row in img[10:]:
        for col in row[:9]:
            section.append(col)
    return section    

# Gets the values of left pupil brightness as a minimum value, left eyewhite brightness as the maximum value,
# and the total value - all from the top right subimage
def top_left(img):
    section = []
    for row in img[:9]:
        for col in row[:9]:
            section.append(col)
    return (min(section), max(section), sum(section))

# Gets the values of right pupil brightness as a minimum value, right eyewhite brightness as the maximum value,
# and the total value - all from the top right subimage
def top_right(img):
    section = []
    for row in img[:9]:
        for col in row[10:]:
            section.append(col)
    return (min(section), max(section), sum(section))

# Gets data from the bottom right area of the image 
def bot_right(img):
    section = []
    for row in img[10:]:
        for col in row[10:]:
            section.append(col)
    return section

# Gets the four statistic features of lower left area and lower right area
def comparison(section):
    c = section[40]
    x = section[4] + section[13] + section[22] + section[31] + section[49] + section[58] + section[67] + section[76]
    + section[36] + section[37] + section[38] + section[39] + section[41] + section[42] + section[43] + section[44]
    y = section[0] + section[10] + section[20] + section[30] + section[50] + section[60] + section[70] + section[80]
    + section[8] + section[16] + section[24] + section[32] + section[48] + section[56] + section[64] + section[72]
    z = sum(section) - c - x - y           
    return (c, x / 16, y / 16, z / 48)


# Takes the features of interest out of the input image
def extricate(image_data):
    l_pupil, l_eyewhite, topleft = top_left(image_data)
    r_pupil, r_eyewhite, topright = top_right(image_data)
    (lc, lx, ly, lz) = comparison(bot_left(image_data))
    (rc, rx, ry, rz) = comparison(bot_right(image_data))
    
    pupil_dif = abs(l_pupil - r_pupil)               #Difference of pupil values
    eyewhite_dif = abs(l_eyewhite - r_eyewhite)      #Difference of eyewhite values
    upper_dif = abs(topleft - topright)              #Difference of top-left (eye) subsection and top-right (eye) subsection
    (nosetip_brightness, nosetip_loc) = nose(image_data) #Brightness value (out of 255) and location of nose tip within image
    bc_dif = abs(lc - rc)                            #Differences between features of the bottom left and right areas
    bx_dif = abs(lx - rx)
    by_dif = abs(ly - ry)
    bz_dif = abs(lz - rz)
    return [pupil_dif, eyewhite_dif, upper_dif, nosetip_brightness, nosetip_loc,
            bc_dif, bx_dif, by_dif, bz_dif]
    
main()