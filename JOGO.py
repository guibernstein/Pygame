import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

game = True

font = pygame.font.SysFont('Comic Sans', 48)

text = font.render('Deadly Target', True, (0, 0, 255))

largura_zumbi = 10
altura_zumbi = 4

zumbi = pygame.image.load('zumbi.png').convert_alpha()
zumbi = pygame.transform.scale(zumbi, (largura_zumbi,altura_zumbi))



while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(text, (400, 400))
    pygame.display.update()