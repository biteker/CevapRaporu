#!/usr/bin/env python3

# FIXME: requirements.txt
# pip3 install python-telegram-bot --upgrade
# pip3 install pyscreenshot
# pip3 install pillow

from telegram.ext import Updater
from telegram.ext import CommandHandler

import pyscreenshot as ImageGrab
import os
import time

os.environ['TOKEN']='1142979898:AAEGJvOstfYNHLKMPYaclsIOx3YsHzjOUPw' #bilirkisi

#os.environ['TOKEN']='980552993:AAH5DPFby37PpE8mhxpP6E_aUtKsj1OCgOA' #malumat
token = os.getenv('TOKEN')
if not token:
    print("You need to export TOKEN=YOURTELEGRAMTOKEN")
    exit()

updater = Updater(token=token)
dispatcher = updater.dispatcher

dosyaAdi = 1
kanalID="-1001144169699"

cevaplarToplu=[[0 for y in range(5)] for x in range(20)]

def harfCevir(harf):
    if(harf=="a" or harf=="A"):
        return 0
    if(harf=="b" or harf=="B"):
        return 1
    if(harf=="c" or harf=="C"):
        return 2
    if(harf=="d" or harf=="D"):
        return 3
    if(harf=="e" or harf=="E"):
        return 4
    
def sayiCevir(sayi):
    if (sayi==0):
        return "A"
    if (sayi==1):
        return "B"
    if (sayi==2):
        return "C"
    if (sayi==3):
        return "D"
    if (sayi==4):
        return "E"
    
def cevapGoster():
    mesaj=""
    for i in range(len(cevaplarToplu)):
        mesaj+="%s) " % int(i+1)
        for j in range(len(cevaplarToplu[i])):
            if (cevaplarToplu[i][j]>0):
                mesaj+="%s(%s) " % (sayiCevir(j),cevaplarToplu[i][j])
        mesaj+="\n"
    return mesaj

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="'/cevap Soru cevap seklinde cevabi bildirin. Ornek: /cevap 5-a")

def cevap(bot, update):
    if(str(update.message.chat_id)==kanalID):
        cevaplar1=update.message.text
        cevaplar=cevaplar1.split()
        cevaplarToplu[int(cevaplar[1])-1][harfCevir(cevaplar[2])]+=1
        #bot.send_message(chat_id=update.message.chat_id, text="soru:" + cevaplar[1] + " cevap:" + cevaplar[2])
    else:
        bot.send_message(chat_id=update.message.chat_id, text= "%s : Ozelden komut gonderemezsiniz" % update.message.chat_id)

def sil(bot,update):
    if(str(update.message.chat_id)==kanalID):
        cevaplar1=update.message.text
        cevaplar=cevaplar1.split()
        if(cevaplarToplu[int(cevaplar[1])-1][harfCevir(cevaplar[2])]>0):
            cevaplarToplu[int(cevaplar[1])-1][harfCevir(cevaplar[2])]-=1
        bot.send_message(chat_id=update.message.chat_id, text="SILINDI soru:" + cevaplar[1] + " cevap:" + cevaplar[2])    
    else:
        bot.send_message(chat_id=update.message.chat_id, text= "%s : Ozelden komut gonderemezsiniz" % update.message.chat_id)

def cevaplar(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=cevapGoster())

def k(bot, update):
    bot.send_message(chat_id=kanalID, text=update.message.text[3:])

def sifirla(bot,update):
    for i in range(len(cevaplarToplu)):
        for j in range(len(cevaplarToplu[i])):
            cevaplarToplu[i][j]=0
    bot.send_message(chat_id=update.message.chat_id, text="sifirlandi")
       

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

capture_handler = CommandHandler('cevap', cevap)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('sil', sil)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('cevaplar', cevaplar)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('k', k)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('sifirla', sifirla)
dispatcher.add_handler(capture_handler)

print("Running bot now.")
updater.start_polling()