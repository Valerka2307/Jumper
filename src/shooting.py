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

        bolt_anim = []
        for anim in ANIMATION_FIREBALL:
            bolt_anim.append((anim, ANIMATION_DEL))
        self.bolt_anim_fb = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_fb.play()

    def update(self):
        self.bolt_anim_fb.blit(self.image, (0, 0))
        self.rect.x += self.vel * self.facing
        if self.rect.right < 0 or self.rect.left > 2000:
            self.kill()