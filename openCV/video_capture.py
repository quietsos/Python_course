import cv2
import time

# Capturing single frame:
#
# video = cv2.VideoCapture(0)
# check, frame = video.read()
# print(check)
# print(frame)
# time.sleep(3)
# cv2.imshow("1st frame", frame)
# cv2.waitKey(2000)
# video.release()
# cv2.destroyAllWindows()

# Capturing multiple color frame:

# cap = cv2.VideoCapture(0);
#
# k = cv2.waitKey(0)
#
# while(True):
#     ret,frame = cap.read()
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(1) & k == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# Capturing multiple gray frame:

# cap = cv2.VideoCapture(0);
#
# k = cv2.waitKey(0)
# while(True):
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame", gray)
#
#     if cv2.waitKey(1) & k == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
#

# Video streaming from hardisk:

# cap = cv2.VideoCapture("/media/quiet/3492bf6f-3b91-43c7-8929-bb29bbd29817/songs/Zaroori.mp4");
#
# k = cv2.waitKey(0)
# print((cap.isOpened()))
# while(cap.isOpened()):
#     ret,frame = cap.read()
#
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(1) & k == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# Reading height,width and count of frame:

# cap = cv2.VideoCapture(0);
#
# k = cv2.waitKey(0)
# print(cap.isOpened())
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(1) & k == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# Video captured and shaved:

cap = cv2.VideoCapture(0)    # here videoCapture(0) class is used for using default laptop camera.

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # videowriter_fourcc() class is used for defining video fourcc code
out = cv2.VideoWriter("video.avi",fourcc,20.0,(640,480))   # capturing video used video.writer(filename, fourcc, frame count, frame size)

print(cap.isOpened())
k = cv2.waitKey(0)

while(cap.isOpened()):
    ret,frame = cap.read() # ret define is frame available or not and frame is the captured frame

    if ret == True:

        cv2.imshow("video",frame)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        if cv2.waitKey(1) & k == ord("q"):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
