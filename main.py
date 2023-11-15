import random
import time

ls = ["rock","paper","scissors"]
running = True
while running:
    player = None
    computer = random.choice(ls)
    player = input("choose rock,paper or scissors:")
    while player not in ls:
        player = input("i said choose from rock,paper or scissors:")
    time.sleep(0.5)
    print(f"player: {player}")
    time.sleep(0.5)
    print(f"computer: {computer}")
    if player == computer:
        time.sleep(0.5)
        print("it's tie")
    elif player == "rock" and computer == "paper":
        time.sleep(0.5)
        print("you loose")
    elif player == "paper" and computer == "scissors":
        time.sleep(0.5)
        print("you loose")
    elif player == "scissors" and computer == "rock":
        time.sleep(0.5)
        print("you loose")
    else:
        time.sleep(1)
        print("you win")

        time.sleep(0.5)
        res = input("do you want to play again (y/n):").lower()
        if res != "y":
            running = False
            time.sleep(0.4)
            print("thanks for playing!")
        elif res == "y":
            continue


