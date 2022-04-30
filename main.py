import pygame
from pygame import *
from character import Player
from blocks import Platform


WIDTH = 800
HEIGHT = 640
DISPLAY = (WIDTH, HEIGHT)
BACKGROUND_COLOR = "purple"

PWIDTH = 32
PHEIGHT = 32
PCOLOR = "dark orange"

timer = pygame.time.Clock()

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Platform")
    bg = Surface((WIDTH,HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    
    hero = Player(55,55) # создаем героя по (x,y) координатам
    left = right = False    # по умолчанию — стоим

    entities = pygame.sprite.Group() # Все объекты
    platforms = [] # то, во что мы будем врезаться или опираться
    entities.add(hero)

    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

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

    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == QUIT:
                exit()
        screen.blit(bg, (0,0))

        hero.update(left, right, up, platforms) # передвижение
        entities.draw(screen) # отображение всего

        pygame.display.update()        

if __name__ == "__main__":
    main()

