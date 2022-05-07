from pygame import *
import pyganim
from shooting import *

JUMP_POWER = 12
GRAVITY = 0.4 # Сила, которая будет тянуть нас вниз
MOVE_SPEED = 9
WIDTH = 32
HEIGHT = 32
COLOR = "red"

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

ANIMATION_DELAY = 60 # скорость смены кадров
ANIMATION_RIGHT = [('character/r0.png'),
            ('character/r1.png'),
            ('character/r2.png')]
ANIMATION_LEFT = [('character/l0.png'),
            ('character/l1.png'),
            ('character/l2.png')]

ANIMATION_JUMP_LEFT = [('character/jl.png', 1)]
ANIMATION_JUMP_RIGHT = [('character/jr.png', 1)]
ANIMATION_JUMP = [('character/j.png', 1)]
ANIMATION_STAY = [('character/s0.png'),
            ('character/s1.png'),
            ('character/s2.png'),
            ('character/s3.png'),
            ('character/s4.png'),
            ('character/s5.png')]
ANIMATION_SHOOT_LEFT = [('character/sl0.png'),
                       ('character/sl1.png'),
                       ('character/sl2.png'),
                       ('character/sl3.png')]
ANIMATION_SHOOT_RIGHT = [('character/sr0.png'),
                        ('character/sr1.png'),
                        ('character/sr2.png'),
                        ('character/sr3.png' )]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.yvel = 0 # скорость вертикального перемещения
        self.onGround = False # На земле ли я?
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево        
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        boltAnim = []
        for anim in ANIMATION_STAY:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimStay = pyganim.PygAnimation(boltAnim)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим
        
        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        
        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        boltAnim = []
        for anim in ANIMATION_SHOOT_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimSL = pyganim.PygAnimation(boltAnim)
        self.boltAnimSL.play()

        boltAnim = []
        for anim in ANIMATION_SHOOT_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimSR = pyganim.PygAnimation(boltAnim)
        self.boltAnimSR.play()

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER

        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED # Право = x + n

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
        
        if up:
            if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
            self.image.fill(Color(COLOR))
            if up: # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:

            self.yvel += GRAVITY

        self.onGround = False; # Мы не знаем, когда мы на земле
        
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = self.rect.bottom
                    self.yvel = 0

    def shoot(self, facing):
        self.facing = facing
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.facing)
        all_sprites.add(bullet)
        bullets.add(bullet)


def anim_shoot():
    if Player.shoot(1):
        self.boltAnimSR.blit(self.image, (0, 0))
    else:
        self.boltAnimSL.blit(self.image, (0, 0))
