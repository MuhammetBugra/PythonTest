class Dusman:
    kalanCan=3
    def saldir(self):
        print("Hucum")
        self.kalanCan-=1

    def hayattaMi(self):
        if(self.kalanCan<1):
            print("Oldu")
        else:
            print("Hayatta "+str(self.kalanCan)+" can kaldi")

dusman1=Dusman()
dusman2=Dusman()
dusman1.saldir()
dusman1.hayattaMi()

