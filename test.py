
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
    

cevaplarToplu[19][harfCevir("A")]+=1
cevaplarToplu[19][harfCevir("A")]+=1
cevaplarToplu[19][harfCevir("b")]+=1

def cevapGoster():
    mesaj=""
    for i in range(len(cevaplarToplu)):
        mesaj+="%s) " % int(i+1)
        for j in range(len(cevaplarToplu[i])):
            if (cevaplarToplu[i][j]>0):
                mesaj+="%s(%s) " % (sayiCevir(j),cevaplarToplu[i][j])
        mesaj+="\n"
    return mesaj

print(cevapGoster())
#print(cevaplarToplu)
