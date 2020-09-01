# This are the mutable cells in the board as dict
cells = {
"aa":"1", "ab":"2", "ac":"3", 
"ba":"4", "bb":"X", "bc":"6",
"ca":"7", "cb":"8", "cc":"9"
}

def DisplayBoard(): #Print current board
    #The board as a dict
    board = {
    "a": "+-------+-------+-------+",
    "b": "|       |       |       |",
    "row1": "|   "+cells["aa"]+"   |   "+cells["ab"]+"   |   "+cells["ac"]+"   |",
    "d": "|       |       |       |",
    "e": "+-------+-------+-------+",
    "f": "|       |       |       |",
    "row2": "|   "+cells["ba"]+"   |   "+cells["bb"]+"   |   "+cells["bc"]+"   |",
    "h": "|       |       |       |",
    "i": "+-------+-------+-------+",
    "j": "|       |       |       |",
    "row3": "|   "+cells["ca"]+"   |   "+cells["cb"]+"   |   "+cells["cc"]+"   |",
    "l": "|       |       |       |",
    "m": "+-------+-------+-------+",
    }   
    for row in board:
        print(board[row])

free_fields = []
def MakeListOfFreeFields(): #Lists current free fields
    global free_fields 
    free_fields = [str(field) for field in cells.values() if field.isdigit()]

def EnterMove():
    new_move = str(input("Enter your move: ")) #Asks input new move
    if new_move.isdigit() and 0 < int(new_move) <= 9: #Checks input is valid digit
        if new_move in free_fields : #Checks input is available cell
            #Updates cell with input
            if new_move == "1": cells["aa"] = "O"
            elif new_move == "2": cells["ab"] = "O"
            elif new_move == "3": cells["ac"] = "O"
            elif new_move == "4": cells["ba"] = "O"
            elif new_move == "6": cells["bc"] = "O"
            elif new_move == "7": cells["ca"] = "O"
            elif new_move == "8": cells["cb"] = "O"
            elif new_move == "9": cells["cc"] = "O"
        else:
            return print("That cell is not available"), EnterMove()
    else:
        print("You must choose a number between 1 and 9"), EnterMove()
    
def VictoryFor():
    row1 = [cells["aa"], cells["ab"], cells["ac"]]
    row2 = [cells["ba"], cells["bb"], cells["bc"]]
    row3 = [cells["ca"], cells["cb"], cells["cc"]]
    column1 = [cells["aa"], cells["ba"], cells["ca"]]
    column2 = [cells["ab"], cells["bb"], cells["cb"]]
    column3 = [cells["ac"], cells["bc"], cells["cc"]]
    if (
        len(free_fields) != 0 and
        row1[0] == row1[1] == row1[2] == "O" or
        row2[0] == row2[1] == row2[2] == "O" or
        row3[0] == row3[1] == row3[2] == "O" or
        column1[0] == column1[1] == column1[2] == "O" or
        column2[0] == column2[1] == column2[2] == "O" or
        column3[0] == column3[1] == column3[2] == "O"
        ):
        print("You WON!")
    elif (
        len(free_fields) != 0
        and row1[0] == row1[1] == row1[2] == "X"
        or row2[0] == row2[1] == row2[2] == "X"
        or row3[0] == row3[1] == row3[2] == "X"
        or column1[0] == column1[1] == column1[2] == "X"
        or column2[0] == column2[1] == column2[2] == "X"
        or column3[0] == column3[1] == column3[2] == "X"
          ):
        print("You LOST!")
    else:
        pass
    
import random
def DrawMove():
    if len(free_fields) != 0:
        auto_move = random.choice(free_fields)
        if auto_move == "1": cells["aa"] = "X"
        elif auto_move == "2": cells["ab"] = "X"
        elif auto_move == "3": cells["ac"] = "X"
        elif auto_move == "4": cells["ba"] = "X"
        elif auto_move == "6": cells["bc"] = "X"
        elif auto_move == "7": cells["ca"] = "X"
        elif auto_move == "8": cells["cb"] = "X"
        elif auto_move == "9": cells["cc"] = "X"
    
DisplayBoard()
MakeListOfFreeFields()
while len(free_fields) != 0:
    EnterMove()
    MakeListOfFreeFields()
    DisplayBoard()
    VictoryFor()
    DrawMove()
    MakeListOfFreeFields()
    DisplayBoard()
    VictoryFor()
print("It's a DRAW!")