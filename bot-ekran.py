#!/usr/bin/env python3

# FIXME: requirements.txt
# pip3 install python-telegram-bot --upgrade
# pip3 install pyscreenshot
# pip3 install pillow
# pip3 install pynput

from telegram.ext import Updater
from telegram.ext import CommandHandler

import pyscreenshot as ImageGrab
import os
import time

from pdf import pdfYap
from pynput import keyboard

os.environ['TOKEN']='buraya api key girilecek' 

token = os.getenv('TOKEN')
if not token:
    print("You need to export TOKEN=YOURTELEGRAMTOKEN")
    exit()

updater = Updater(token=token)
dispatcher = updater.dispatcher

dosyaAdi = 1
kanalID="buraya kanal id" #kanalID="-213542313"



def ekranYakala():
    im = ImageGrab.grab(bbox =(0, 100, 1430, 850))
    tZaman = time.localtime()
    dosyaAdi = time.strftime("%Y%M%d%H%m%S.png", tZaman)
    im.save(dosyaAdi, "PNG")
    print("Sending...")
    return dosyaAdi

def mesajYolla():
    dosyaAdi=ekranYakala()
    updater.bot.send_photo(chat_id=kanalID, photo=open(dosyaAdi, 'rb'))

def pdfYolla():
    dosyaAdi=pdfYap()
    str(dosyaAdi)
    updater.bot.send_document(chat_id=kanalID, document=open(dosyaAdi,'rb'))

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #capture(bot,update)
        mesajYolla()
        print('Key pressed: ' + k)
        #return False  # stop listener; remove this if want more keys
    if k in ['3']:
        pdfYolla()
        print('Key pressed: ' + k)


print("Running bot now.")
updater.start_polling()

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
