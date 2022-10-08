import cv2

img = cv2.imread('D:/DataScience/OpenCV Sketch/Test_Image.JPG')

cv2.imshow('',img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('',img_gray)

img_invert = cv2.bitwise_not(img_gray)

cv2.imshow('',img_invert)

img_smoothing = cv2.GaussianBlur(img_invert, (21,21), sigmaX=0, sigmaY=0)

cv2.imshow('',img_smoothing)

def dodgeV2(x,y):
    return cv2.divide(x,255-y, scale =256)

final_img = dodgeV2(img_gray, img_smoothing)

cv2.imshow('',final_img)

img_new = cv2.imwrite('D:/DataScience/OpenCV Sketch/Test_Image_Sketch.JPG',final_img)

print('Done')
