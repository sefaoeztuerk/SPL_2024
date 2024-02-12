import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

print("Zahl 1:", number1)
print("Zahl 2:", number2)


#Wenn die erste Zahl kleiner ist als die zweite UND die erste Zahl kleiner ist als 50
#dann gib aus "Zahl 1 ist kleiner als Zahl 2 und Mini"
if number1 < number2 and number1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
		
#Wenn die erste Zahl kleiner ist als 30 oder die zweite Zahl kleiner ist als 30
#dann gib aus "Eine der beiden ist kleiner als 30"
    
if number1 < 30 or number2 < 30:
    print("Eine der beiden ist kleiner als 30")
		
#Wenn die erste Zahl kleiner ist als 50 UND die zweite Zahl ungleich 50 ist
#dann gib aus "Erste Zahl klein, zweite kein 50iger"
    
if number1 < 50 and number2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")