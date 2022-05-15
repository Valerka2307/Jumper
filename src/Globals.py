import pygame
from pygame import mixer

mixer.init()

shoot_sound = mixer.Sound('sounds/laserShoot.wav')
jump_sound = mixer.Sound('sounds/jump.wav')

JUMP_POWER = 10
GRAVITY = 0.4  # Сила, которая будет тянуть нас вниз
MOVE_SPEED = 12
CWIDTH = 32
CHEIGHT = 32
COLOR = "red"

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

ANIMATION_DELAY = 100  # скорость смены кадров
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

pygame.init()

WIDTH = 896
HEIGHT = 640
DISPLAY = (WIDTH, HEIGHT)
BACKGROUND_COLOR = "purple"
PWIDTH = 40
PHEIGHT = 32
PCOLOR = "dark orange"

screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Platform")
bg = pygame.image.load("background/moun.jpg")
back = pygame.image.load("background/back.png")

start_img = pygame.image.load('button/start_btn.png').convert_alpha()
exit_img = pygame.image.load('button/exit_btn.png').convert_alpha()
timer = pygame.time.Clock()
BG = (144, 201, 120)
block = pygame.sprite.Group()
start_game = False

pygame.init()

left = right = False  # по умолчанию — стоим

entities = pygame.sprite.Group()  # Все объекты
platforms = []  # то, во что мы будем врезаться или опираться

mobs = pygame.sprite.Group()

font_name = pygame.font.match_font('arial')
