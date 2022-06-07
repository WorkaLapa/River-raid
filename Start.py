import pygame
import random

okno=pygame.display.set_mode(size=(900,600))
clock=pygame.time.Clock()
bok = 50*(random.randint(1,8))
while True:
    for event in pygame.event.get():
        pygame.draw.rect(okno, (0, 255, 0), (0, 0, bok, 600))
        pygame.draw.rect(okno, (0, 255, 0), (900-bok, 0, 900, 600))
        pygame.display.flip()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
`

pygame.display.update()
clock.tick(15)
