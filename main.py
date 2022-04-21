import random


while True:
    #making the ai
    choice = ["Rock", "Paper", "Scissor"]
    ai = random.choice(choice)


    #making our player

    print("hi am a rock paper scissor game")
    player = input("Choose rock paper or scissor\n")
    player = player.capitalize()


    #making the logic for the game

    if ai == "Rock":
        if player == "Rock":
            print("its a draw")
        if player == "Paper":
            print("You Win!")
        if player == "Scissor":
            print("You lose")

    if ai == "Paper":
        if player == "Rock":
            print("You lose")
        if player == "Paper":
            print("its a draw")
        if player == "Scissor":
            print("You win!")

    if ai == "Scissor":
        if player == "Rock":
            print("You Win!")
        if player == "Paper":
            print("You Lose")
        if player == "Scissor":
            print("its a tie")

    close = input("do you want to continue or close type continue or close\n")
    close = close.capitalize()
    if close == "Continue":
        continue
    if close == "Close":
        break
