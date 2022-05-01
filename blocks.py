from pygame import *


PWIDTH = 32
PHEIGHT = 32
PCOLOR = "dark orange"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PWIDTH, PHEIGHT))
        self.image = image.load("blocks/block2.png")
        self.rect = Rect(x, y, PWIDTH, PHEIGHT)

