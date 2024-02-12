import random 

#Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert. Das Programm soll die Zufallszahlen zusammenzählen. 
#Sobald die Zahl 15 oder die Zahl 25 kommt, wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!

summe_Zufallszahlen = 0

while summe_Zufallszahlen != 15 and summe_Zufallszahlen != 25:
    
    Zufallszahl = random.randint(10, 30)
    
    
    print("Generierte Zufallszahl:", Zufallszahl)

    summe_Zufallszahlen += Zufallszahl
    
    
print("Die Summe der Zufallszahlen vor dem Erreichen von 15 oder 25 ist:", summe_Zufallszahlen)
