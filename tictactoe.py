import os

class tictactoe:
    def __init__(self, v = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]):
        self.running = True
        self.value = v
        self.player = None
        self.playerChoise = {True : "X", False : "O"}
        self.warningMessage = " "
    
    def getRunning(self) -> bool:
        return self.running

    def printBoard(self):
        self.getHelp()
        print("  Player " + self.playerChoise[self.player]+ " turn:\n")
        print(f"    {self.value[0][0]} | {self.value[0][1]} | {self.value[0][2]}")
        print("   -----------")
        print(f"    {self.value[1][0]} | {self.value[1][1]} | {self.value[1][2]}")
        print("   -----------")
        print(f"    {self.value[2][0]} | {self.value[2][1]} | {self.value[2][2]}")
        print(f"\n{self.warningMessage}\n")

    def getHelp(self):
        os.system('cls')
        print("\n  Help menu")
        print("-----------------")
        print("    1 | 2 | 3")
        print("   -----------")
        print("    4 | 5 | 6")
        print("   -----------")
        print("    7 | 8 | 9\n\n")

    def selectPlayer(self):
        while True:
            try:
                option = int(input("What do you want to be?: \n1) X. \n2) O.\n>> "))
                if option== 1:
                    self.player = True
                    break
                elif option == 2:
                    self.player = False
                    break
                else:
                    print("Invalid option!.")
            except:
                print("Warning: Invalid format!.")

    def isEmpty(self, pos):
            if pos == 1 :
                if self.value[0][0] == " ": return True
            elif pos == 2:
                if self.value[0][1] == " ": return True
            elif pos == 3:
                if self.value[0][2] == " ": return True
            elif pos == 4:
                if self.value[1][0] == " ": return True
            elif pos == 5:
                if self.value[1][1] == " ": return True
            elif pos == 6:
                if self.value[1][2] == " ": return True
            elif pos == 7:
                if self.value[2][0] == " ": return True
            elif pos == 8:
                if self.value[2][1] == " ": return True
            elif pos == 9:
                if self.value[2][2] == " ": return True
            return False

    def setValueBoard(self, pos, valor):
            if pos == 1 :
                self.value[0][0] = valor
            if pos == 2:
                self.value[0][1] = valor
            if pos == 3:
                self.value[0][2] = valor
            if pos == 4:
                self.value[1][0] = valor
            if pos == 5:
                self.value[1][1] = valor
            if pos == 6:
                self.value[1][2] = valor
            if pos == 7:
                self.value[2][0] = valor
            if pos == 8:
                self.value[2][1] = valor
            if pos == 9:
                self.value[2][2] = valor

    def changePlayer(self):
        # change player:
        self.player = not(self.player)

    def playerTurn(self):
        while True:
            try:
                pos = int(input(">> "))
                if pos < 1 or pos > 9:
                    raise Exception("Position not in range")
                break
            except: 
                self.warningMessage = "Value not in range (1 - 9), try again..."
                self.printBoard()
            
        if not self.isEmpty(pos): 
            self.warningMessage = f"Position number {pos} is already in use!"
            self.changePlayer() #be the same player
        else:
            self.warningMessage = " "
            self.setValueBoard(pos, self.playerChoise[self.player])


    def checkWinner(self):
        for i in range(3):
            if self.value[i][0] == self.value[i][1] == self.value[i][2] != " ":
                  return (self.playerChoise[self.player])
            elif self.value[0][i] == self.value[1][i] == self.value[2][i] != " ":
                  return (self.playerChoise[self.player])
            elif " " not in self.value[0] and " " not in self.value[1] and " " not in self.value[2]:
                return "draw"
        if self.value[0][0] == self.value[1][1] == self.value[2][2] != " ":
            return (self.playerChoise[self.player])
        if self.value[0][2] == self.value[1][1] == self.value[2][0] != " ":
            return (self.playerChoise[self.player])
        
        self.warningMessage = " " not in self.value[0]

        return " "

    def restar(self):
        self.value = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
        self.player = False
        self.warningMessage = " "

    def playAgain(self):
        again = input("Do you want to play again? (y/n)\n>> ")
        if again == "y":
            self.restar()
            self.selectPlayer()
        else:
            quit()

    def setMessage(self, msg):
        self.warningMessage = msg
