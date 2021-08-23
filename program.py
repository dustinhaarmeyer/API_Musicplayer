#pip3 install pygame
#pip install pygame     -> So we can use it on every python-version
#same for flask 
import os 
import pygame 
import time
from time import sleep
import flask
from flask import redirect, request
import multiprocessing

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

buttons = [7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]

musicDir = '/test/'     #musicDir button fileType
fileType = '.mp4'   #In der Pygame Dokumentation nach den passenden Dateitypen suchen!!!!

pygame.init()
pygame.mixer.init()

@app.route('/', methods=['GET'])
def home():
    return '<a href="play">->Play</a> <br> <a href="pause">->Pause</a> <br> <a href="resume">->Resume</a> <br> <a href="next">->Next</a> <br> <a href="back">->Back</a> <br> <a href="stop">->Stop</a>'

@app.route('/button/', methods=['GET', 'POST'])  #http://{thisdevice}:5000/button?button={button Number}
def button():
    #pygame.mixer.music.play()
    print('/button called')
    button =str(request.args.get('button'))
    if int(button) in buttons:
        pygame.mixer.music.load(musicDir + button + fileType)
        pygame.mixer.music.play()
        return "Start"
    else:
        return "Error, button not in list"

@app.route('/play', methods=['GET'])
def play():
    pygame.mixer.music.play()
    print('Play')
    return redirect("/")    #"<h1>Start Playing now</p>"

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
    
