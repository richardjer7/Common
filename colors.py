
from cozmo.lights import Light, Color

'''
@class Colors
Helper class for Cozmo light colors
@author - Wizards of Coz
'''


class Colors:
    """ Class to define common colors to be used """
    CYAN_2 = Light(on_color=Color(name="cyan", int_color=0x00ffffff), off_color=Color(name="black", int_color=0x00000000), on_period_ms=1000, off_period_ms=500);
    GRAY_2 = Light(on_color=Color(name="gray", int_color=0x808080ff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    MAGENTA_2 = Light(on_color=Color(name="magenta", int_color=0xff00ffff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    YELLOW_2 = Light(on_color=Color(name="yellow", int_color=0xe5e500ff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    GREEN_2 = Light(on_color=Color(name="green", int_color=0x00ff00ff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    RED_2 = Light(on_color=Color(name="red", int_color=0xff0000ff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    BLUE_2 = Light(on_color=Color(name="blue", int_color=0x0000ffff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    WHITE_2 = Light(on_color=Color(name="white", int_color=0xffffffff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);
    TEAL_2 = Light(on_color=Color(name="teal", int_color=0x009688ff), off_color=Color(name="black", int_color=0x00000000),on_period_ms=1000, off_period_ms=500);

    CYAN_1 = Light(on_color=Color(name="cyan", int_color=0x00ffffff),
                   off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    GRAY_1 = Light(on_color=Color(name="gray", int_color=0x808080ff),
                   off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    MAGENTA_1 = Light(on_color=Color(name="magenta", int_color=0xff00ffff),
                      off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    YELLOW_1 = Light(on_color=Color(name="yellow", int_color=0xe5e500ff),
                     off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    GREEN_1 = Light(on_color=Color(name="green", int_color=0x00ff00ff),
                    off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    RED_1 = Light(on_color=Color(name="red", int_color=0xff0000ff), off_color=Color(name="black", int_color=0x00000000),
                  on_period_ms=200, off_period_ms=200);
    BLUE_1 = Light(on_color=Color(name="blue", int_color=0x0000ffff),
                   off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    WHITE_1 = Light(on_color=Color(name="white", int_color=0xffffffff),
                    off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);
    TEAL_1 = Light(on_color=Color(name="teal", int_color=0x009688ff),
                   off_color=Color(name="black", int_color=0x00000000), on_period_ms=200, off_period_ms=200);

    GRAY = Light(Color(name="gray", int_color=0x808080ff))
    MAGENTA = Light(Color(name="magenta", int_color=0xff00ffff))
    YELLOW = Light(Color(name="yellow", int_color=0xe5e500ff))
    GREEN = Light(Color(name="green", int_color=0x00ff00ff))
    RED = Light(Color(name="red", int_color=0xff0000ff))
    BLUE = Light(Color(name="blue", int_color=0x0000ffff))
    WHITE = Light(Color(name="white", int_color=0xffffffff))
    TEAL = Light(Color(name="teal", int_color=0x009688ff))

    OFF = Light(Color(name="off"))