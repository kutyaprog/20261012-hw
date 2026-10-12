import random
import math
true = True

"""
#1

toke = int(input("Kezőtőke: "))
kamat = int(input("Kamatlab % ban: "))
kivant = 300000
year = 0
while toke <= kivant:
    toke += toke*kamat/100
    year+=1

print(f"{year} évbe telt amig {kivant} lett a tőke")
"""
#2
"""
eset = int(input("Milyen magasról esik le a cucc? (m) "))
patt = 0
while eset >=0.2:
    eset /= 2
    patt +=1

print(f"{patt} ptaatnás volt")

"""

#3

"""szam = int(input("Pozitív egész szám: "))
lepes = 0
if szam == 1:
    print("A szám 1")
else:
    while szam != 1:
        lepes+= 1
        if szam %2 == 0:
            szam /= 2
            print(szam)
        else:
            szam = szam*3+1
            print(szam)
    print(f"{lepes} lépésből lett meg")"""


#4
"""
hatar = int(input("Felsőhatár: "))
hatvany = 0
while 2 ** (hatvany+1) < hatar:
    hatvany += 1
print(f"A legnagyobb 2 hatvány a {hatar} alatt a {2**hatvany}")
"""

#5
"""
szam = 0
lepes = 0
while szam < 500:
    szam += int(input("Adj egy számot:"))
    lepes += 1
print(f"Vegosszeg {szam} lépések: {lepes}")

"""
#6
"""
jelkod = "titok123"
porba = 0
while True:
    
    if input("Kérem a jelszót: ") == jelkod:
        print(f"Sikeres jelszó, próbák száma: {porba}")
        break
    else:
        print("Hibás jelszó próbáld újra")
        porba += 1

"""
#7
"""miertkellez = 0
while True:
    miertkellez = input("Kérek egy szót: ")
    if miertkellez == "stopp" or miertkellez == ".":
        print("bye")
        break
    else: 
        print(miertkellez.upper())
"""
#8


a = True
while a:
    eletkor = int(input("Életkor: "))
    if 0<=eletkor<=120:
        print(f"Köszönöm az életkorod: {eletkor}")
        a = False
    else:
        print("Hibás")


#1
osszeghatar = 1000
valtas = 0
cimlet200 = 0
cimlet100 = 0
cimlet50 = 0
cimlet20 = 0
cimlet10 = 0
cimlet5 = 0
osszeg = int(input("Adj egy 5-tel osztható számot: "))
if osszeg < osszeghatar:
    while True:
        if osszeg > 200:
            osszeg -= 200
            cimlet200+=1
        elif osszeg > 100:
            osszeg-=100
            cimlet100+=1
        elif osszeg > 50:
            osszeg-=50
            cimlet20+=1
        elif osszeg> 20:
            osszeg-=20
            cimlet20+=1
        elif osszeg > 10:
            osszeg -=10
            cimlet10+=1
        else:
            osszeg-=5
            cimlet5+=1
            break




































