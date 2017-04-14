import cozmo
from math import log, sqrt, atan2

def running_average_pos(old: cozmo.util.Position, new: cozmo.util.Position, a: float):
    xx = new.x * a + old.x * (1-a)
    yy = new.y * a + old.y * (1-a)
    zz = new.z * a + old.z * (1-a)
    return cozmo.util.Position(xx,yy,zz)

def distance2(pos1: cozmo.util.Position, pos2: cozmo.util.Position):
    xx = pos1.x - pos2.x
    yy = pos1.y - pos2.y
    zz = pos1.z - pos2.z
    return xx * xx + yy * yy + zz * zz

def linear_mapping(x1:float, y1:float, x2:float, y2:float, vx:float):
    # y = k*x + b
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k * vx + b

def log_mapping(x1:float, y1:float, x2:float, y2:float, vx:float, base:float):
    xl1 = log(x1, base)
    xl2 = log(x2, base)
    vxl = log(vx, base)
    return linear_mapping(xl1, y1, xl2, y2, vxl)

def tupleMagnitude(v1, v2):
    return sqrt(sum((a*b) for a,b in zip(v1, v2)))

def tupleRadians(v):
    return atan2(v[1], v[0])


# test case
if __name__ == '__main__':
    r = log_mapping(10,1,100,2,50,10)
    print(r)
