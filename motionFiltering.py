import cv2

vid=cv2.VideoCapture(0)
#sub=cv2.createBackgroundSubtractorMOG2(20,30)
sub=cv2.createBackgroundSubtractorKNN(20,350)
while True:
    ret,frame=vid.read()
    if ret:
        mask=sub.apply(frame)
        cv2.imshow('Mask: ',mask)
        if cv2.waitKey(5)==ord('e'):
            break


cv2.destroyAllWindows()
vid.release()
