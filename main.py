import random
import time
import os
from AI import runAI
tie = False
p1 = "\033[33m   X   \033[m"
p2 = "\033[35m   O   \033[m"
availableSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [
    ["       ", "|", "       ", "|", "       "],
    ["   1   ", "|", "   2   ", "|", "   3   "],  #board[1]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    ["   4   ", "|", "   5   ", "|", "   6   "],  #board[5]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    ["   7   ", "|", "   8   ", "|", "   9   "],  #board[9]
    ["       ", "|", "       ", "|", "       "],
]

boardSave = [
    ["       ", "|", "       ", "|", "       "],
    ["   1   ", "|", "   2   ", "|", "   3   "],  #boardSave[1]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    ["   4   ", "|", "   5   ", "|", "   6   "],  #boardSave[5]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    ["   7   ", "|", "   8   ", "|", "   9   "],  #boardSave[9]
    ["       ", "|", "       ", "|", "       "],
]

boardSave1 = [
    ["       ", "|", "       ", "|", "       "],
    [1, "|", 2, "|", 3],  #boardSave1[1]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    [4, "|", 5, "|", 6],  #boardSave1[5]
    ["       ", "|", "       ", "|", "       "],
    ["-------", "|", "-------", "|", "-------"],
    ["       ", "|", "       ", "|", "       "],
    [7, "|", 8, "|", 9],  #boardSave1[9]
    ["       ", "|", "       ", "|", "       "],
]

thing = ""


#creating the board
def boardSetup(table):
    os.system('clear')
    print("\033[1mWelcome to Tic-Tac-Toe!")
    print(
        "How to play: To play, type in the number that corresponds with the box that you want to put your marker in. Get three in a row before the your opponent to win! \033[m \n"
    )
    global thing
    for item in table:
        for otheritem in item:
            thing += otheritem
        print(thing)
        thing = ""
    print(" ")


boardSetup(board)
userIsP1 = random.randint(0, 1)

playerChoices = []
ColumnP1 = []
ColumnP2 = []
RowP1 = []
RowP2 = []
bothP1 = []
bothP2 = []
dec = [ColumnP1, ColumnP2, RowP1, RowP2, bothP1, bothP2]

isNumber = False




turnCounter = 0

def turn(player):
    global isNumber
    global userIsP1
    global availableSpaces
    global p1
    global p2
    global turnCounter
    turnCounter += 1
    #player's turn
    while isNumber == False:
        if player == p1:
            if userIsP1 == 1:
                playerTurn = input("Type the number here. It must be between 1 and 9 and it must be an available space: ")
            else:
                playerTurn = runAI.choices(boardSave1, availableSpaces, ColumnP1, ColumnP2, RowP1, RowP2, board, boardSave1, userIsP1)
        elif player == p2:
            if userIsP1 == 1:
                playerTurn = runAI.choices(boardSave1, availableSpaces, ColumnP1, ColumnP2, RowP1, RowP2, board, boardSave1, userIsP1)
            else:
                playerTurn = input("Type the number here. It must be between 1 and 9 and it must be an available space: ")

        if playerTurn.isnumeric():

            if int(playerTurn) <= 9 and int(playerTurn) >= 1 and availableSpaces.__contains__(int(playerTurn)):

                isNumber = True
                playerChoices.append(int(playerTurn))
                availableSpaces.remove(int(playerTurn))
                print(availableSpaces)
                playerTurn = int(playerTurn)

                pNum = 1
                pRow = 1

                def append(p, column, row):
                    if p == p1:
                        ColumnP1.append({'column': column})
                        RowP1.append({'row': pRow})
                        bothP1.append({'row': pRow, 'column': column})
                    elif p == p2:
                        ColumnP2.append({'column': column})
                        RowP2.append({'row': pRow})
                        bothP2.append({'row': pRow, 'column': column})

                for i in range(1, 4):
                    if playerTurn == pNum:
                        append(player, 0, pRow)
                        board[pRow][0] = player

                    elif playerTurn == pNum + 1:
                        append(player, 2, pRow)
                        board[pRow][2] = player

                    elif playerTurn == pNum + 2:
                        append(player, 4, pRow)
                        board[pRow][4] = player

                    pRow += 4
                    pNum += 3
    print(playerChoices)
    isNumber = False
    boardSetup(board)


end = False


#setting up win conditions
def winner(choiceboard):
    global end
    global availableSpaces
    global playerChoices
    global board
    global boardSave
    global userIsP1
    global bothP1
    global bothP2
    global tie
    time.sleep(1)
    for item in choiceboard:
        if item == ColumnP1 or item == ColumnP2:
            FirstColumn = int(item.count({'column': 0}))
            SecondColumn = int(item.count({'column': 2}))
            ThirdColumn = int(item.count({'column': 4}))

            if FirstColumn == 3 or SecondColumn == 3 or ThirdColumn == 3:
                end = True

        if item == RowP1 or item == RowP2:
            FirstRow = int(item.count({'row': 1}))
            SecondRow = int(item.count({'row': 5}))
            ThirdRow = int(item.count({'row': 9}))

            if FirstRow == 3 or SecondRow == 3 or ThirdRow == 3:
                end = True

        if item == bothP1 or item == bothP2:
            if {
                    'row': 1,
                    'column': 0
            } in item and {
                    'row': 5,
                    'column': 2
            } in item and {
                    'row': 9,
                    'column': 4
            } in item:
                end = True
            elif {
                    'row': 1,
                    'column': 4
            } in item and {
                    'row': 5,
                    'column': 2
            } in item and {
                    'row': 9,
                    'column': 0
            } in item:
                end = True

    if len(availableSpaces) == 0 and end == False:
      end = True
      tie = True
    if end == True:
      print("Game Over!")

      replay = input("Play again? (Y or N) ")
      if replay.lower() == "y":
            board[1][0] = "   1   "
            board[1][2] = "   2   "
            board[1][4] = "   3   "
            board[5][0] = "   4   "
            board[5][2] = "   5   "
            board[5][4] = "   6   "
            board[9][0] = "   7   "
            board[9][2] = "   8   "
            board[9][4] = "   9   "
            boardSetup(board)
            end = False
            playerChoices.clear()
            bothP1.clear()
            bothP2.clear()
            availableSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            userIsP1 = random.randint(0, 1)
            for item in dec:
                item.clear()
            play()
      else:
            print("Bye!")


def play():
    while end == False:
        turn(p1)
        winner(dec)
        if end == False:
            turn(p2)
            winner(dec)

play()
