import pygame
import random
from gpohi import  *

def start_gameee():
    global bemon
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
            if keys[pygame.K_RIGHT] and self.rect.x < 1050:
                self.rect.x += self.speed
            if keys[pygame.K_DOWN] and self.rect.y > 5:
                self.rect.y += self.speed
            if keys[pygame.K_UP] and self.rect.y < 600:
                self.rect.y -= self.speed

        def draw(self, window):
            window.blit(self.image, (self.rect.x, self.rect.y))
    class Enemmi(Gamesprite):
        def update(self):
            #global missed_enemies
            self.rect.y += self.speed
            if self.rect.y > 600:
                self.rect.y = 5
                self.rect.x = random.randint(400,1100)
                #missed_enemies += 1
                #reheuf = read_from_file()
                #reheuf['кількість монет'] += 1
                #write_in_file(reheuf)


    xxx = read_from_file()
    pygame.init()
    window = pygame.display.set_mode((1100, 600))
    fps = pygame.time.Clock()
    fon = pygame.image.load("img_8.png")
    pygame.display.set_caption("Killing_spirits!")
    enemii = []
    enemii.append(Enemmi("monster.png", random.randint(0, 600),300,90,100,3))
    enemii.append(Enemmi("bfbrf.png", random.randint(0, 600),300,90,100,3))
    enemii.append(Enemmi("monster.png", random.randint(0, 600),300,90,100,3))
    enemii.append(Enemmi("bfbrf.png", random.randint(0, 600),300,90,100,3))


    pers = Player("pixilartt.png", 10,400,140,190,10)


    demon = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        if not False :
            i_enemies_text = pygame.font.Font(None, 35).render('Вбито:' + str(demon), True, [255, 255, 255])
            pers.update()
            window.blit(fon, (0, 0))
            window.blit(i_enemies_text, [0, 10])
            pers.draw(window)
            for enemy in enemii:
                if enemy.rect.colliderect(pers.rect):
                    enemy.rect.y = 5
                    enemy.rect.x = random.randint(0, 600)
                    demon = demon + 1
                    xxx = read_from_file()
                    xxx['зароблено монеток'] += 1
                    write_in_file(xxx)
                    break

            for enemy in enemii:
                enemy.update()

            for enemy in enemii:
                enemy.reset()


        pygame.display.flip()
        fps.tick(60)
