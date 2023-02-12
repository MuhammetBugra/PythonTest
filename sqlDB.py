import sqlite3
import time
import datetime
import random

con = sqlite3.connect("dersler.db")
cursor=con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, numara INT, zaman REAL)")

def degerEkle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO ogrenciler(ad,numara,zaman) VALUES('Bugra',?,?)",(deger,tarih))
    con.commit()

def degerlerial():
    cursor.execute("SELECT * FROM ogrenciler WHERE ad='Bugra'")
    data=cursor.fetchall()
    for i in data:
        print(i)

def degerGuncelle():
    cursor.execute("SELECT * FROM ogrenciler")
    print("Ilk degerler  ")
    data=cursor.fetchall()
    for i in data:
        print(i)
    cursor.execute("UPDATE ogrenciler SET ad='Ahmet' WHERE ad='Bugra'")
    cursor.execute("SELECT * FROM ogrenciler")
    print("Son degerler  ")
    data=cursor.fetchall()
    for i in data:
        print(i)

#degerGuncelle()
#tabloOlustur()
#i=0
#while(i<10):
#    degerEkle()
#    time.sleep(1)
#    i+=1
con.close()