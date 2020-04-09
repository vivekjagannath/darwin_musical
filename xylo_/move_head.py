import dxl

a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(21))
d.set_torque({i: 1 for i in range(1, 21)})
d.set_speed({i: 1023 for i in range(1, 7)})

d.move(19, 1963)
