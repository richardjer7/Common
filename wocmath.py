import cozmo

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
