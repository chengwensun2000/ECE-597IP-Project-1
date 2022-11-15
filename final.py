import numpy as np
import cv2 as cv
from sklearn.cluster import MeanShift, estimate_bandwidth
from ds import decorrstretch
from meanshiftmain import meanshift


def ImageProcessing(path,image,number):
    img = cv.imread(image)
    img2 = img
    imgHSV =cv.cvtColor(img, cv.COLOR_RGB2HSV)
    imgLUV =cv.cvtColor(img2, cv.COLOR_RGB2LUV)
    cv.imwrite(path+"HSV"+number+".jpeg",imgHSV)
    cv.imwrite(path+"LUV"+number+".jpeg",imgLUV)
    imgdecorr = decorrstretch(imgHSV)
    img2decorr = decorrstretch(imgLUV)
    cv.imwrite(path + "HSVdecorr" + number +".jpeg", imgdecorr)
    cv.imwrite(path + "LUVdecorr" + number + ".jpeg", img2decorr)
    imglin = cv.convertScaleAbs(img,alpha = 2,beta = 0)
    img2lin = cv.convertScaleAbs(img2,alpha = 2,beta = 0)
    cv.imwrite(path + "HSVlin" + number + ".jpeg",imglin)
    cv.imwrite(path + "LUVlin" + number + ".jpeg",img2lin)


if __name__ == "__main__":
    path = "/Users/chengwensun/Library/CloudStorage/GoogleDrive-nikki1231121@gmail.com/Other computers/My Computer/Umass/FALL 2022/ECE 597IP/Another attempt/"
    ImageProcessing(path,'4.tif','4')


