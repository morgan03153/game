import os, time, random
import pygame

pygame.init()
clock = pygame.time.Clock()
disp_w = 600
disp_h = 600
gameDisplay = pygame.display.set_mode((disp_w,disp_h))
white = (40,40,40)

run_idx = ['008','009','010','011','012','013']

img = []
for idx in run_idx:
    pic_file = 'run_'+str(idx)+'.png'
    img_i = pygame.image.load(pic_file)
    img.append(img_i)

i = 0
run = 1
while run == 1:
    gameDisplay.fill(white)
    if i == len(run_idx):
        i = 0
    img_get = img[i]
    gameDisplay.blit(img_get,(20,20))
    i = i + 1
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
