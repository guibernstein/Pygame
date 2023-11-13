import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

game = True

font = pygame.font.SysFont('Comic Sans', 48)
text = font.render('Deadly Target', True, (0, 0, 255))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(text, (400, 400))
    pygame.display.update()