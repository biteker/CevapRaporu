#!/usr/bin/env python3

# FIXME: requirements.txt
# pip3 install python-telegram-bot --upgrade

from telegram.ext import Updater
from telegram.ext import CommandHandler

import os
import time

#os.environ['TOKEN']='buraya api gelecek'

token = os.getenv('TOKEN')
if not token:
    print("You need to export TOKEN=YOURTELEGRAMTOKEN")
    exit()

updater = Updater(token=token)
dispatcher = updater.dispatcher

dosyaAdi = 1
kanalID=os.getenv('kanalID')  #kanalID="-100324324"

cevaplarToplu=[[0 for y in range(5)] for x in range(20)]
kisi =[]
cevapRapor=[]
katilimciListesi=[]
katilimciListesi1=[]
mesajID=1000
mesajID2=1000

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
    bot.send_message(chat_id=update.message.chat_id, text="Merhaba")

def kisiSoruyaCevapVerdiMi(kullanciID,soru):
    for i in range(len(cevapRapor)):
        if (kullanciID == cevapRapor[i][0]) and (soru == str(cevapRapor[i][1])):
            return True
    return False

def cevap(bot, update):
    if(str(update.message.chat_id)==kanalID):
        cevaplar1=update.message.text
        cevaplar=cevaplar1.split()
        kisi=[str(update.message.from_user.id), int(cevaplar[1])-1, harfCevir(cevaplar[2]), str(update.message.from_user.first_name), str(update.message.from_user.last_name)]
        if kisiSoruyaCevapVerdiMi(kisi[0], str(kisi[1]))==False:
            cevaplarToplu[int(cevaplar[1])-1][harfCevir(cevaplar[2])]+=1
            cevapRapor.append(kisi)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=str(update.message.from_user.first_name) + " bu soruya daha once cevap verdiniz.")
        #bot.send_message(chat_id=update.message.chat_id, text=str(update.message.from_user.first_name) + " soru:" + cevaplar[1] + " cevap:" + cevaplar[2])
    else:
        bot.send_message(chat_id=update.message.chat_id, text= "%s : Ozelden komut gonderemezsiniz" % update.message.chat_id)

def sil(bot,update):
    if(str(update.message.chat_id)==kanalID):
        cevaplar1=update.message.text
        cevaplar=cevaplar1.split()
        kisi=[str(update.message.from_user.id), int(cevaplar[1])-1, harfCevir(cevaplar[2]), str(update.message.from_user.first_name), str(update.message.from_user.last_name)]
        if kisi in cevapRapor:
            cevaplarToplu[int(cevaplar[1])-1][harfCevir(cevaplar[2])]-=1
            bot.send_message(chat_id=update.message.chat_id, text=str(update.message.from_user.first_name) + " SILINDI soru:" + cevaplar[1] + " cevap:" + cevaplar[2])    
            cevapRapor.remove(kisi)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=str(update.message.from_user.first_name) + " daha once bu soruya cevap vermediniz veya baska bir yanita cevap verdiniz.")    
    else:
        bot.send_message(chat_id=update.message.chat_id, text= "%s : Ozelden komut gonderemezsiniz" % update.message.chat_id)

def cevaplar(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=cevapGoster())
    bot.send_message(chat_id=kanalID, text=cevapGoster())


def k(bot, update):
    bot.send_message(chat_id=kanalID, text=update.message.text[3:])

def sifirla(bot,update):
    cevapRapor.clear()
    for i in range(len(cevaplarToplu)):
        for j in range(len(cevaplarToplu[i])):
            cevaplarToplu[i][j]=0
    bot.send_message(chat_id=update.message.chat_id, text="sifirlandi")

def katilanlaraEkle():
    for i in range(len(cevapRapor)):
        if any(cevapRapor[i][0] in sublist for sublist in katilimciListesi)==False:
            katilimciListesi1=[cevapRapor[i][0],1,cevapRapor[i][3],cevapRapor[i][4]]
            katilimciListesi.append(katilimciListesi1)
        else:
            for j in range(len(katilimciListesi)):
                if (cevapRapor[i][0] in katilimciListesi[j])==True:
                    katilimciListesi[j][1]+=1

def katilanlar(bot, update):
    katilimciListesi.clear()
    katilanlaraEkle()
    mesaj="Katılanların Soru cevaplama Sayilari"
    mesaj+="\n" 
    for i in range(len(katilimciListesi)):
        mesaj+=katilimciListesi[i][2]
        mesaj+=" "
        mesaj+=katilimciListesi[i][3]
        mesaj+=" : "
        mesaj+=str(katilimciListesi[i][1])
        mesaj+="\n"  
    bot.send_message(chat_id=update.message.chat_id, text=mesaj)

def baslat(bot, update):
    global mesajID
    mesajID=update.message.message_id
    bot.send_message(chat_id=update.message.chat_id, text="Basladi")

def bitir(bot, update):
    global mesajID2
    mesajID2=update.message.message_id
    bot.send_message(chat_id=update.message.chat_id, text="bitti")

def gecmisiSil(bot,update):
    son=mesajID2 + 2
    for i in range(mesajID, son):
        try:
            bot.delete_message(chat_id=kanalID, message_id=i)
        except:
            print("hata")
    print("silindi")

def kanaldanAyril(bot, update):
    bot.leave_chat(chat_id=kanalID)

def kanalid(bot,update):
    global kanalID
    if (update.message.text[9:]=="reset"):
        kanalID = os.getenv('kanalID')
    else:
        kanalID=update.message.text[9:]

start_handler = CommandHandler('kanalid', kanalid)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('kanaldanayril', kanaldanAyril)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

capture_handler = CommandHandler('cevap', cevap)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('sil', sil)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('yanitlar', cevaplar)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('k', k)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('sifirla', sifirla)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('gecmisisil', gecmisiSil)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('baslat', baslat)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('bitir', bitir)
dispatcher.add_handler(capture_handler)

capture_handler = CommandHandler('katilanlar', katilanlar)
dispatcher.add_handler(capture_handler)

print("Running bot now.")
updater.start_polling()
