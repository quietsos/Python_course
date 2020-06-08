import cv2      #importing opencv module

print(cv2.__version__)

img = cv2.imread("sohan.jpg",-1)  # imread() function is used to read image converting image in numpy array format.

print(img)
cv2.imshow("Sohan",img)         # imshow() function is used for displaying image that convert numpy array format
k = cv2.waitKey(0)              # waitKey() function is used for define how much time image will display.
if k == 27:
    cv2.destroyAllWindows()     # destroyAllWindows() function is used to remove image from displaying
elif k == ord("s"):             # ord() function is used for inserting specific character
    cv2.imwrite("sohan.png",img)
    cv2.destroyAllWindows()


