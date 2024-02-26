import random 

#Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert. Das Programm soll die Zufallszahlen zusammenzählen. 
#Sobald die Zahl 15 oder die Zahl 25 kommt, wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!

summe_Zufallszahlen = 0
Zahl = 0
Zahl2 = 0

while Zahl != 15 and Zahl2 != 25:
    
    Zufallszahl = random.randint(10, 30)
    Zahl, Zahl2 == Zufallszahl
    
    print("Generierte Zufallszahl:", Zufallszahl)

    summe_Zufallszahlen += Zufallszahl
    
    
print("Die Summe der Zufallszahlen vor dem Erreichen von 15 oder 25 ist:", summe_Zufallszahlen)
