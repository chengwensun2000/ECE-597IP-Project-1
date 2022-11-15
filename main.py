import numpy as np
import cv2 as cv
from sklearn.cluster import MeanShift, estimate_bandwidth

image = 'LUVdecorr4.jpeg'

path = r'/Users/chengwensun/Library/CloudStorage/GoogleDrive-nikki1231121@gmail.com/Other computers/My Computer/Umass/FALL 2022/ECE 597IP/Another attempt/'

path2 = path + image
path3 = path + "Segmented" + image
img = cv.imread(path2)

# filter to reduce noise
img = cv.medianBlur(img, 3)

# flatten the image
flat_image = img.reshape((-1,3))
flat_image = np.float32(flat_image)

# meanshift

print('here1')
bandwidth = estimate_bandwidth(flat_image, quantile=.06, n_samples=3000)
print("here2")
ms = MeanShift(bandwidth=bandwidth, max_iter=800, bin_seeding=True)
print("here3")
ms.fit(flat_image)
print("here4")
labeled=ms.labels_
print('here')

# get number of segments
segments = np.unique(labeled)
print('Number of segments: ', segments.shape[0])

# get the average color of each segment
total = np.zeros((segments.shape[0], 3), dtype=float)
count = np.zeros(total.shape, dtype=float)
for i, label in enumerate(labeled):
    total[label] = total[label] + flat_image[i]
    count[label] += 1
avg = total/count
avg = np.uint8(avg)

# cast the labeled image into the corresponding average color
res = avg[labeled]
result = res.reshape((img.shape))

# show the result

cv.imwrite(path3,result)
cv.imshow('result',result)
cv.waitKey(0)
