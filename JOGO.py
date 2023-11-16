import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

largura_zumbi = 50
altura_zumbi = 50
font = pygame.font.SysFont('Comic Sans', 48)
background = pygame.image.load('fundo.png').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
zumbi = pygame.image.load('zumbi.png').convert_alpha()
zumbi = pygame.transform.scale(zumbi, (largura_zumbi,altura_zumbi))

game = True
zumbi_x = 500
zumbi_y = 500
zumbi_speedx = 0.2
zumbi_speedy = 0.2

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    zumbi_x += zumbi_speedx
    zumbi_y += zumbi_speedy

    window.blit(background, (0, 0))
    window.blit(zumbi, (zumbi_x,zumbi_y))
    pygame.display.update()

pygame.quit()