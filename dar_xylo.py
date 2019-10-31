import dxl
import time

moved=0
move=0
section=2
radius=20
a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
d.set_torque({i: 1 for i in range(1, 21)})
d.set_speed({i: 1023 for i in range(1, 7)})
x,y=0,0

def knock(a):
    if a == "ln":
        d.move(2, 1700)
        time.sleep(0.07)
        d.move(2, 1100)
    if a == "lfn":
        d.move(2, 1400)
        time.sleep(0.035)
        d.move(2, 1100)
    if a == "ls":
        d.move(2, 1200)
        time.sleep(0.03)
        d.move(2, 1100)
    if a == "rn":
        d.move(1, 2700)
        time.sleep(0.05)
        d.move(1, 3000)
    if a == "rs":
        d.move(1, 2800)
        time.sleep(0.02)
        d.move(1, 3000)


see={1:{19:2343,20:2443},2:{19:1963,20:2443},3:{19:1499,20:2443}}

positions = {
    "init": {2: 1100, 4: 2702, 6: 2048, 1: 3000, 3: 1475, 5: 1819, 19: 1963, 20: 2443},
    "lg": {4: 2576, 6: 2642, 19: 2401},
    "lgs": {4: 2094, 6: 1929, 19: 2401},
    "la": {4: 2653, 6: 2712, 19: 2401},
    "las": {4: 2231, 6: 2266, 19: 2401},
    "lb": {4: 2702, 6: 2830, 19: 2401},
    "lc1": {4: 2618, 6: 2835, 19: 2401},
    "lc1s": {4: 1700, 6: 1740, 19: 2401},
    "ld1": {4: 2548, 6: 2883, 19: 2401},
    "ld1s": {4: 1785, 6: 2000, 19: 2191},
    "le1": {4: 2426, 6: 2920, 19: 2191},
    "lf1": {4: 2279, 6: 2800, 19: 2191},
    "lf1s": {4: 1425, 6: 1680, 19: 2038},
    "lg1": {4: 2055, 6: 2660, 19: 2038},
    "lg1s": {4: 1675, 6: 2190, 19: 2038},
    "la1": {4: 1954, 6: 2700, 19: 2038},
    "la1s": {4: 1444, 6: 1930, 19: 2038},
    "lb1": {4: 1707, 6: 2400, 19: 1810},
    "lc2": {4: 1517, 6: 2231, 19: 1810},
    "rc3": {3: 1793, 5: 2667},
    "rb2": {3: 1577, 5: 2304},
    "ra2s": {3: 1811, 5: 2527},
    "ra2": {3: 1470, 5: 2125},
    "rg2s": {3: 2022, 5: 2702},
    "rg2": {3: 1376, 5: 1949},
    "rf2s": {3: 1979, 5: 2542},
    "rf2": {3: 1398, 5: 1868},
    "re2": {3: 1445, 5: 1840},
    "rd2s": {3: 1969, 5: 2362},
    "rd2": {3: 1406, 5: 1708},
    "rc2s": {3: 2016, 5: 2300},
    "rc2": {3: 1470, 5: 1700},
    "rb1": {3: 1520, 5: 1642},
    "ra1s": {3: 2221, 5: 2422},
    "ra1": {3: 1645, 5: 1720},
    "rg1s": {3: 2322, 5: 2432},
    "rg1": {3: 1816, 5: 1751},
    "rf1s": {3: 2379, 5: 2493},
    "rf1": {3: 1961, 5: 1812},
    "re1": {3: 2137, 5: 1916},
    "rd1s": {3: 2527, 5: 2481},
    "rd1": {3: 2320, 5: 2081},
    "rc1s": {3: 2787, 5: 2759},
    "rc1": {3: 2510, 5: 2233},
}


rtest = "re2 0.5 rn 0.5 rd2s 0.5 rs 0.5 rd2 0.5 rn 0.5 rc2s 0.5 rs 0.5 rc2 0.5 rn 0.5 rb1 0.5 rn"
ltest = "le1 0.5 lfn 0.5 lg1s 0.5 ls 0.5 la1s 0.5 ls 0.5 la1 0.5 lfn 0.5 lf1s 0.5 ls 0.5 la1 0.5 lfn"
las = "las 0.5 ls"
harry_potter = "lb 0.2 ln 0.1 le1 rg1 0.3 lfn  0.2 lf1s 0.4 rn 0.2 ls 0.1 le1 0.1 rb1 0.3 lfn \
                0.3 la1 0.4 rn 0.30 lfn 0.05 rc2 0.05 lf1s 0.8 ln \
                0.1 le1 rg1 0.6 lfn  0.2 lf1s 0.5 rn 0.2 ls 0.1 ld1s 0.1 rf1 0.3 ls\
                0.2 lb 0.4 rn 0.4 ln\
                1 lb 0.2 ln 0.1 le1 rg1 0.3 lfn  0.2 lf1s 0.4 rn 0.2 ls 0.1 le1 0.1 rd2 0.3 ln \
                0.3 lb1 0.4 lfn 0.3 rn 0.1 rc2s lc2 0.7 rs 0.3 lfn \
                0.1 lg1s 0.2 rc2 0.5 ls 0.3 rn 0.1 rb1 la1s 0.5 rn 0.2 ls 0.1 las rg1 0.3 ls \
                0.1 le1 0.5 rn 0.3 lfn \
                0.1 rb1 lg1 1.4 lfn 0.3 rn 0.5 lfn 0.3 rn 0.1 rc2 0.4 lfn 0.1 la1s 0.3 rn 0.1 rb1 \
                0.4 rn 0.3 ls 0.1 lf1s rg1 0.4 ls 0.3 rn 0.1 rb1 la1s 0.2 rn 0.2 ls 0.1 las 0.3 ls\
                0.1 lb rb1 0.4 ln 0.3 rn \
                0.1 rb1 lg1 1 lfn 0.3 rn 0.5 lfn 0.3 rn 0.1 rd2 0.4 lfn 0.2 rn 0.1 rc2s lc2 \
                0.4 rs 0.3 lfn 0.1 lg1s rc2 0.3 ls 0.5 rn 0.1 rb1 la1s 0.2 rn 0.2 ls 0.1 las 0.3 ls\
                0.1 le1 rg1 0.4 rn 0.3 ln 0.2 init"

omsom = "la1 ra1s 0.5 lfn 0.4 rs 0.2 lfn 0.4 rs 0.2 lfn 0.4 rs 0.2 lfn 0.1 lg1 0.15 lfn 0.15 lf1 0.05 rg1 lfn 0.4\
         lfn 0.4 rn 0.2 lfn 0.4 rn 0.2 lfn 0.4 rn 0.2 lfn 0.1 le1 0.15 lfn 0.15 ld1 0.05 re1 lfn 0.4\
         lfn 0.4 rn 0.2 lfn 0.4 rn 0.2 lfn 0.4 rn 0.2 lfn 0.1 lc1 0.15 lfn 0.2 las 0.2 ls 0.2 init"

chinni = "lc1 re1 0.2 lfn 0.1 ld1 0.2 rn 0.1 rf1 0.1 lfn 0.1 le1 0.2 rn 0.2 lfn 0.2 lfn"

kolaveri = "la1 ra1s 0.2 lfn 0.2 rs 0.2 lfn 0.085 lg1 0.085 lfn 0.085 la1s 0.085 lfn 0.2 rs 0.2 lfn 0.085 lg1 0.085 lfn\
            0.085 la1 0.085 lfn 0.2 rs 0.085 rc2 la1s 0.075 ls 0.2 rn 0.2 rn 0.2 ls 0.085 lg1 ra1 0.075 rn 0.2 lfn 0.2 lfn"

animals = "lg1s rc2 0.5 ls 0.45 ls 0.2 la1s 0.3 ls 0.5 rn 0.15 rd2s 0.35 rs 0.15 lg1 ra1s 0.55 rs 0.4 rs 0.15 rg1s\
            0.35 rs 0.5 lfn 0.15 lf1 0.35 lfn\
            0.15 lg1 0.55 lfn 0.4 lfn 0.4 rs 0.4 rs 0.15 lf1 0.25 lfn\
            0.15 lg1 0.55 lfn 0.7 lfn 0.4 rs 0.4 rs 0.15 lf1 0.35 lfn 0.1\
            rc2 la1s 0.4 rn 0.2 rn 0.2 rn 0.2 ls 0.2 ls 0.2 ls 0.1 lg1s 0.1 ls 0.3 ls 0.1 lf1 0.4 lfn"

lc2 = "init 1 la 0.5 ln 1 lb1 0.5 lfn"

ra2s = "rc3 0.5 rn"
d.set_goal_position(positions["init"])
input("start?")
print("starting...")
time.sleep(1)
# for i in lc2.split():
#     try:
#         time.sleep(float(i))
#     except ValueError:
#         if i in positions:
#             d.set_goal_position(positions[i])
#         else:
#             knock(i)


# def dekhdekhdekh():
import numpy as np
import cv2
u=115
v=195
area=[]
avarea=[]
kernel = np.ones((5,5),np.uint8)
cap=cv2.VideoCapture(1)
lastx,lasty=0,0
numberoftimes=0
while True:

        # Take each frame
        _, frame = cap.read()
        gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        grad_x = cv2.Sobel(gr, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        grad_y = cv2.Sobel(gr, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

     


        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

        # define range of blue color in HSV
        lower_color = np.array([0,u-30,v-30])
        upper_color = np.array([255,u+30,v+30])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(frame,frame, mask= mask)

        #cv2.imshow('mask',mask)
    
        thresh=cv2.Canny(mask,100,200)

        contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # print(len(contours1))
        if radius <20:
            if lastx<320:
                move=-1
                print("go left",numberoftimes)

            elif lastx>320:
                move=1
                print("go right",numberoftimes)

            flag=1
            numberoftimes=numberoftimes+1
        # cv2.drawContours(res, contours1, -1 , (0,0,255), 3)
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
        radius = int(radius)
        # print("radius=",radius)
        # cv2.circle(grad,center,radius,(0,0,255),2)
        # print (center[0],center[1])
        # cv2.imshow("im3",frame)
        cv2.circle(grad,center,radius,(255,255,255),-1)
        cv2.imshow('grad',grad)

        if move==-1:
            if section==3:
                section=2
            if section==2:
                section=1
            d.set_goal_position(see[section])

        elif move==1:
            if section==1:
                section=2
            if section==2:
                section=3
            d.set_goal_position(see[section])
            

        if radius>19:
            lastx,lasty=center[0],center[1]
        # cv2.imshow('res',res)
        if cv2.waitKey(5)==27:
            break


cv2.destroyAllWindows()
