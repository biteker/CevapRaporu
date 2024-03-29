class Person(object):
    def __init__(self, userId, soru, cevap):
        self._userId = userId
        self._soru = soru
        self._cevap = cevap

    @property
    def userId(self):
        return self._userId

    @property
    def soru(self):
        return self._soru

    @property
    def cevap(self):
        return self._cevap

    def __str__(self):
        return "Kullanıcı:%s Soru:%s Cevap:%s" % (self._userId,self._soru,self._cevap)


liste = []

ogrenci = Person(1, 2, 3)  # ogrenci blgilerini girmek icin 1. yol
liste.append(ogrenci)
ogrenci=Person(4,5,6)
liste.append(ogrenci)

print(liste[1].userId)

#print(*liste, sep="\n")