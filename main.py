import pygame
from pygame import *
from character import *
from blocks import *
from camera import *
from shooting import *
from mob import *


WIDTH = 900
HEIGHT = 640
DISPLAY = (WIDTH, HEIGHT)
BACKGROUND_COLOR = "purple"
PWIDTH = 40
PHEIGHT = 32
PCOLOR = "dark orange"

timer = pygame.time.Clock()

block = pygame.sprite.Group()


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIDTH / 2, -t + HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Platform")
    bg = pygame.image.load("background/moun.jpg")

    hero = Player(900, 500)   # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    mobs = pygame.sprite.Group()

    font_name = pygame.font.match_font('arial')

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, "dark orange")
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    n = 2
    k = 1
    for i in range(n):
        m1 = MobLeft()
        all_sprites.add(m1)
        mobs.add(m1)

    for i in range(n):
        m2 = MobRight()
        all_sprites.add(m2)
        mobs.add(m2)

    score = 0
    score1 = 0
    if score - score1 == 30 * k:
        k += 1
        n += 1
        m += 1
        score1 == score

    level = [
        "--------------------------------------------------",
        "-                                                -",
        "-                       --                       -",
        "-                                                -",
        "-            --                    -----         -",
        "-                                                -",
        "--                                               -",
        "-                                                -",
        "-                   ----     ---                 -",
        "-                                                -",
        "-                                                -",
        "--                                     ----      -",
        "-                                                -",
        "-                                                -",
        "-                                                -",
        "-                            ---                 -",
        "-                                                -",
        "-                                                -",
        "-      ---                       --- --          -",
        "-                                                -",
        "-                                                -",
        "-   -------         ----                         -",
        "-                                                -",
        "-                          -                     -",
        "-                                                -",
        "-                               --               -",
        "-                                                -",
        "-                                                -",
        "--------------------------------------------------"]
    up = False

    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PWIDTH
        y += PHEIGHT
        x = 0
    lastMove = "right"

    total_level_width = len(level[0]) * PWIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PHEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    mixer.init()
    mixer.music.load('sounds/phoneMusic.mp3')
    mixer.music.set_volume(1.1)
    mixer.music.play(loops=-1)
    running = True

    while running:
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

            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == KEYUP and e.key == K_SPACE:
                if lastMove == "right":
                    hero.shoot(1)
                else:
                    hero.shoot(-1)

            if e.type == QUIT:
                exit()

        mixer.init()
        exp_sound = mixer.Sound('sounds/explosion.wav')
        # Обновление
        all_sprites.update()

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

        for hit in hits:
            score += 30
            exp_sound.play()
            m1 = MobLeft()
            all_sprites.add(m1)
            mobs.add(m1)

        for hit in hits:
            score += 30
            exp_sound.play()
            m2 = MobRight()
            all_sprites.add(m2)
            mobs.add(m2)

        hits = pygame.sprite.spritecollide(hero, mobs, False, pygame.sprite.collide_circle_ratio(0.9))
        if hits:
            running = False
        screen.blit(bg, (0, 0))

        hero.update(left, right, up, platforms)  # передвижение

        camera.update(hero)  # центризируем камеру относительно персонажа
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        for e in all_sprites:
            e.update()
            screen.blit(e.image, camera.apply(e))

        draw_text(screen, str(score), 30, WIDTH - 40, 10)
        pygame.display.update()


if __name__ == "__main__":
    main()
