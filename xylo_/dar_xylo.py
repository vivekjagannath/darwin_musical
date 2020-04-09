#360
import dxl
import time
import numpy as np
import cv2

a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
d.set_torque({i: 1 for i in range(1, 21)})
d.set_speed({i: 1023 for i in range(1, 7)})


def knock(a):
    if a == "ln":
        d.move(2, 1700)
        time.sleep(0.07)
        d.move(2, 1100)
    if a == "lfn":
        d.move(2, 1400)
        time.sleep(0.045)
        d.move(2, 1100)
    if a == "ls":
        d.move(2, 1220)
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
    if a == "dn":
        d.set_goal_position({1: 2700, 2: 1550})
        time.sleep(0.06)
        d.set_goal_position({1: 3000, 2: 1100})
    if a == "ds":
        d.set_goal_position({1: 2800, 2: 1200})
        time.sleep(0.06)
        d.set_goal_position({1: 3000, 2: 1050})


positions = {
    "init": {2: 1100, 4: 2702, 6: 2809, 1: 3000, 3: 1475, 5: 1819, 19: 2095, 20: 2088},
    "lg" : {4 : 2626, 6 : 2429, },
    "lgs" : {4 : 2166, 6 : 1896},
    "la" : {4 : 2749, 6 : 2637},
    "las" : {4 : 2311, 6 : 2175},
    "lb" : {4 : 2759, 6 : 2740},
    "lc1" : {4 : 2745, 6 : 2810},
    "lc1s" : {4 : 1920, 6 : 1835},
    "ld1" : {4 : 2528, 6 : 2767},
    "ld1s" : {4 : 1891, 6 : 1955},
    "le1" : {4 : 2610, 6 : 2885},
    "lf1" : {4 : 2515, 6 : 2886},
    "lf1s" : {4 : 1686, 6 : 1824},
    "lg1" : {4 : 2410, 6 : 2863},
    "lg1s" : {4 : 1697, 6 : 1912},
    "la1" : {4 : 2275, 6 : 2818},
    "la1s" : {4 : 1564, 6 : 1808},
    "lb1" : {4 : 2090, 6 : 2705},
    "lc2" : {4 : 1961, 6 : 2627},
    "rf1" : {3 : 2540, 5 : 2256},
    "rf1s" : {3 : 2615, 5 : 2600},
    "rg1" : {3 : 2223, 5 : 2024},
    "rg1s" : {3 : 2738, 5 : 2984},
    "ra1" : {3 : 1976, 5 : 1866},
    "ra1s" : {3 : 2566, 5 : 2848},
    "rb1" : {3 : 1871, 5 : 1845},
    "rc2" : {3 : 1764, 5 : 1806},
    "rc2s" : {3 : 2396, 5 : 2758},
    "rd2" : {3 : 1663, 5 : 1800},
    "rd2s" : {3 : 2314, 5 : 2728},
    "re2" : {3 : 1559, 5 : 1800},
    "rf2" : {3 : 1546, 5 : 1873},
    "rf2s" : {3 : 2256, 5 : 2820},
    "rg2" : {3 : 1580, 5 : 1994},
    "rg2s" : {3 : 2257, 5 : 2910},
    "ra2" : {3 : 1651, 5 : 2137},
    "ra2s" : {3 : 2229, 5 : 2932},
    "rb2" : {3 : 1684, 5 : 2275},
    "rc3" : {3 : 1833, 5 : 2571},
    "dg": {4: 2576, 6: 2642, 19: 2401, 3: 1816, 5: 1751},
    "dgs": {4: 2094, 6: 1929, 19: 2401, 3: 2322, 5: 2432},
    "da": {4: 2653, 6: 2712, 19: 2401, 3: 1645, 5: 1720},
    "das": {4: 2231, 6: 2266, 19: 2401, 3: 2221, 5: 2422},
    "db": {4: 2702, 6: 2830, 19: 2401, 3: 1520, 5: 1642},
    "dc1": {4: 2618, 6: 2835, 19: 2401, 3: 1470, 5: 1700},
    "dc1s": {4: 1700, 6: 1740, 19: 2401, 3: 2016, 5: 2300},
    "dd1": {4: 2548, 6: 2883, 19: 2401, 3: 1406, 5: 1708},
    "dd1s": {4: 1785, 6: 2000, 19: 2191, 3: 1969, 5: 2362},
    "de1": {4: 2426, 6: 2920, 19: 2191, 3: 1445, 5: 1840},
    "df1": {4: 2279, 6: 2800, 19: 2191, 3: 1398, 5: 1868},
    "df1s": {4: 1425, 6: 1680, 19: 2038, 3: 1979, 5: 2542},
    "dg1": {4: 2055, 6: 2660, 19: 2038, 3: 1376, 5: 1949},
    "dg1s": {4: 1675, 6: 2190, 19: 2038, 3: 2022, 5: 2702},
    "da1": {4: 1954, 6: 2700, 19: 2038, 3: 1470, 5: 2125},
    "da1s": {4: 1444, 6: 1930, 19: 2038, 3: 1811, 5: 2527},
    "db1": {4: 1670, 6: 2400, 19: 1810, 3: 1577, 5: 2304},
    "dc2": {4: 1517, 6: 2231, 19: 1810, 3: 1793, 5: 2667},
}


rtest = "re2 0.5 rn 0.5 rd2s 0.5 rs 0.5 rd2 0.5 rn 0.5 rc2s 0.5 rs 0.5 rc2 0.5 rn 0.5 rb1 0.5 rn"
ltest = "le1 0.5 lfn 0.5 lg1s 0.5 ls 0.5 la1s 0.5 ls 0.5 la1 0.5 lfn 0.5 lf1s 0.5 ls 0.5 la1 0.5 lfn"
las = "lb1 0.5 ln"
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

lc2 = "init 1 dg 0.5 dn 1 lb1 0.5 lfn"
ra2s = "rc3 0.5 rn"

harry_potter_new = "lb 0.5 ln 0.1 de1 0.3 dn 0.2 rg1 lf1s 0.4 rn 0.2 ls 0.2 de1 0.3 dn 0.1 lb1 0.4 lfn 0.1 da1 0.4 dn\
                    0.2 df1s 0.3 ds 0.2 de1 0.3 dn 0.2 rg1 lf1s 0.3 rn 0.2 ls 0.1 rd1s 0.3 rs 0.1 lf1 0.4 lfn 0.1 db 0.4 dn"
hp1 = "lb 0.2 ln 0.1 de1 0.3 dn  0.2 rg1 lf1s 0.4 rn 0.2 ls 0.1 de1 0.4 dn 0.2 db1 \
        0.5 dn 0.1 da1 0.2 dn 0.3 df1s 0.6 ds \
        0.1 de1 0.6 dn  0.2 rg1 lf1s 0.5 rn 0.2 ls 0.1 dd1s 0.4 ds \
        0.2 df1 0.4 dn 0.1 db 0.3 dn \
        1 lb 0.2 ln 0.1 de1 0.3 dn  0.2 rg1 lf1s 0.4 rn 0.2 ls 0.1 de1 0.4 dn \
        0.3 lb1 0.4 lfn 0.1 dd1 0.2 dn 0.1 dc1s 0.7 ds 0.1 dc1 0.2 dn"
# d.set_goal_position(positions["init"])
# input("start?")
# print("starting...")
# time.sleep(1)
# for i in hp1.split():
#     try:
#         time.sleep(float(i))
#     except ValueError:
#         if i in positions:
#             d.set_goal_position(positions[i])
#         else:
#             knock(i)

lis = []
dictio = {19: 2095, 20: 2088}
d.set_goal_position(dictio)
def wow():
    moved=1
    move=0
    section=2
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
    if center[0] > 0 and center[0] <= 166 and center[1] > 0 and center[1] <= 174:
        lis.append("ld1s")
    elif center[0] > 0 and center[0] <= 92 and center[1] > 238 and center[1] <= 480:
        lis.append("le1")
    elif center[0] > 92 and center[0] <= 198 and center[1] > 238 and center[1] <= 480:
        lis.append("lf1")
    elif center[0] > 186 and center[0] <= 299 and center[1] > 0 and center[1] <= 170:
        lis.append("lf1s")
    elif center[0] > 198 and center[0] <= 303 and center[1] > 234 and center[1] <= 480:
        lis.append("lg1")
    elif center[0] > 299 and center[0] <= 373 and center[1] > 0 and center[1] <= 173:
        lis.append("lg1s")
    elif center[0] > 303 and center[0] <= 409 and center[1] > 203 and center[1] <= 480:
        lis.append("ra1")
    elif center[0] > 373 and center[0] <= 459 and center[1] > 0 and center[1] <= 167:
        lis.append("ra1s")
    elif center[0] > 409 and center[0] <= 520 and center[1] > 201 and center[1] <= 480:
        lis.append("rb1")
    elif center[0] > 520 and center[0] <= 640 and center[1] > 200 and center[1] <= 480:
        lis.append("rc2")
    elif center[0] > 549 and center[0] <= 640 and center[1] > 0 and center[1] <= 73:
        lis.append("rc2s")
    else:
        print("nope")
    # cv2.imshow("im3",frame)
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

for i in range(5):
    wow()
    time.sleep(3)
for i in lis:
    d.set_goal_position(positions[i])
    time.sleep(1)
    if i == "ld1s" or i == "lf1s" or i == "lg1s":
        knock("ls")
    elif i == "le1" or i == "lf1" or i == "lg1":
        knock("lfn")
    elif i == "ra1" or i == "rb1" or i == "rc2":
        knock("rn")
    elif i == "ra1s" or i == "rc2s":
        knock ("rs")
    time.sleep(1)