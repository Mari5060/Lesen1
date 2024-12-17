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
            self.hitbox.y += 5
        if keys[pygame.K_d]:
            self.hitbox.x += 5
        if keys[pygame.K_w]:
            self.hitbox.y += -5
        if keys[pygame.K_a]:
            self.hitbox.x += -5



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

class Vol:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

class Trophy:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

class Win:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

pygame.init()

window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

background = pygame.image.load("img_4.png")
background = pygame.transform.scale(background, [500, 500])

hero = MainHero(90, 350,"pixilart-drawing (1).png", 50, 50)
trophy = Trophy(390, 60,"fdsfds.png", 60, 60)

villain = MainVillain(350,250, "pixilart-drawing (3).png", 50,50)
vool = [  ]
vool.append(Vol(50,50, "img_5.png", 10,350))
vool.append(Vol(50,50, "img_5.png", 350,10))
vool.append(Vol(150,130, "img_5.png", 10,270))
vool.append(Vol(150,130, "img_5.png", 70,10))
vool.append(Vol(210,130, "img_5.png", 10,270))
vool.append(Vol(300,50, "img_5.png", 10,260))
vool.append(Vol(210,390, "img_5.png", 200,10))
vool.append(Vol(400,130, "img_5.png", 10,270))

win_ = Win(0,0, "pixilart-drtvytrvhrt.png", 500,500)

pygame.mixer.init()
pygame.mixer.music.load("golub-vorkuet-nochyu-v-lesu.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

kick_ = pygame.mixer.Sound("kick.ogg")
zvon = pygame.mixer.Sound("vnushayuschiy-zvon-dostannogo-starinnogo-mecha.ogg")
styk = pygame.mixer.Sound("gluhoy-stuk-v-dver.ogg")
zvon.set_volume(0.2)
styk.set_volume(0.8)

stan = "Шукаєм меч"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if stan == "Шукаєм меч":

        hero.movement()
        villain.movement()

        for element in vool:
            if hero.hitbox.colliderect(element.hitbox):
                hero.hitbox.x=90
                hero.hitbox.y=350
                styk.play()

        if hero.hitbox.colliderect(villain.hitbox):
            hero.hitbox.x=90
            hero.hitbox.y=350
            kick_.play()

        if hero.hitbox.colliderect(trophy.hitbox):
            zvon.play()


        window.fill((138, 178, 201))
        window.blit(background, (0, 0))
        hero.draw(window)
        villain.draw(window)
        trophy.draw(window)
        for element in vool:
            element.draw(window)
        if hero.hitbox.colliderect(trophy.hitbox):
            stan = "Взяли Меч"
            hero.hitbox.x=410
    if stan == "Взяли Меч":
        win_.draw(window)



    pygame.display.flip()
    fps.tick(60)