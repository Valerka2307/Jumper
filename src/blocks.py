import pygame
from pygame import sprite
from pygame import Surface
from pygame import image
from pygame import Rect
from src.Globals import *

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PWIDTH, PHEIGHT))
        self.image = image.load("blocks/block8.png")
        self.rect = Rect(x, y, PWIDTH, PHEIGHT)

