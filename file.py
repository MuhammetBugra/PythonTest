dosya=open("yazilim.txt","w")
dosya.write("asd")
try:
    dosya=open("yazilim.txt","r")
    print(dosya.read())
except FileNotFoundError:
    print("Dosya bulunamadi")

