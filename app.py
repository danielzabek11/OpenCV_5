import numpy as np
import cv2


cap = cv2.VideoCapture(0)


while True:
    ret, frame =cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([1, 107, 69])
    upper_red = np.array([179, 255, 99])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    result = cv2.bitwise_and(frame, frame, mask=mask) #checking for green pixels in range to keep in our image

    #Display each frame
    cv2.imshow('frame', result)
    
    if cv2.waitKey(1) == ord('q'):
        break


# After the loop release the cap object (relase our webcam so it can be used by other programs)
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()