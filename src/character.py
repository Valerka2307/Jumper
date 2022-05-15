from pygame import *
import pyganim
from src.shooting import *
import time
from src.Globals import *


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.start_x = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.start_y = y
        self.image = Surface((CWIDTH, CHEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, CWIDTH, CHEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.on_ground = False  # На земле ли я?
        self.counter = 0
        self.last_jump = time.time()
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        bolt_anim = []
        for anim in ANIMATION_RIGHT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_right = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_right.play()
        #        Анимация движения влево
        bolt_anim = []
        for anim in ANIMATION_LEFT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_left = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_left.play()

        bolt_anim = []
        for anim in ANIMATION_STAY:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_stay = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_stay.play()
        self.bolt_anim_stay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.bolt_anim_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.bolt_anim_jump_left.play()

        self.bolt_anim_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.bolt_anim_jump_right.play()

        self.bolt_anim_jump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.bolt_anim_jump.play()

    def update(self, left, right, up, platforms):
        if up:
            # прыгаем, только когда можем оттолкнуться от земли
            if self.counter < 2 and time.time() - self.last_jump > 0.3:
                print(self.counter)
                self.yvel = -JUMP_POWER
                self.counter += 1
                self.last_jump = time.time()
            self.image.fill(Color(COLOR))
            self.bolt_anim_jump.blit(self.image, (0, 0))
            jump_sound.play()

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.bolt_anim_jump_left.blit(self.image, (0, 0))
            else:
                self.bolt_anim_left.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.bolt_anim_jump_right.blit(self.image, (0, 0))
            else:
                self.bolt_anim_right.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.bolt_anim_stay.blit(self.image, (0, 0))

        if self.on_ground:
            self.counter = 0

        if not self.on_ground:
            self.yvel += GRAVITY

        self.on_ground = False  # Мы не знаем, когда мы на земле

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
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
                    self.on_ground = True
                    self.counter = 0
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = self.rect.bottom
                    self.yvel = 0

    def shoot(self, facing):
        self.facing = facing
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.facing)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()
