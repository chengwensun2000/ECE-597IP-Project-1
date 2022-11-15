import cv2
from ds import decorrstretch
# path
image = "LUVfourthimage.tif"
path = r'/Users/chengwensun/Library/CloudStorage/GoogleDrive-nikki1231121@gmail.com/Other computers/My Computer/Umass/FALL 2022/ECE 597IP/Another attempt/'+image


image = cv2.imread(path)
decorrimage = decorrstretch(image)


cv2.imwrite('/Users/chengwensun/Library/CloudStorage/GoogleDrive-nikki1231121@gmail.com/Other computers/My Computer/Umass/FALL 2022/ECE 597IP/Another attempt/LUVfourthimagede4.tif',decorrimage)
cv2.imshow('Original image',decorrimage)
cv2.waitKey(0)
