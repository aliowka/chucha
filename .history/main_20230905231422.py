import cv2

img_file = "imgs/car1.jpg"

#pretrain car detector file
classifier_file = 'detectors/haar.xml'

img = cv2.imread(img_file)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = car_tracker.detectMultiScale(black_n_white)

for x,y,w,h in cars:
    print("car was detected")
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        
cv2.imshow('chucha', img)
cv2.waitKey()



print("Code Complete")