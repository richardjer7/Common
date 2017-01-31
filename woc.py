import pygame

class WOC:
    def __init__(self):
        pygame.init()

    @property
    def exit_flag(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_ESCAPE):
                    print("EXIT")
                    return True
        return False