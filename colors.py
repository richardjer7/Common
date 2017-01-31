from cozmo.lights import Light, Color

class Colors:
    """ Class to define common colors to be used """
    CYAN = Light(Color(name="cyan", int_color=0x00ffffff))
    MAGENTA = Light(Color(name="magenta", int_color=0xff00ffff))
    YELLOW = Light(Color(name="yellow", int_color=0xffff00ff))
    GREEN = Light(Color(name="green", int_color=0x00ff00ff))
    RED = Light(Color(name="red", int_color=0xff0000ff))
    BLUE = Light(Color(name="blue", int_color=0x0000ffff))
    WHITE = Light(Color(name="white", int_color=0xffffffff))
    OFF = Light(Color(name="off"))