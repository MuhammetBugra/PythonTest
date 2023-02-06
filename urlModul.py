import urllib.request
url1="https://upload.wikimedia.org/wikipedia/tr/4/4e/Gazi_%C3%9Cniversitesi_logo.png"
urlListesi=[url1]
sayi=1
for url in urlListesi:
    urllib.request.urlretrieve(url,"Resim"+str(sayi)+".jpg")
    sayi+=1
