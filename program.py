#pip3 install pygame
#pip install pygame     -> So we can use it on every python-version
#same for flask 
import os 
import pygame 
import time
from time import sleep
import flask
from flask import redirect
import multiprocessing

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

actual = 0
plN = 0
a = 0

musicDir = '/test/'
os.chdir(musicDir)
playlist = os.listdir()

print (playlist)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(playlist[actual])

for numbers in playlist:
    plN += 1
print(plN)

@app.route('/', methods=['GET'])
def home():
    return '<a href="play">->Play</a> <br> <a href="pause">->Pause</a> <br> <a href="resume">->Resume</a> <br> <a href="next">->Next</a> <br> <a href="back">->Back</a> <br> <a href="stop">->Stop</a>'

@app.route('/play', methods=['GET'])
def play():
    pygame.mixer.music.play()
    print('Play')
    return redirect("/")    #"<h1>Start Playing now</p>"

@app.route('/resume', methods=['GET'])
def resume():
    pygame.mixer.music.unpause()
    print('Resume')
    return redirect("/")

@app.route('/pause', methods=['GET'])
def pause():
    pygame.mixer.music.pause()
    return redirect("/")

@app.route('/next', methods=['GET'])
def next():
    stop()
    global actual
    actual += 1
    if actual >= plN:
        actual = 0
    pygame.mixer.music.load(playlist[actual])
    sleep(1)
    play()
    print('Playing next')
    return redirect("/")

@app.route('/back', methods=['GET'])
def before():
    global actual
    actual -= 1
    pygame.mixer.music.load(playlist[actual])
    stop()
    play()
    print('Going back')
    return redirect("/")

@app.route('/get_state/busy', methods=['GET'])
def busy():
    return str(pygame.mixer.music.get_busy())

@app.route('/stop', methods=['GET'])
def stop():
    pygame.mixer.music.stop()
    return redirect("/")

def API(Conf):
   print('In API selction')
   app.run(host='0.0.0.0')

if __name__ == "__main__":
    config = {"Something":"SomethingElese"}
    p = multiprocessing.Process(target=API, args=(config))
    p.start()
    sleep(3)
    print('After Flask run')
    
