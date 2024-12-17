import pygame
import random
from skin import  *


def start_game():
    global missed_enemies
    class Gamesprite(pygame.sprite.Sprite):
        def __init__(self, player_image, player_x,player_y,size_x,size_y,player_speed):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(player_image),(size_x, size_y))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class Player(Gamesprite):
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.x < width-80:
                self.rect.x += self.speed

        def draw(self, window):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class Enemmi(Gamesprite):
        def update(self):
            global missed_enemies
            self.rect.y += self.speed
            if self.rect.y > 500:
                self.rect.y = 5
                self.rect.x = random.randint(0,600)
                missed_enemies += 1
                reheuf = read_from_file()
                reheuf['кількість монет'] += 1
                write_in_file(reheuf)


        def draw(self, window):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class Bullettt(Gamesprite):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()

        def draw(self, window):
            window.blit(self.image, (self.rect.x, self.rect.y))

    ###### ДЗ заходе улітка в бар і каже...

    reheuf = read_from_file()
    pygame.init()

    width = 700
    height = 500

    fps = pygame.time.Clock()
    enemies = []
    enemies.append(Enemmi("asteroid.png", 110,height-500,80,100,2))
    enemies.append(Enemmi("ufo.png", random.randint(0, 600), 100, 50, 50, 2))

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Shooter")

    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, [700, 500])
    ship = Player(reheuf['скін'], 5,height-100,80,100,20)
    bullets = []

    pygame.mixer.init()
    pygame.mixer.music.load("space.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    fire = pygame.mixer.Sound('fire.ogg')
    i = 0
    missed_enemies = 0

    run = True
    finish = False

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
                return
            if e.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(Bullettt("bullet.png", ship.rect.x, ship.rect.y, 30, 50, 8))
                fire.play()

        if not finish:
            missed_enemies_text = pygame.font.Font(None, 35).render('Пропущені:' + str(missed_enemies), True, [255, 255, 255])
            i_enemies_text = pygame.font.Font(None, 35).render('Вбито:' + str(i), True,[255, 255, 255])

            for enemy in enemies:
                enemy.update()
            for enemy in enemies:
                if enemy.rect.colliderect(ship.rect):
                    run = False
            for enemy in enemies:
                for bullet in bullets:
                    if enemy.rect.colliderect(bullet.rect):
                        bullet.kill()
                        bullets.remove(bullet)
                        enemy.rect.y = 5
                        enemy.rect.x = random.randint(0,600)
                        i = i + 1
                        reheuf = read_from_file()
                        reheuf['кількість монет'] += 1
                        write_in_file(reheuf)
                        break



            ship.update()
            window.blit(background, (0, 0))
            window.blit(missed_enemies_text, [0, 0])
            window.blit(i_enemies_text, [0, 35])
            ship.draw(window)
            for bullet in bullets:
                bullet.reset()
                bullet.update()
            for enemy in enemies:
                enemy.reset()

        pygame.display.flip()
        fps.tick(60)
