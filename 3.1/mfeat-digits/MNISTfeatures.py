import glob
import csv
import scipy.signal

"""
COMP422 Project 1 Task 3.1: Object Recognition: Classification of Hand-Written Digits
William Wallace 
20/08/2020

NOTE: Change the address of the directory address below to a valid directory where you want to save the output CSV file
"""

def main():
    data = tabulate('mfeat-fou', 'mfeat-fac', 'mfeat-kar', 'mfeat-pix', 'mfeat-zer', 'mfeat-mor')
    with open("C:/Users/William/Documents/William'sFolderOfEverything/2020/COMP422/project1-images/project1-images/3.1/numdata.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Opens the extracted feature files and assigns the contents to a corresponding variable
def tabulate(f1, f2, f3, f4, f5, f6):

    list_of_data = []

    data1 = open(f1)
    d1 = data1.readlines()
    data1.close()

    data2 = open(f2)
    d2 = data2.readlines()
    data2.close()

    data3 = open(f3)
    d3 = data3.readlines()
    data3.close()

    data4 = open(f4)
    d4 = data4.readlines()
    data4.close() 

    data5 = open(f5)
    d5 = data5.readlines()
    data5.close() 

    data6 = open(f6)
    d6 = data6.readlines()
    data6.close()    

    # Appends data corresponding to each extracted feature files to one long list.
    
    # Fourier coefficients
    for line in d1[:]:
        obj = line.split()
        attributes = []
        for i in range(76):
            attributes.append(obj[i])
        list_of_data.append(attributes)
    
    # Profile correlations
    n = 0
    for line in d2[:]:
        obj = line.split()
        for i in range(216):
            list_of_data[n].append(obj[i])
        n += 1
    
    # Karhunen-Love coefficient 
    n = 0
    for line in d3[:]:
        obj = line.split()
        for i in range(64):
            list_of_data[n].append(obj[i])
        n += 1

    # Pixel averages in 2x3 windows
    n = 0
    for line in d4[:]:
        obj = line.split()
        for i in range(240):
            list_of_data[n].append(obj[i])
        n += 1

    # Zernike moment
    n = 0
    for line in d5[:]:
        obj = line.split()
        for i in range(47):
            list_of_data[n].append(obj[i])
        n += 1

    # Morphological features
    n = 0
    for line in d6[:]:
        obj = line.split()
        for i in range(6):
            list_of_data[n].append(obj[i])
        n += 1

    # 200 instances per class
    n = 0
    for num in range(10):
        for i in range(200):
            list_of_data[n].append(num)
            n += 1 
    return list_of_data
            
main()