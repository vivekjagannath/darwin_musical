import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while 1:
    _, frame = cap.read()
    img_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    mask = cv2.inRange(
        img_yuv, (np.array([0, 97 - 30, 98 - 30])), (np.array([255, 97 + 30, 99 + 30]))
    )
    mask = cv2.dilate(mask, None, iterations=1)
    mask = cv2.erode(mask, None, iterations=5)
    cv2.imshow("out", frame)
    cv2.imshow("masking", mask)
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()
