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


positions = {
    "init": {2 : 1100, 4 : 2702, 6 : 2809, 1 : 3000, 3 : 1475, 5 : 1819, 19 : 2152, 20 : 2442, 7 : 2015, 8 : 2005, 9 : 2070, 10 : 2026, 11 : 1086, 12 : 3012, 13 : 2926, 14 : 1125, 15 : 2001, 16 : 2097, 17 : 2060, 18 : 2031},
    
    "lg"    :   {4 : 2617, 6 : 2367, 19 : 2401},
    "lgs"   :   {4 : 2128, 6 : 1837, 19 : 2401},
    "la"    :   {4 : 2686, 6 : 2555, 19 : 2401},
    "las"   :   {4 : 2177, 6 : 2016, 19 : 2401},
    "lb"    :   {4 : 2733, 6 : 2719, 19 : 2401},
    "lc1"   :   {4 : 2695, 6 : 2802, 19 : 2401},
    "lc1s"  :   {4 : 1825, 6 : 1738, 19 : 2401},
    "ld1"   :   {4 : 2613, 6 : 2829, 19 : 2401},
    "ld1s"  :   {4 : 1751, 6 : 1758, 19 : 2401},
    "le1"   :   {4 : 2523, 6 : 2864, 19 : 2191},
    "lf1"   :   {4 : 2422, 6 : 2866, 19 : 2191},
    "lf1s"  :   {4 : 1603, 6 : 1755, 19 : 2191},
    "lg1"   :   {4 : 2238, 6 : 2793, 19 : 2038},
    "lg1s"  :   {4 : 1499, 6 : 1719, 19 : 2038},
    "la1"   :   {4 : 2099, 6 : 2755, 19 : 2038},
    "la1s"  :   {4 : 1419, 6 : 1707, 19 : 2038},
    "lb1"   :   {4 : 1892, 6 : 2602, 19 : 1810},
    "lc2"   :   {4 : 1701, 6 : 2451, 19 : 1810},

    "rf1"   :   {3 : 2388, 5 : 2063},
    "rf1s"  :   {3 : 2617, 5 : 2494},
    "rg1"   :   {3 : 2176, 5 : 1877},
    "rg1s"  :   {3 : 2382, 5 : 2275},
    "ra1"   :   {3 : 2021, 5 : 1789},
    "ra1s"  :   {3 : 2489, 5 : 2560},
    "rb1"   :   {3 : 1878, 5 : 1742},
    "rc2"   :   {3 : 1757, 5 : 1725},
    "rc2s"  :   {3 : 2296, 5 : 2466},
    "rd2"   :   {3 : 1609, 5 : 1687},
    "rd2s"  :   {3 : 2167, 5 : 2405},
    "re2"   :   {3 : 1521, 5 : 1689},
    "rf2"   :   {3 : 1501, 5 : 1778},
    "rf2s"  :   {3 : 2025, 5 : 2410},
    "rg2"   :   {3 : 1459, 5 : 1841},
    "rg2s"  :   {3 : 2105, 5 : 2626},
    "ra2"   :   {3 : 1490, 5 : 1972},
    "ra2s"  :   {3 : 2171, 5 : 2817},
    "rb2"   :   {3 : 1545, 5 : 2122},
    "rc3"   :   {3 : 1641, 5 : 2328},

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
