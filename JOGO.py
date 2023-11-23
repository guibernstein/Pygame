import pygame
import random

pygame.init()

WIDTH = 1200
HEIGHT = 800
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

largura_zumbi = 100
altura_zumbi = 100
font = pygame.font.SysFont('Comic Sans', 48)
background = pygame.image.load('fundo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (largura_zumbi,altura_zumbi))
mira_img = pygame.image.load('Mira.png').convert_alpha()
mira_img = pygame.transform.scale(mira_img, (80,80))

class Zumbi(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 900)
        self.rect.y = 400
        self.speedx = 0.075
        self.speedy = 1.5

        self.tamanho_original = (largura_zumbi, altura_zumbi)
    
    def reset(self):

        self.rect.x = random.randint(100, 900)
        self.rect.y = 400
    
    def update(self):

        tamanho_aumento = self.rect.y / 2
        novo_tamanho = (int(self.tamanho_original[0] + tamanho_aumento), int(self.tamanho_original[1] + tamanho_aumento))
        self.image = pygame.transform.scale(zumbi_img, novo_tamanho)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.reset()

class Mira(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect(center = (WIDTH/2 ,  HEIGHT/2))

    def update(self):

        self.rect.center = pygame.mouse.get_pos()

game = True
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_zumbis = pygame.sprite.Group()
for i in range(3):
    zumbi = Zumbi(zumbi_img)
    all_sprites.add(zumbi)
    all_zumbis.add(zumbi)
mira = Mira(mira_img)
all_sprites.add(mira)

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        # if event.type == pygame.MOUSEBUTTONDOWN:

        if event.type == pygame.QUIT:
            game = False

    all_sprites.update() 

    window.blit(background, (0, 0))
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()