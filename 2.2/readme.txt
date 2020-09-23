README FOR FACEDETECTOR.PY 

To run facedetector.py, put the program in each directory that contains the PGM files for face detection. 

Ensure that the location of the output file is logically named and in a valid directory on your computer.

For face data, ensure that 1 is added as the final element of the train_example list on line 17. 
For non-face data, ensure this value is 0.

For example, if you have individual directories for training data, testing data, face data and non-face data 
then put the program in each of these directories and run the program four times, each from their own 
directory (specified by the coding environment).

Finally, convert the outputted CSV files into ARTT format using WEKA's ARTTViewer tool for further analysis of the data. 