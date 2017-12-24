import os, time, random
from gtts import gTTS
#import speech_recognition as sr
import pygame
import string
import numpy
import mafan

test_file = 'test2.txt'

pygame.init()
pygame.mixer.init()

# get audio from the microphone
pp = 'wonder.mp3'
      

tts = gTTS(text="答對了,很棒", lang='zh-tw')
filename = 'correct.mp3'
tts.save(filename)


clock = pygame.time.Clock()
disp_w = 1000
disp_h = 600
f1 = pygame.font.SysFont('simsunnsimsun',60)
gameDisplay = pygame.display.set_mode((disp_w,disp_h))
white = (40,40,40)

run_idx = ['1','2','3','4','5','6']

wall = [pygame.image.load("castle_0.png"), pygame.image.load("castle_2.png"),pygame.image.load("castle_3.png"),\
       pygame.image.load("castle_4.png"), pygame.image.load("castle_5.png"),pygame.image.load("castle_6.png"),\
       pygame.image.load("castle_7.png") 
        ]


def full_wall(x,n):
    #wall_img = "castle_"+str(n)+".png"
    #walli = pygame.image.load(wall_img)
    img_wall = pygame.transform.scale(wall[n],[1200,500])
    gameDisplay.blit(img_wall,(x-100,100))


img = []
princess = []
rect = []
for idx in run_idx:
    pic_file = 'm'+str(idx)+'.png'
    img_i = pygame.image.load(pic_file)
    rect.append(img_i.get_rect())
    img.append(img_i)

princess_num = 25

for idx in range(1,princess_num):
    pic_file = 'p'+str(idx)+'.png'
    princess_i = pygame.image.load(pic_file)
    #rect.append(princess_i.get_rect())
    princess.append(princess_i)    

i = 0
done = 0
x = 250
y = 310
x_inc = 8
y_inc = 8
left = 0
inflat = 0
y_w = 0
y_w_inc = 3
rect_ini = [150,300]


w1_x = numpy.round(disp_w*2/10)
w2_x = numpy.round(disp_w*8/10)

latin = []
with open(test_file,'r') as test_fp:
    for item in test_fp:
        latin.extend(item.split())
        

#latin = ['apple','milk','egg','animal']
#latin = string.ascii_letters+"123456789"
#latin = ['ㄅ','ㄆ','ㄇ','ㄈ','大','小','中','羽','陳']
#latin=['a','b']
print(latin)

listen = 0

w1 = f1.render('',True,(50,250,50))
w2 = f1.render('',True,(50,250,50))
gameDisplay.blit(w1,(10,50))
gameDisplay.blit(w2,(10,200))
cnt = 0
score = 0

while done != 1:   
    target_list = []
    if y_w == 0:
        cnt = cnt + 1
 
        w1 = f1.render('',True,(0,250,50))
        w2 = f1.render('',True,(0,250,50))    

        w1_r =random.choice(latin)
        w2_r =random.choice(latin)
        while w1_r == w2_r:
            w2_r =random.choice(latin)
        target = w1_r

        if mafan.text.contains_latin(target):
            tts = gTTS(text=target, lang='en')
        else:
            tts = gTTS(text=target, lang='zh-tw')
        print("target:",target,"\n")    
        filename = "target.mp3"
        tts.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.load("correct.mp3")
        #while pygame.mixer.music.get_busy():
        #    clock.tick(30)
        #    os.system('rm -f target.mp3')
        #pygame.mixer.music.stop()
        #pygame.mixer.quit()
        
        w1 = f1.render(w1_r,True,(50,250,50))
        w2 = f1.render(w2_r,True,(50,250,50))
        

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
    elif keys[pygame.K_UP]:
        i = i + 1
        y = y - y_inc
    elif keys[pygame.K_DOWN]:
        i = i + 1
        y = y + y_inc
    elif keys[pygame.K_s]:
        inflat = 1
    elif keys[pygame.K_b]:
        inflat = 2
    elif keys[pygame.K_a]:
        listen = 1        
    elif keys[pygame.K_ESCAPE]:
        done = 1
    if x > disp_w :
        x = 0
    elif x < 0:
        x = disp_w
    if i == len(run_idx):
       i = 0
    elif i < 0:
       i = len(run_idx) - 1
    
    img_get = img[i]
    if left == 1:
        img_get = pygame.transform.flip(img_get,True,False)
    rect_get = rect[i]



    img_get = pygame.transform.scale(img_get,[75,150])
    
    if inflat == 1:
        #pygame.mixer.music.load("small.mp3")
        #pygame.mixer.music.play()
        #time.sleep(4)
        img_get = pygame.transform.scale(img_get,[75,150])
        inflat = 0
    elif inflat == 2:
        #pygame.mixer.music.load("big.mp3")
        #pygame.mixer.music.play()
        #time.sleep(4)
        img_get = pygame.transform.scale(img_get,[250,400])
        inflat = 0
    #if score < 20:
    #    wall_num = 0
    #elif score < 60:
    #    wall_num = 1
    #else:    
    #    wall_num = 2
    wall_num = numpy.round(score/50)
    if wall_num > 7:
        wall_num = 7
    full_wall(numpy.round((500-x)/10),numpy.int_(wall_num))
    y_w = y_w + y_w_inc
    w1_y = y_w
    w2_y = y_w
    dist_w1 = (x-w1_x)*(x-w1_x)+(y-w1_y)*(y-w1_y)
    #dist_w2 = (array_p-array_w2)**2
    if dist_w1 < 2000:
        score = score + 10
        y_w = -y_w_inc
        #inflat = 2
        pygame.mixer.music.load("correct.mp3")
        pygame.mixer.music.play()
        time.sleep(4)
        #if score > 20:
        #   gameDisplay.blit(princess[0],(500,300))    
    if y_w > numpy.round(disp_h*99/100):
        y_w =  -y_w_inc
    if y_w == 0:    
        w1_x = random.randrange(10,numpy.round(disp_w*9/10))
        w2_x = numpy.mod(w1_x + numpy.round(disp_w*0.5),disp_w)   
    #print("w1:",w1_x," ",w1_y,"\n")
    #print("w2:",w2_x," ",w2_y,"\n")
    #input(">>")
    w3 = f1.render(str(score),True,(20,20,250))


    princess_idx = numpy.int_(numpy.round(score/20)) 
    
    if princess_idx >= 0 and princess_idx < princess_num:
       #print(princess_idx) 
       gameDisplay.blit(princess[princess_idx],(10,10))
         
    gameDisplay.blit(w3,(500,30))
    gameDisplay.blit(img_get,(x,y))
    if y_w > 0:
        gameDisplay.blit(w1,(w1_x,w1_y))
        gameDisplay.blit(w2,(w2_x,w2_y))
    array_p = numpy.array((x,y))
    array_w1 = numpy.array((w1_x,w1_y))
    array_w2 = numpy.array((w2_x,w2_y))

    
    pygame.display.flip()
    clock.tick(32)

pygame.quit()

print("w1:",w1_x," ",w1_y,"\n")
print("w2:",w2_x," ",w2_y,"\n")
print("p:",x," ",y,"\n")
print("distance:",dist_w1,"\n")




