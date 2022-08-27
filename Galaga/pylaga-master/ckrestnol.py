import pygame
 
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
radius = 20
 
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 4:
                radius += 1 
            if i.button == 5:
                radius -= 1
            if i.button == 1:
                pygame.draw.circle(sc, RED, i.pos, radius)
                pygame.display.update()
            elif i.button == 3:
                pygame.draw.circle(sc, BLUE, i.pos, radius)
                pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20, 20))
                pygame.display.update()
            elif i.button == 2:
                sc.fill(WHITE)
                pygame.display.update()
 
    pygame.time.delay(20)