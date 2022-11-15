import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import figure

def plot(firstImage,secondImage,thirdImage,fourthImage,color,stretch,number):
    if stretch == '':
        stretch = "no stretch"
    if stretch == "lin":
        stretch = "linear"
    firstImage = mpimg.imread(firstImage)
    sencondImage = mpimg.imread(secondImage)
    thirdImage = mpimg.imread(thirdImage)
    fourthImage = mpimg.imread(fourthImage)
    plt.figure(figsize=(13,8))
    fig = plt.gcf()
    fig.suptitle("Original ->" + color + "-> " + stretch + " -> Segmented using meanshift", fontsize=14)
    plt.subplot(241), plt.imshow(firstImage),plt.xlabel("original"),plt.xticks([]),plt.yticks([])
    plt.subplot(242), plt.imshow(sencondImage),plt.xlabel(color),plt.xticks([]),plt.yticks([])
    plt.subplot(243), plt.imshow(thirdImage),plt.xlabel(stretch),plt.xticks([]),plt.yticks([])
    plt.subplot(244), plt.imshow(fourthImage),plt.xlabel('mean shift'),plt.xticks([]),plt.yticks([])
    plt.subplot(245), plt.hist(firstImage.ravel(),256,[0,256])
    plt.subplot(246), plt.hist(sencondImage.ravel(), 256, [0, 256])
    plt.subplot(247), plt.hist(thirdImage.ravel(), 256, [0, 256])
    plt.subplot(248), plt.hist(fourthImage.ravel(), 256, [0, 256])
    plt.savefig("Original -> "+ color + " -> " + stretch+" -> Segmented using meanshift"+number)
    plt.show()


if __name__ == "__main__":
    color = "LUV"
    stretch = 'decorr'
    number = '2'
    suffix = '.jpeg'

    plot("2.tif",color + number + suffix,color + stretch + number + suffix,"Segmented"+color+stretch+number+suffix,color,stretch,number)





