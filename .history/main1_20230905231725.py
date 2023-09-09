from easyocr import Reader
import cv2

# load the image and resize it
image = cv2.imread('image1.jpg')
image = cv2.resize(image, (800, 600))

