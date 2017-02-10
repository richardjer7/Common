import cozmo

def running_average_pos(old: cozmo.util.Position, new: cozmo.util.Position, a: float):
    xx = new.x * a + old.x * (1-a)
    yy = new.y * a + old.y * (1-a)
    zz = new.z * a + old.z * (1-a)
    return cozmo.util.Position(xx,yy,zz)
