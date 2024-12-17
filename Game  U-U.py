import pygame

class MainHero:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.hitbox.y += 7
        if keys[pygame.K_d]:
            self.hitbox.x += 7
        if keys[pygame.K_w]:
            self.hitbox.y += -7
        if keys[pygame.K_a]:
            self.hitbox.x += -7



    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

class MainVillain:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.hitbox.y += 7
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += 7
        if keys[pygame.K_UP]:
            self.hitbox.y += -7
        if keys[pygame.K_LEFT]:
            self.hitbox.x += -7

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

pygame.init()

window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, [500, 500])

hero = MainHero(100, 100,"", 50, 50)

villain = MainVillain(150,150, "sprite2.png", 60,60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    hero.movement()
    villain.movement()
    window.fill((138, 178, 201))
    window.blit(background, (0, 0))
    hero.draw(window)
    villain.draw(window)

    pygame.display.flip()
    fps.tick(60)












