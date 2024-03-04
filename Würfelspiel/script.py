import random
import sys

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Willkommen beim Würfelspiel!")
    player_score = 0
    computer_score = 0

    for _ in range(1):
        

        player_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"Du hast eine {player_roll} gewürfelt.")
        print(f"Der Computer hat eine {computer_roll} gewürfelt.")

        player_score += player_roll
        computer_score += computer_roll

    print("\nSpiel beendet!")
    print(f"Deine Zahl: {player_score}")
    print(f"Computer Zahl: {computer_score}")

    if player_score > computer_score:
        print("Du hast gewonnen!")
    elif player_score < computer_score:
        print("Der Computer hat gewonnen.")
    else:
        print("Unentschieden!")

if __name__ == "__main__":
    play_game()















