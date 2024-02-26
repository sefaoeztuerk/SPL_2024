import random

#Erstelle eine Funktion die 2 Zahlen addiert

def addiere_zahlen(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

ergebnis = addiere_zahlen(5, 7)
print("Summe:", ergebnis)

#Erstelle eine Funktion, die eine zufällige Zahl zwischen 100 und 200 zurückliefert

def zufallszahl():
    return random.randint(100, 200)

zufalls_num = zufallszahl()
print("Zufallszahl:", zufalls_num)

#Erstelle eine Funktion, die ein Wort aus einem String Array zurückliefert. 

def zufaelliges_wort(wort_array):
    return random.choice(wort_array)

wort_liste = ["hans", "peter", "susi"]
zufaelliges_wort = zufaelliges_wort(wort_liste)
print("Zufälliges Wort:", zufaelliges_wort)



