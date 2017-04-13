import cozmo
from cozmo.faces import EvtFaceObserved, EvtFaceAppeared, EvtFaceDisappeared

async def initFaceHandlers(coz_conn: cozmo.conn.CozmoConnection,
                           f_ob, f_ap, f_dis):
    robot = await coz_conn.wait_for_robot()
    world = robot.world
    world.add_event_handler(EvtFaceObserved, f_ob)
    world.add_event_handler(EvtFaceAppeared, f_ap)
    world.add_event_handler(EvtFaceDisappeared, f_dis)


