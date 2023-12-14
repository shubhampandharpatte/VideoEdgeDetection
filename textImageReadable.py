import cv2 as cv
image = cv.imread('Alice in Wonderland Book Pages -.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# thresh is all above it are white and below are black
# thresh_binary is method for two values
_, result = cv.threshold(image, 35, 255, cv.THRESH_BINARY)

# ADAPTIVE THRESHOLDING METHOD
adaptive = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4)

cv.imshow('My Image', image)
cv.imshow('My result', result)
cv.imshow('My Adaptive', adaptive)

cv.waitKey(0)
cv.destroyAllWindows()
