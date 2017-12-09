import os, time, random
import pygame

pygame.init()
clock = pygame.time.Clock()
disp_w = 1000
disp_h = 600
gameDisplay = pygame.display.set_mode((disp_w,disp_h))
white = (40,40,40)

run_idx = ['008','009','010','011','012','013']

wall = pygame.image.load("wall.png")
wall_inv = pygame.transform.flip(wall,False,True)

def full_wall():
    gameDisplay.blit(wall,(0,310))
    gameDisplay.blit(wall,(500,310))
    gameDisplay.blit(wall_inv,(0,50))
    gameDisplay.blit(wall_inv,(500,50))    

img = []
for idx in run_idx:
    pic_file = 'run_'+str(idx)+'.png'
    img_i = pygame.image.load(pic_file)
    img.append(img_i)

i = 0
done = 0
x = 20
y = 310
x_inc = 3
left = 0
while done != 1:
    gameDisplay.fill(white)
    keys = pygame.key.get_pressed()
    pygame.event.get() # this line is must to have following get_pressed
    if keys[pygame.K_RIGHT]:
        i = i + 1
        x = x + x_inc
        left = 0
        #print("i=",i,"\n")
    elif keys[pygame.K_LEFT]:
        i = i - 1
        x = x - x_inc
        left = 1
    elif keys[pygame.K_ESCAPE]:
        done = 1
    if i == len(run_idx):
       i = 0
    elif i < 0:
       i = len(run_idx) - 1
    
    img_get = img[i]
    if left == 1:
        img_get = pygame.transform.flip(img_get,True,False)
    full_wall()
    gameDisplay.blit(img_get,(x,310))
    pygame.display.flip()
    clock.tick(32)

pygame.quit()
