class Calisan:
    
    def __init__(self,isim,maas,departman):
        self.isim=isim
        self.maas= maas
        self.departman= departman
    
    def print(self):
        print("Basliyor")
        print("Isim: ",self.isim,"Maas: ",self.maas,"departman: ",self.departman)

    def maasZam(self,zamMiktari):
        self.maas= zamMiktari

class Calisan1():
    pass

class Yonetici(Calisan,Calisan1):
    
    def __init__(self,isim,maas,departman,kisi):
        super().__init__(isim,maas,departman)
        self.kisi= kisi

yonetici= Yonetici("Ahmet",5000,"aaa",10)


