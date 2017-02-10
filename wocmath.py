import cozmo

def running_average_pos(old: cozmo.util.Position, new: cozmo.util.Position, a: float):
    xx = new.x * a + old.x * a
    yy = new.y * a + old.y * a
    zz = new.z * a + old.z * a
    return cozmo.util.Position(xx,yy,zz)
