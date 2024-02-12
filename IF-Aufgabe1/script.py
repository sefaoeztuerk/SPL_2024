
import random

number = random.randint(0, 100)

print("Die Zufallszahl ist:", number)


if number < 20:
    print("Mini")
elif 20 <= number <= 50:
    print("Medium")
else:
    print("Large")

		
		
		