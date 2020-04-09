#105 240
#119 234
import numpy as np
import cv2
import time
a = []

def wow():
    radius=20
    u=109   
    v=184
    area=[]
    avarea=[]
    kernel = np.ones((5,5),np.uint8)
    cap=cv2.VideoCapture(0)
    lastx,lasty=0,0
    x,y=0,0
    numberoftimes=0
    
    _, frame = cap.read()
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gr, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    grad_y = cv2.Sobel(gr, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    lower_color = np.array([0,u-30,v-30])
    upper_color = np.array([255,u+30,v+30])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    thresh=cv2.Canny(mask,100,200)

    _, contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    flag=1
    numberoftimes=numberoftimes+1

    for i in range(len(contours1)):
            area.append(cv2.contourArea(contours1[i]))
            flag=0
    if len(contours1)!=0:
        (x,y),radius = cv2.minEnclosingCircle(contours1[0])

    center = (int(x),int(y))
    r = int(radius)
    for i in range(len(contours1)):
            avarea.append(cv2.contourArea(contours1[i]))
            (x,y),radius = cv2.minEnclosingCircle(contours1[i])
            if radius > r:
                    center = (int(x),int(y))
                    r = int(radius)
                    ind = i

    if len(contours1)!=0:
        (x,y),radius = cv2.minEnclosingCircle(contours1[ind])
    
    center = (int(x),int(y))
    radius=int(radius)

    print (center[0],center[1])
    if center[0] > 21 and center[0] <= 172 and center[1] > 7 and center[1] <= 195:
        a.append("ld1s")
    elif center[0] > 0 and center[0] <= 78 and center[1] > 207 and center[1] <= 478:
        a.append("le1")
    elif center[0] > 78 and center[0] <= 183 and center[1] > 210 and center[1] <= 478:
        a.append("lf1")
    elif center[0] > 190 and center[0] <= 305 and center[1] > 21 and center[1] <= 201:
        a.append("lf1s")
    elif center[0] > 183 and center[0] <= 289 and center[1] > 228 and center[1] <= 478:
        a.append("lg1")
    elif center[0] > 305 and center[0] <= 381 and center[1] > 28 and center[1] <= 209:
        a.append("lg1s")
    elif center[0] > 289 and center[0] <= 403 and center[1] > 282 and center[1] <= 478:
        a.append("ra1")
    elif center[0] > 381 and center[0] <= 487 and center[1] > 44 and center[1] <= 210:
        a.append("ra1s")
    elif center[0] > 416 and center[0] <= 511 and center[1] > 239 and center[1] <= 478:
        a.append("rb1")
    elif center[0] > 524 and center[0] <= 611 and center[1] > 248 and center[1] <= 478:
        a.append("rc2")
    elif center[0] > 549 and center[0] <= 620 and center[1] > 57 and center[1] <= 219:
        a.append("rc2s")
    else:
        print("nope")

    cv2.circle(grad,center,radius,(255,255,255),-1)
    cv2.imshow('grad',grad)
    
    if radius>19:
        lastx=x
        lasty=y
    
    _, contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours1)!=0:
        for i in range(len(contours1)):
            avarea.append(cv2.contourArea(contours1[i]))
            (x,y),radius = cv2.minEnclosingCircle(contours1[i])
            if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
            (x,y),radius = cv2.minEnclosingCircle(contours1[ind])

    cv2.destroyAllWindows()

while True:
    wow()
    var = input()
    if var == 'q':
        break
print (a)
