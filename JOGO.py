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

class zumbi(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 900)
        self.rect.y = 600
        self.speedx = 0.05
        self.speedy = 1
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - largura_zumbi)
            self.rect.y = 600

game = True
clock = pygame.time.Clock()
FPS = 110

zumbi1 = zumbi(zumbi_img)
zumbi2 = zumbi(zumbi_img)

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    zumbi1.update()
    zumbi2.update()

    window.blit(background, (0, 0))
    window.blit(zumbi1.image, zumbi1.rect)
    window.blit(zumbi2.image, zumbi2.rect)

    pygame.display.update()

pygame.quit()