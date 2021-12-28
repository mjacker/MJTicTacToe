import os
#from tictactoe import getBoard

from tictactoe import tictactoe

def chooseMenu():
    return int(input())

def printMenu():
    os.system('cls')
    print("""
                 TIC TAC Toe
------------------------------------------------
        1) Player vs Player.
        2) Player vs Computer (not implemented).
        0) Exit. """)
    op = chooseMenu()
    if op == 0:
        quit()
    if op == 1:
        pvp()
    if op == 2:
        print("CALL: player vs player")
    print("press enter to continue...")
    input()



def pvp():
    myGame = tictactoe()
    myGame.selectPlayer()  # X or O
    while myGame.getRunning():
        myGame.printBoard()     # print Board
        myGame.playerTurn()
        myGame.printBoard()  
        winner = myGame.checkWinner() 
        if winner  == " ":
            myGame.changePlayer()
        elif winner == "draw":
            myGame.setMessage("Draw game...")
            myGame.printBoard() 
            myGame.playAgain()
        else:
            myGame.setMessage("The winner is: " + winner)
            myGame.playAgain()



if __name__ == '__main__':
    while True:
        printMenu()
    
