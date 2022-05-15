import pygame
import pyganim
from random import randrange

ANIMATION_DEL = 120
ANIMATION_MOB = [('mob/mob0.png'),
            ('mob/mob1.png'),
            ('mob/mob2.png'),
            ('mob/mob3.png'),
            ('mob/mob4.png'),
            ('mob/mob5.png')]


class MobLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((35, 35))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.image.set_colorkey('red')
        self.rect.x = -40
        self.rect.y = randrange(0, 896)
        self.speedx = randrange(2, 5)
        self.speedy = randrange(-2, 2)
        boltAnim = []
        for anim in ANIMATION_MOB:
            boltAnim.append((anim, ANIMATION_DEL))
        self.boltAnimMOB = pyganim.PygAnimation(boltAnim)
        self.boltAnimMOB.play()

    def update(self):
        self.boltAnimMOB.blit(self.image, (0, 0))
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > 2000:
            self.rect.x = -40
            self.rect.y = randrange(0, 896)
            self.speedx = randrange(2, 5)
            self.speedy = randrange(-2, 2)


class MobRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((35, 35))
        self.image.fill("red")
        self.rect = self.image.  get_rect()
        self.image.set_colorkey('red')
        self.rect.x = 2040
        self.rect.y = randrange(0, 896)
        self.speedx = randrange(2, 5)
        self.speedy = randrange(-2, 2)
        boltAnim = []
        for anim in ANIMATION_MOB:
            boltAnim.append((anim, ANIMATION_DEL))
        self.boltAnimMOB = pyganim.PygAnimation(boltAnim)
        self.boltAnimMOB.play()

    def update(self):
        self.boltAnimMOB.blit(self.image, (0, 0))
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0:
            self.rect.x = 2040
            self.rect.y = randrange(0, 896)
            self.speedx = randrange(2, 5)
            self.speedy = randrange(-2, 2)
