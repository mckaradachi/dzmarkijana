import os
from os import system
from time import sleep
import random

fake_board = [["X"]*4 for i in range(0,4)]

def greet(name):

    choice = input("Do you want to skip greeting?(yes or no): ")
    c = ["yes","no"]
    while choice.lower() not in c:
        choice = input("Do you want to skip greeting?(yes or no): ")

    if choice.lower() == "yes":
        print(f"WELCOME TO THE MEMORY GAME {name.upper()}!!!!!!!!")
        print("LESS GOO!!!!")

    if choice.lower() == "no":
     print(f"WELCOME TO THE MEMORY GAME {name.upper()}!!!!!!!!")
     sleep(3)
     print("HERE ARE SOME RULES FOR YOU TO UNDERSTAND THE GAMEPLAY")
     sleep(2)
     print("THERE ARE 22 CARDS FOR YOU TO REVEAL ")
     sleep(2)
     print("TO REVEAL EACH CARD Y0U NEED TO INPUT IT'S COORDINATES LIKE THIS:  ")
     sleep(2)
     print("Please input coordinates of first card:X;Y ")
     print("Please input coordinates of second card:X;Y ")
     sleep(2)
     print("                                    ")
     print("GAME FIELD LOOKS LIKE THIS: columns(y) 1 2 3 4 ")
     print("                                   r 1 X X X X ")
     print("                                   o 2 X X X X ")
     print("                                   w 3 X X X X ")
     print("                                   s 4 X X X X ")
     print("                                  (x)         ")
     sleep(2)
     print("1.EACH TURN YOU WILL REVEAL A PAIR OF CARDS")
     sleep(2)
     print("2.IF THEY MATCH, THEY WILL BE SAVED ON THE DECK")
     sleep(2)
     print("3.IN CASE THEY DO NOT MATCH ")
     sleep(2)
     print("YOU WILL EFFORTLESLY SPEND YOUR TRY UNLESS YOU WILL REMEMBER  THEM AND THEIR COORDINATES")
     sleep(2)
     print("4.EACH TURN YOU WILL REAVEAL A PAIR OF CARDS")
     sleep(2)
     print("5.YOUR GOAL IS TO FIND EVERY PAIR!!!!!")
     sleep(2)
     print("6.YOU WILL BE GIVEN 16 TRIES TO REACH THE GOAL ")
     sleep(2)
     print(f"GOOD LUCK {name.upper()}!!!!")

def coord_valid(num):
  if len(num.split(";")) != 2:
    return False
  for i in num.split(";"):
      if not i.isdigit():
          return False
  for j in [int(i) for i in num.split(";")]:
    if j < 1 or j > 4:
     return False
  return True

def unique_coords(coords, gaming_board, real_board):
    while gaming_board[coords[0] - 1][coords[1] - 1] == real_board[coords[0] - 1][coords[1] - 1] :
        return False
    while gaming_board[coords[2] - 1][coords[3] - 1] == real_board[coords[2] - 1][coords[3] - 1] :
        return False
    return True


def clear():
 sleep(10)
 os.system('cls||clear')

def create_board():

    real_board = [[0]*4 for i in range(0,4)]
    symbols = "ABCDEFGH"
    pairs = list(symbols)*2
    random.shuffle(pairs)
    for i in range(0,4):
        for j in range(0,4):
            real_board[i][j]= pairs.pop()
    return real_board



def get_coords():
    coords1 = input("Please input coordinates of first card(1;2): ")
    while coord_valid(coords1) == False:
        coords1 = input("Please input coordinates of first card(1;2): ")

    coords2 = input("Please input coordinates of second card(1;2): ")
    while coord_valid(coords2) == False:
        coords2 = input("Please input coordinates of second card(1;2): ")

    while coords1 == coords2:
        coords2 = input("Please input coordinates of second card(1;2): ")
    return [int(i) for i in coords1.split(";")+coords2.split(";")]

def reveal(coords, gaming_board, real_board, fake_board):
    gaming_board[coords[0] - 1][coords[1] - 1] = real_board[coords[0] - 1][coords[1] - 1]
    gaming_board[coords[2] - 1][coords[3] - 1] = real_board[coords[2] - 1][coords[3] - 1]
    for rows in gaming_board:
        print(*rows)
    if real_board[coords[0] - 1][coords[1] - 1] != real_board[coords[2] - 1][coords[3] - 1]:
        gaming_board[coords[2] - 1][coords[3] - 1] = fake_board[coords[2] - 1][coords[3] - 1]
        gaming_board[coords[0] - 1][coords[1] - 1] = fake_board[coords[0] - 1][coords[1] - 1]
    else:
        print("Match!")
    clear()
    return gaming_board

def play_game():
    you_won = False
    gaming_board = [["X"]*4 for i in range(0,4)] #генеруємо дошку яка може змінюватись
    real_board = create_board() #генеруємо дошку
    turns = 0
    name = input("Please input your name: ")
    greet(name) #вітаємо гравця
    for rows in fake_board:
     print(*rows)

    for tries in range(0,24):
        coords = get_coords()  # запитуємо у гравця координати
        while unique_coords(coords, gaming_board, real_board) == False:
            coords = get_coords()
        reveal(coords, gaming_board, real_board, fake_board)
        for rows in gaming_board:
            print(*rows)

        turns += 1

        if gaming_board == real_board:
            you_won= True
            break

    if you_won == True:
        print(f"You won {name.upper()}!")
        sleep(2)
        print(f"It took you {turns} turns to beat it!")
        sleep(3)
    else:
        sleep(3)
        print("You lost")
        sleep(3)

play_game()