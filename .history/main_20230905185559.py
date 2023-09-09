import cv2

img_file = "imgs/car1.jpg"

#pretrain car detector file
classifier_file = 'detectors/cars.xml'





img = cv2.imread(img_file)
black_n_white = cv2.cvtColor


car_tracker = cv2.CascadeClassifier(classifier_file)


cv2.imshow('chucha', img)
cv2.waitKey()



print("Code Complete")