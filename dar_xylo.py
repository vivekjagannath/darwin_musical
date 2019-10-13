import dxl
import time

a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
d.set_torque({i: 1 for i in range(1, 21)})
d.set_speed({i: 1023 for i in range(1, 7)})


def knock(a):
    if a == "ln":
        d.move(2, 1610)
        time.sleep(0.06)
        d.move(2, 1100)
    if a == "lfn":
        d.move(2, 1430)
        time.sleep(0.06)
        d.move(2, 1100)
    if a == "ls":
        d.move(2, 1250)
        time.sleep(0.02)
        d.move(2, 1100)
    if a == "rn":
        d.move(1, 2700)
        time.sleep(0.05)
        d.move(1, 2960)
    if a == "rs":
        d.move(1, 2800)
        time.sleep(0.02)
        d.move(1, 2960)


positions = {
    "init": {2: 1100, 4: 2702, 6: 2809, 1: 2960, 3: 1475, 5: 1819, 19: 2038, 20: 2186},
    "las": {4: 2231, 6: 2266, 19: 2401},
    "lb": {4: 2702, 6: 2830, 19: 2401},
    "lc1": {4: 2618, 6: 2835, 19: 2401},
    "lc1s": {4: 1700, 6: 1740, 19: 2401},
    "ld1": {4: 2548, 6: 2883, 19: 2401},
    "ld1s": {4: 1785, 6: 2000, 19: 2191},
    "le1": {4: 2426, 6: 2920, 19: 2191},
    "lf1": {4: 2179, 6: 2800, 19: 2191},
    "lf1s": {4: 1425, 6: 1680, 19: 2038},
    "lg1": {4: 2055, 6: 2660, 19: 2038},
    "lg1s": {4: 1700, 6: 2190, 19: 2038},
    "la1": {4: 1954, 6: 2700, 19: 2038},
    "la1s": {4: 1464, 6: 1930, 19: 2038},
    "lb1": {4: 1707, 6: 2400, 19: 1810},
    "lc2": {4: 1517, 6: 2231, 19: 1810},
    "re2": {3: 1445, 5: 1840},
    "rd2s": {3: 1969, 5: 2362},
    "rd2": {3: 1406, 5: 1708},
    "rc2s": {3: 2016, 5: 2300},
    "rc2": {3: 1470, 5: 1700},
    "rb1": {3: 1520, 5: 1642},
    "ra1s": {3: 2221, 5: 2422},
    "ra1": {3: 1645, 5: 1720},
    "rg1s": {3: 2272, 5: 2432},
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
ltest = "las 0.5 ls 0.5 le1 0.5 lfn 0.5 lg1s 0.5 ls 0.5 la1s 0.5 ls 0.5 la1 0.5 lfn 0.5 lf1s 0.5 ls 0.5 la1 0.5 lfn"
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

naya = "la1 0.5 ln"
d.set_goal_position(positions["init"])
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
