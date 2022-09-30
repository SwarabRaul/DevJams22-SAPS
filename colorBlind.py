import cv2

image=cv2.imread("//Users//pritika//Documents//VIT//Projects//GitHub//DevJams22-SAPS//tiger.jpeg")
image1=cv2.cvtColor(image, cV2.COLOR_BGR2GRAY)
cv2.imwrite("//Users//pritika//Documents//VIT//Projects//GitHub//DevJams22-SAPS//Gray_tiger.jpeg", image1)
