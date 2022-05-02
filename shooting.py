import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 12
        self.facing = facing

    def update(self):
        self.rect.x += self.vel * self.facing
        if self.rect.right < 0 or self.rect.left > 900:
            self.kill()
