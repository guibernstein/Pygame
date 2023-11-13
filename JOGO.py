import pygame

pygame.init()

window = pygame.display.set_mode((500,400))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False