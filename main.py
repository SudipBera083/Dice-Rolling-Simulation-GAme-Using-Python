
import time

import random


user_choice="yes"

while(user_choice=="yes" or user_choice=="y"):

    print("please wait a moment...")
    time.sleep(1)

    dice1=random.randint(1,6)
    dice2 = random.randint(1, 6)

    time.sleep(1)

    print("Dice-1:",dice1)
    print("Dice-2:",dice2)

    if dice1==dice2:
        print("Congratulations, the number of two dice is matched!")
    user_choice=input("Do you want to play it again?\nPress y for yes and n for No").lower()

print("Thanks for playing !")
