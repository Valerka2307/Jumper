import pygame
import pyganim

ANIMATION_DEL = 120 # скорость смены кадров
ANIMATION_FIREBALL = [('character/fb0.png'),
            ('character/fb1.png'),
            ('character/fb2.png'),
            ('character/fb3.png'),
            ('character/fb4.png'),
            ('character/fb5.png')]


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 5
        self.vel = 15
        self.image.set_colorkey('yellow')
        self.facing = facing

        bolt_Anim = []
        for anim in ANIMATION_FIREBALL:
            bolt_Anim.append((anim, ANIMATION_DEL))
        self.bolt_Anim_FB = pyganim.PygAnimation(bolt_Anim)
        self.bolt_Anim_FB.play()

    def update(self):
        self.bolt_Anim_FB.blit(self.image, (0, 0))
        self.rect.x += self.vel * self.facing
        if self.rect.right < 0 or self.rect.left > 2000:
            self.kill()