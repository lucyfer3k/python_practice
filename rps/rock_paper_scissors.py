#!/usr/bin/env python3
import random

def winner_rps(player, pc):
    '''Returns string with who is the winner player, PC or is it a draw'''
    if type(player) == int and type(pc) == int:
        if player == pc:
            return "Draw"
        elif (player == 0 and pc == 1) or (player == 1 and pc == 2) or (player == 2 and pc == 0):
            return "PC won"
        elif (player == 1 and pc == 0) or (player == 2 and pc == 1) or (player == 0 and pc == 2):
            return "Player won"
        else:
            return "Error"
    else:
        return "Error"

if __name__ == "__main__":
    print("Rock, paper, scissors game!")
    choice_list = ["rock", "paper", "scissors"]
    i = ""
    while i != "q":
        pc = random.randint(0, 2)
        try:
            player = int(input("\nChoose your poison by inserting correct number!\nRock [0], Paper [1], Scissors [2]: "))
            winner = winner_rps(player, pc)
            print("\nPlayer: {} VS PC: {}\n{}!\n".format(choice_list[player], choice_list[pc], winner))
        except:
            print("Incorrect number inserted!")

        i = input("Try again? [q to exit]: ")
