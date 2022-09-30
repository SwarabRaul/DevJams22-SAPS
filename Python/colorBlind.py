import cv2

image=cv2.imread('tiger.jpeg')
image1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_tiger.jpeg', image1)
