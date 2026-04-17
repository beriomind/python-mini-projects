# --------------------------------------
# - Dice Rolling (dice-roll.py)
# - Version 1
# --------------------------------------
import random

i = 0
while True:
    roll = random.randint(1, 6)
    i += 1

    print(f"Rolling Time {i} : {roll}")

    stop_rolling = input("Do you want to stop rolling ? (y/n) ")

    if stop_rolling == "y":
        break
