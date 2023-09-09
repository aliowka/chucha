from easyocr import Reader
import cv2

# load the image and resize it
image = cv2.imread('image1.jpg')
image = cv2.resize(image, (800, 600))

# convert the input image to grayscale,
# blur it, and detect the edges 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray, (5,5), 0) 
edged = cv2.Canny(blur, 10, 200) 
cv2.imshow('Canny', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find the contours, sort them, and keep only the 5 largest ones
contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]

# loop over the contours
for c in contours:
    # approximate each contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    # if the contour has 4 points, we can say
    # that we have found our license plate
    if len(approx) == 4:
        n_plate_cnt = approx
        break        

# get the bounding box of the contour and 
# extract the license plate from the image
(x, y, w, h) = cv2.boundingRect(n_plate_cnt)
license_plate = gray[y:y + h, x:x + w]


