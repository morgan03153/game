
import os
import time
import random
import pygame
from gtts import gTTS
import speech_recognition as sr

pygame.mixer.init()

# get audio from the microphone
os.system("rm -f *.mp3")
tts = gTTS(text="My name is Elsa", lang='en')
filename = 'myname.mp3'
tts.save(filename)
tts = gTTS(text="I am good", lang='en')
filename = 'good.mp3'
tts.save(filename)


while 1:
    
    r = sr.Recognizer()
    os.system("rm -f recog.mp3")
    kk=input("?")
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        tt = r.recognize_google(audio)
        ok = 1
    except:
        ok = 0

    if ok == 1:
        #cnt = cnt + 1
        if "what's" in tt:
            pygame.mixer.music.load("myname.mp3")
            pygame.mixer.music.play()
            time.sleep(4)
        elif "how are you" in tt:
            pygame.mixer.music.load("good.mp3")
            pygame.mixer.music.play()
            time.sleep(4)            
        else:    
            tts = gTTS(text=tt, lang='en')
            filename = 'recog.mp3'
            print(tt,'\n')
            tts.save(filename)
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            time.sleep(4)
    else:
        print("say again \n")    
pygame.quit()
