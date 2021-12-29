from tictactoe import tictactoe

if __name__ == '__main__':
    myGame = tictactoe()
    while myGame.getRunning():
        myGame.gameStart()
    
