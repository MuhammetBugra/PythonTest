class Dusman:
    
    def __init__(self,isim,kalanCan,saldiriGucu,mermiSayisi):
        self.isim=isim
        self.kalanCan= kalanCan
        self.saldiriGucu= saldiriGucu
        self.mermiSayisi= mermiSayisi
    
    def print(self):
        print("Basliyor")
        print("Isim: ",self.isim,"Kalan Can: ",self.kalanCan,"Saldiri Gucu: ",self.saldiriGucu,"Mermi Sayisi: ",self.mermiSayisi)

dusman1=Dusman("Ali",2000,50,40)
dusman2=Dusman("Veli",1500,100,50)
dusman1.print()
dusman2.print()
