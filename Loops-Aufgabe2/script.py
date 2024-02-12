#Zähle die geraden Ziffern zwischen 1 und 1000 zusammen - Tip: Starte den Loop bei 2 und erhöhe den Zählindex jeweils um 2.

summe_gerade_Ziffer = 0


for zahl in range(2, 1001, 2):

    summe_gerade_Ziffer += zahl


print("Die Summe der geraden Zahlen von 1 bis 1000 ist:", summe_gerade_Ziffer)
