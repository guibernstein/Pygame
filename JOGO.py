import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

largura_zumbi = 100
altura_zumbi = 100
font = pygame.font.SysFont('Comic Sans', 48)
background = pygame.image.load('fundo.png').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (largura_zumbi,altura_zumbi))

class Zumbi(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 900)
        self.rect.y = 500
        self.speedx = 0.3
        self.speedy = 6
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - largura_zumbi)
            self.rect.y = 500

game = True
clock = pygame.time.Clock()
FPS = 30

zumbis = pygame.sprite.Group()
for i in range(3):
    zumbi = Zumbi(zumbi_img)
    zumbis.add(zumbi)

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    zumbis.update() 

    window.blit(background, (0, 0))
    zumbis.draw(window)

    pygame.display.update()

pygame.quit()