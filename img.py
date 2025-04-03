import cv2
import numpy

array = cv2.imread('image.png')
def img_write(array):
    array_im = numpy.array(array)
    cv2.imwrite('image5.png', array_im)


if __name__ == "__main":
    print(array)
    print(array.shape)