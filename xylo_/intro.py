import dxl
import time
from pygame import mixer
import numpy as np
import cv2
from playsound import playsound

a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
d.set_torque({i: 1 for i in range(1, 21)})

mixer.init()
mixer.music.load('/home/vivek/Music/para1.mp3')
mixer.music.play()
d.set_speed({i: 100 for i in range(1,7)})
positions = {
    "init": {2 : 1100, 4 : 2702, 6 : 2809, 1 : 3000, 3 : 1475, 5 : 1819, 19 : 2152, 20 : 2442, 7 : 2015, 8 : 2005, 9 : 2070, 10 : 2026, 11 : 1086, 12 : 3012, 13 : 2926, 14 : 1125, 15 : 2001, 16 : 2097, 17 : 2060, 18 : 2031},
    "lg" : {4 : 2525, 6 : 2373, 19 : 2400},
    "lgs" : {4 : 2080, 6 : 1874, 19 : 2400},
    "la" : {4 : 2657, 6 : 2608, 19 : 2400},
    "las" : {4 : 2219, 6 : 2147, 19 : 2400},
    "lb" : {4 : 2682, 6 : 2729, 19 : 2400},
    "lc1" : {4 : 2668, 6 : 2804, 19 : 2400},
    "lc1s" : {4 : 1776, 6 : 1712, 19 : 2400},
    "ld1" : {4 : 2651, 6 : 2865, 19 : 2400},
    "ld1s" : {4 : 1735, 6 : 1750, 19 : 2071},
    "le1" : {4 : 2556, 6 : 2861, 19 : 2071},
    "lf1" : {4 : 2485, 6 : 2886, 19 : 2071},
    "lf1s" : {4 : 1543, 6 : 1676, 19 : 2071},
    "lg1" : {4 : 2362, 6 : 2865, 19 : 2071},
    "lg1s" : {4 : 1608, 6 : 1860, 19 : 2071},
    "la1" : {4 : 2234, 6 : 2826, 19 : 2071},
    "la1s" : {4 : 1493, 6 : 1789, 19 : 2071},
    "lb1" : {4 : 2033, 6 : 2694, 19 : 2071},
    "lc2" : {4 : 1894, 6 : 2589, 19 : 2071},
    "rf1" : {3 : 2495, 5 : 2232},
    "rf1s" : {3 : 2659, 5 : 2642},
    "rg1" : {3 : 2227, 5 : 2006},
    "rg1s" : {3 : 2437, 5 : 2404},
    "ra1" : {3 : 2060, 5 : 1897},
    "ra1s" : {3 : 2507, 5 : 2653},
    "rb1" : {3 : 1911, 5 : 1818},
    "rc2" : {3 : 1813, 5 : 1798},
    "rc2s" : {3 : 2284, 5 : 2534},
    "rd2" : {3 : 1744, 5 : 1830},
    "rd2s" : {3 : 2270, 5 : 2605},
    "re2" : {3 : 1634, 5 : 1787},
    "rf2" : {3 : 1629, 5 : 1896},
    "rf2s" : {3 : 2153, 5 : 2636},
    "rg2" : {3 : 1642, 5 : 2024},
    "rg2s" : {3 : 2127, 5 : 2691},
    "ra2" : {3 : 1648, 5 : 2128},
    "ra2s" : {3 : 2066, 5 : 2696},
    "rb2" : {3 : 1693, 5 : 2270},
    "rc3" : {3 : 1815, 5 : 2546},

    "dg"    :   {4 : 2617, 6 : 2367, 3 : 2176, 5 : 1877, 19 : 2401},
    "dgs"   :   {4 : 2128, 6 : 1837, 3 : 2382, 5 : 2275, 19 : 2401},
    "da"    :   {4 : 2686, 6 : 2555, 3 : 2021, 5 : 1789, 19 : 2401},
    "das"   :   {4 : 2177, 6 : 2016, 3 : 2489, 5 : 2560, 19 : 2401},
    "db"    :   {4 : 2733, 6 : 2719, 3 : 1878, 5 : 1742, 19 : 2401},
    "dc1"   :   {4 : 2695, 6 : 2802, 3 : 1757, 5 : 1725, 19 : 2401},
    "dc1s"  :   {4 : 1825, 6 : 1738, 3 : 2296, 5 : 2466, 19 : 2401},
    "dd1"   :   {4 : 2613, 6 : 2829, 3 : 1609, 5 : 1687, 19 : 2401},
    "dd1s"  :   {4 : 1751, 6 : 1758, 3 : 2167, 5 : 2405, 19 : 2401},
    "de1"   :   {4 : 2523, 6 : 2864, 3 : 1521, 5 : 1689, 19 : 2191},
    "df1"   :   {4 : 2422, 6 : 2866, 3 : 1501, 5 : 1778, 19 : 2191},
    "df1s"  :   {4 : 1603, 6 : 1755, 3 : 2025, 5 : 2410, 19 : 2191},
    "dg1"   :   {4 : 2238, 6 : 2793, 3 : 1459, 5 : 1841, 19 : 2038},
    "dg1s"  :   {4 : 1499, 6 : 1719, 3 : 2105, 5 : 2626, 19 : 2038},
    "da1"   :   {4 : 2099, 6 : 2755, 3 : 1490, 5 : 1972, 19 : 2038},
    "da1s"  :   {4 : 1419, 6 : 1707, 3 : 2171, 5 : 2817, 19 : 2038},
    "db1"   :   {4 : 1892, 6 : 2602, 3 : 1545, 5 : 2122, 19 : 1810},
    "dc2"   :   {4 : 1701, 6 : 2451, 3 : 1641, 5 : 2328, 19 : 1810}
}
hi1 = {1 : 3993, 2 : 1109, 3 : 1876, 4 : 2698, 5 : 2233, 6 : 2806, 19 : 2154, 20 : 2440}
hi2 = {1 : 3993, 2 : 1109, 3 : 1872, 4 : 2698, 5 : 1857, 6 : 2806, 19 : 2154, 20 : 2440}
pos1 = {1 : 3100, 2 : 1105, 3 : 1495, 4 : 2816, 5 : 2199, 6 : 2425, 19 : 2154, 20 : 2440}
pos2 = {1 : 2994, 2 : 1009, 3 : 2128, 4 : 2303, 5 : 1917, 6 : 2821, 19 : 2150, 20 : 2460}
pos3 = {1 : 3950, 2 : 44, 3 : 1237, 4 : 2952, 5 : 2415, 6 : 2291, 19 : 2154, 20 : 2440}
d.set_goal_position(hi1)
time.sleep(1)
d.set_goal_position(hi2)
time.sleep(1)
d.set_goal_position(hi1)
time.sleep(1)
d.set_goal_position(hi2)
time.sleep(1)
d.set_goal_position(positions["init"])
time.sleep(4)
d.set_goal_position(pos1)
time.sleep(5)
d.set_goal_position(pos2)
time.sleep(6)
d.set_goal_position(pos3)
time.sleep(4)
d.set_goal_position(pos1)
time.sleep(5)
d.set_goal_position(pos2)
time.sleep(6)
d.set_goal_position(pos3)
time.sleep(4)
d.set_goal_position(pos1)
time.sleep(5)
d.set_goal_position(pos2)
time.sleep(6)
d.set_goal_position(pos3)
time.sleep(4)
d.set_goal_position(positions["init"])
input()
def knock(a):
    if a == "ln":
        d.move(2, 1400)
        time.sleep(0.07)
        d.move(2, 1100)
    if a == "lfn":
        d.move(2, 1400)
        time.sleep(0.05)
        d.move(2, 1100)
    if a == "ls":
        d.move(2, 1300)
        time.sleep(0.03)
        d.move(2, 1100)
    if a == "rn":
        d.move(1, 2800)
        time.sleep(0.05)
        d.move(1, 3000)
    if a == "rs":
        d.move(1, 2830)
        time.sleep(0.02)
        d.move(1, 3000)
    if a == "dn":
        d.set_goal_position({1: 2800, 2: 1400})
        time.sleep(0.06)
        d.set_goal_position({1: 3000, 2: 1100})
    if a == "ds":
        d.set_goal_position({1: 2830, 2: 1300})
        time.sleep(0.06)
        d.set_goal_position({1: 3000, 2: 1100})





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


playsound('/home/vivek/Music/para2_1.mp3')
input()
mixer.music.load('/home/vivek/Music/para2_2.1.mp3')
mixer.music.play()
d.set_speed({i:1024 for i in range(1,7)})
time.sleep(1)
d.set_goal_position(positions["ld1s"])
d.set_goal_position(positions["rc2s"])
time.sleep(4)
knock("ls")
time.sleep(0.5)
knock("rs")
time.sleep(1)
d.set_goal_position(positions["le1"])
time.sleep(0.5)
d.move(2, 1400)
time.sleep(2)
d.move(2, 1100)
time.sleep(1)
d.set_goal_position(pos1)
input()

lis = []
dictio = {19: 2071, 20: 2053}
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
    if center[0] > 0 and center[0] <= 144 and center[1] > 0 and center[1] <= 181:
        lis.append("ld1s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 0 and center[0] <= 64 and center[1] > 197 and center[1] <= 480:
        lis.append("le1")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 64 and center[0] <= 197 and center[1] > 193 and center[1] <= 480:
        lis.append("lf1")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 186 and center[0] <= 295 and center[1] > 0 and center[1] <= 180:
        lis.append("lf1s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 197 and center[0] <= 304 and center[1] > 189 and center[1] <= 480:
        lis.append("lg1")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 295 and center[0] <= 369 and center[1] > 0 and center[1] <= 183:
        lis.append("lg1s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 304 and center[0] <= 405 and center[1] > 203 and center[1] <= 480:
        lis.append("ra1")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 369 and center[0] <= 455 and center[1] > 0 and center[1] <= 177:
        lis.append("ra1s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 405 and center[0] <= 517 and center[1] > 203 and center[1] <= 480:
        lis.append("rb1")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 517 and center[0] <= 640 and center[1] > 206 and center[1] <= 480:
        lis.append("rc2")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    elif center[0] > 550 and center[0] <= 640 and center[1] > 0 and center[1] <= 181:
        lis.append("rc2s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
    else:
        lis.append("lf1s")
        playsound("/home/vivek/Music/para2_2.2.mp3")
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
    time.sleep(3)
    wow()
time.sleep(5)
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
time.sleep(1)
d.set_goal_position(positions["init"])
input()
playsound('/home/vivek/Music/para2_3.mp3')
input()
playsound('/home/vivek/Music/para3_1.mp3')
input("start?")
print("starting...")
time.sleep(1)
for i in harry_potter.split():
    try:
        time.sleep(float(i))
    except ValueError:
        if i in positions:
            d.set_goal_position(positions[i])
        else:
            knock(i)
