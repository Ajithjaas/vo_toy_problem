import cv2
import numpy as np
import glob
 
img_array = []
size = (0,0)
for filename in glob.glob("/home/ajith/Documents/openCV/data/*.jpg"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()