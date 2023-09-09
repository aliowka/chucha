import cv2

img_file = "imgs/car2.jpg"

#pretrain car detector file
classifier_file = 'detectors/cars.xml'

img = cv2.imread(img_file)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = car_tracker.detectMultiScale(black_n_white)

for x,y,w,h in cars:
    cv2.rectangle(img, )
        
cv2.imshow('chucha', car)
cv2.waitKey()



print("Code Complete")