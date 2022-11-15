from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse

imagename = "HSVfourthimage.tif"
abspath = r'/Users/chengwensun/Library/CloudStorage/GoogleDrive-nikki1231121@gmail.com/Other computers/My Computer/Umass/FALL 2022/ECE 597IP/Another attempt/'
path = abspath+imagename



image = cv.imread(path)

new_image = np.zeros(image.shape, image.dtype)
alpha = 2 # Simple contrast control
beta = 0   # Simple brightness control
# Initialize values
print(' Basic Linear Transforms ')
print('-------------------------')
# try:
#     alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
#     beta = int(input('* Enter the beta value [0-100]: '))
# except ValueError:
#     print('Error, not a number')
# Do the operation new_image(i,j) = alpha*image(i,j) + beta
# Instead of these 'for' loops we could have used simply:
new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
# but we wanted to show you how to access the pixels :)
# for y in range(image.shape[0]):
#     for x in range(image.shape[1]):
#         for c in range(image.shape[2]):
#             new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)



cv.imwrite(abspath+'HSVlinfourthimage.tif',new_image)
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
# Wait until user press some key
cv.waitKey()
