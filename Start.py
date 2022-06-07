import pygame
import random

okno=pygame.display.set_mode(size=(900,600))
clock=pygame.time.Clock()
bok = random.randint(1,8)
a=bok*50
while True:
    for event in pygame.event.get():
        pygame.draw.rect(okno, (0, 255, 0), (0, 0, a, 600))
        pygame.draw.rect(okno, (0, 255, 0), (900-a, 0, 900, 600))
        pygame.display.flip()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
`

pygame.display.update()
clock.tick(15)
