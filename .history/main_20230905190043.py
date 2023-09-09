import cv2

img_file = "imgs/car1.jpg"

#pretrain car detector file
classifier_file = 'detectors/cars.xml'





img = cv2.imread(img_file)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = cv2.

cv2.imshow('chucha', black_n_white)
cv2.waitKey()



print("Code Complete")