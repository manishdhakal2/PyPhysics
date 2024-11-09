import pygame


pygame.init()

win=pygame.display.set_mode((800,800))

class Circle:
    def __init__(self,win,color,radius,width):
        self.win=win
        self.c=color
        self.r=radius
        self.w=width
    
    def place(self,x,y):
        pygame.draw.circle(self.win,self.c,(x,y),self.r,self.w)
    
no_of_balls=10
a,u=9.8,0
Sx,Sy=[i for i in range(50,50*(no_of_balls+1),50)],0
t=0.001

circle=Circle(win,(255,255,255),6.0,0)
circles=[circle for i in range(no_of_balls)]

running=True
while running:
    pygame.time.delay(10)
    win.fill((0,0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running=False
    if(Sy<795):
        Sy=u*t+0.5*a*t*t
        t+=0.001
        u=u+a*t

    for i in range(0,no_of_balls):
        circles[i].place(Sx[i],Sy)
    pygame.display.flip()

pygame.quit()