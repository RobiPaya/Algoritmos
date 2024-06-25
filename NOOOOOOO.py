import pygame, sys
import random
pygame.init()
pygame.display.set_caption('cuadrado inservible')
size = (800,500)
screen=pygame.display.set_mode(size)
NO=pygame.time.Clock()
coorx=400
coory=200
speedx=3
speedy=3
#---colores!!!!!!!!!!!!!---
BLACK=(0,0,0)
rojo=(100,0,0)
blanco=(200,200,200)
azul=(0,0,200)
verde=(0,200,0)
colores=[rojo,azul,verde,blanco]
#---no---------------------


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    if (coorx > 720 or coorx < 0):
        speedx*= -1

    if (coory > 400 or coory < 0):
        speedy*= -1

    coorx+=speedx
    coory+=speedy
    
    screen.fill(random.choice(colores))
    #-----DIBUJO----
    pygame.draw.rect(screen, random.choice(colores), (coorx, coory, 80, 80))
    
    #-----FIN-------
    pygame.display.flip()
    NO.tick(70)
