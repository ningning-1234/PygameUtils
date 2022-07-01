import pygame

run=True

pygame.init()
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

BG_COLOR = pygame.color.Color('0x505050')

while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #_____Draw_____
    window.fill(BG_COLOR)

    pygame.display.flip()
    clock.tick(FPS)
