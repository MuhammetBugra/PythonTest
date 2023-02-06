sayi1=input("Sayi1: ")
sayi2=input("Sayi2: ")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)
except ValueError:
    print("Lutfen 10'luk tabanda sayi girin")
except ZeroDivisionError:
    print("Sayi 0'a bolunemez")
finally:
    print("asd")


