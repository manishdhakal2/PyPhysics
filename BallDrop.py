import pygame

pygame.init()

win=pygame.display.set_mode((800,800))

a,u=9.8,0
Sx,Sy=300,0
t=0.001

running=True
while running:
    pygame.time.delay(10)
    win.fill((0,0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running=False
    Sy=u*t+0.5*a*t*t
    t+=0.001
    u=u+a*t

    pygame.draw.circle(win,(255,255,255),(Sx,Sy),15.0,0)
    pygame.display.flip()

pygame.quit()