import cv2 as cv2
video = cv2.VideoCapture(0)
subtractor=cv2.createBackgroundSubtractorMOG2(20,50)#MOG: Mixture of Gaussains

while True:
    ret,frame= video.read()
    if ret:
        mask=subtractor.apply(frame)
        cv2.imshow('mask',mask)
        if cv2.waitKey(5)==ord('x'):
            break

cv2.destroyAllWindows()
video.release()