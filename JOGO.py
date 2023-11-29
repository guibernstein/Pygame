import pygame
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 800
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

largura_zumbi = 50
altura_zumbi = 50
background = pygame.image.load('fundo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (largura_zumbi,altura_zumbi))
mira_img = pygame.image.load('Mira.png').convert_alpha()
mira_img = pygame.transform.scale(mira_img, (80,80))
score_font = pygame.font.Font('HelpMe.ttf',50)

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.set_volume(0.4)

class Zumbi(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - largura_zumbi) 
        self.rect.y = 450
        self.speedx = -0.4
        self.speedy = 1

        self.tamanho_original = (largura_zumbi, altura_zumbi)
    
    def reset(self):

        self.rect.x = random.randint(0, WIDTH - 2*largura_zumbi)
        self.rect.y = 450
    
    def update(self):

        tamanho_aumento = self.rect.y / 3
        novo_tamanho = (int(self.tamanho_original[0] + tamanho_aumento), int(self.tamanho_original[1] + tamanho_aumento))
        self.image = pygame.transform.scale(zumbi_img, novo_tamanho)
        self.rect.x += self.speedx
        self.rect.y += self.speedy


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

score = 0
zumbi_added = False

pygame.mixer.music.play(loops=-1)

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for zumbi in all_zumbis:
                area_colisao_ampliada = zumbi.rect.inflate(100, 100)
                if area_colisao_ampliada.collidepoint(pygame.mouse.get_pos()):
                    zumbi.reset()
                    score += 100
    

    if score != 0 and score % 2000 == 0 and not zumbi_added:
        novo_zumbi = Zumbi(zumbi_img)
        all_sprites.add(novo_zumbi)
        all_zumbis.add(novo_zumbi)
        zumbi_added = True

        nova_mira = Mira(mira_img)
        all_sprites.add(nova_mira)

    if score % 2000 != 0:
        zumbi_added = False

    all_sprites.update()

    for zumbi in all_zumbis:
        if zumbi.rect.bottom >= HEIGHT:
            game = False

    window.blit(background, (0, 0))
    all_sprites.draw(window)

    text_surface = score_font.render("SCORE:{:06d}".format(score), True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()