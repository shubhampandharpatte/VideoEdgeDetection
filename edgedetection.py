import cv2 as cv2
video = cv2.VideoCapture(0)

while True:
    ret,frame= video.read()
    if ret:
        canny=cv2.Canny(frame,20,150)
        cv2.imshow('my canny sketch',canny)
        if cv2.waitKey(5)==ord('x'):
            break

cv2.destroyAllWindows()
video.release()