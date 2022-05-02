import pygame
from pygame import *
from character import *
from blocks import *
from camera import *
from shooting import *

WIDTH = 900
HEIGHT = 640
DISPLAY = (WIDTH, HEIGHT)
BACKGROUND_COLOR = "purple"
PWIDTH = 32
PHEIGHT = 32
PCOLOR = "dark orange"

timer = pygame.time.Clock()

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIDTH / 2, -t + HEIGHT / 2

    l = min(0, l) # Не движемся дальше левой границы
    l = max(-(camera.width-WIDTH), l) # Не движемся дальше правой границы
    t = max(-(camera.height-HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t) # Не движемся дальше верхней границы

    return Rect(l, t, w, h)

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Platform")
    bg = pygame.image.load("background/moun.jpg")
    
    hero = Player(55,55) # создаем героя по (x,y) координатам
    left = right = False    # по умолчанию — стоим

    entities = pygame.sprite.Group() # Все объекты
    platforms = [] # то, во что мы будем врезаться или опираться
    entities.add(hero)

    level = [
       "-----------------------------------------------",
       "-                                             -",
       "-                       --                    -",
       "-                                             -",
       "-            --                 -----         -",
       "-                                             -",
       "--                                            -",
       "-                                             -",
       "-                   ----     ---              -",
       "-                                             -",
       "-                                             -",
       "--                                    ----    -",
       "-                                             -",
       "-                                             -",
       "-                                             -", 
       "-                            ---              -",
       "-                                             -",
       "-                                             -",
       "-      ---                       --- --       -",
       "-                                             -",
       "-                                             -",
       "-   -------         ----                      -",
       "-                                             -",
       "-                         -                   -",
       "-                                             -",
       "-                            --               -",
       "-                                             -",
       "-                                             -",
       "-----------------------------------------------"]
    up = False
    
    x=y=0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)

            x += PWIDTH
        y += PHEIGHT
        x = 0
    lastMove = "right"

    total_level_width  = len(level[0])*PWIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PHEIGHT   # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    
    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
                lastMove = "left"
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
                lastMove = "right"

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
                lastMove = "right"
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
                lastMove = "left"
            
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == KEYUP and e.key == K_f:
                if lastMove == "right":
                    hero.shoot(1)
                else:
                    hero.shoot(-1)

            if e.type == QUIT:
                exit()

        screen.blit(bg, (0, 0))

        hero.update(left, right, up, platforms) # передвижение

        camera.update(hero) # центризируем камеру относительно персонажа
        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        all_sprites.draw(screen)
        pygame.display.update()        

if __name__ == "__main__":
    main()

