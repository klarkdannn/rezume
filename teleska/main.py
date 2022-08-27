import pygame
from ball import Ball
from random import randint

pygame.mixer.pre_init(44100, -16, 1, 512) # важно прописать до pygame.init()
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

BLACK = (0, 0, 0)
W, H = 1000, 537

sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

score = pygame.image.load('images/score_fon.png').convert_alpha()
f = pygame.font.SysFont('arial', 30)

telega = pygame.image.load('images/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)

balls_data = ({'path': 'rud1.png', 'score': 100},
              {'path': 'rud2.png', 'score': 150},
              {'path': 'almaz.png', 'score': 200})

balls_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()

balls = pygame.sprite.Group()

bg = pygame.image.load('images/back1.jpg').convert()

speed = 10
createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width

    collideBalls()
    sc.blit(bg, (0, 0))
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))

    balls.draw(sc)
    sc.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)

