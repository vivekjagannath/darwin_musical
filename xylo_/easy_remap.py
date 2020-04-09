import dxl

a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
offt = {i:0 for i in range (1,7)}
d.set_torque(offt)

a = ("lg", "lgs", "la", "las", "lb", "lc1", "lc1s", "ld1", "ld1s", "le1", "lf1", "lf1s", "lg1", "lg1s", "la1", "la1s", "lb1", "lc2")
b = ("rf1", "rf1s", "rg1", "rg1s", "ra1", "ra1s", "rb1", "rc2", "rc2s", "rd2", "rd2s", "re2", "rf2", "rf2s", "rg2", "rg2s", "ra2", "ra2s", "rb2", "rc3")
for i in a:
    input()
    print("\"{}\" : {{4 : {}, 6 : {}}}".format(i, d.read(4), d.read(6)))
for i in b:
    input()
    print("\"{}\" : {{3 : {}, 5 : {}}}".format(i, d.read(3), d.read(5)))