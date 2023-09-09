import cv2

img_file = "imgs/car1.jpg"

#pretrain car detector file
classifier_file = 'detectors/cars.xml'

img = cv2.imread(img_file)
cv2.imshow('chucha', img)

print("Code Complete")