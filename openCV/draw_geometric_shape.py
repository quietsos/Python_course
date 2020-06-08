import cv2
img = cv2.imread('sohan.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img)
cv2.imshow("sohan",gray)
cv2.waitKey()
cv2.destroyAllWindows()