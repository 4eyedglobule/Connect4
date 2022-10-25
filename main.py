# This program runs a connect 4 game between 2 players.

#This method allows 2 players to choose whatever they want for their symbols. It returns an array containing both of the players' selected symbols.
def playerSymbolSelection():
    player1symbol = input("Player 1, whoever that might be, type your symbol: X, O, or something else. Warning: Multiple character symbols will distort the board:")
    player2symbol = ""
    player2symbol = input("Player 2, enter your symbol, so long as it is not the same as player 1's:")
    while(player2symbol == player1symbol):
        player2symbol = input("Player 2, please re-enter your symbol as it is the same as player 1's:")
    return [player1symbol,player2symbol]

#Checks the current grid (Dictionary) to see if there are any connect 4's or if the board is filled.
#currentGird parameter: The dictionary of lists representing the grid.
#playerSymbols parameter: The short list that contains both of the players' symbols.
def checkGrid(currentGrid,playerSymbols):
    previousToken = playerSymbols[0]
    TokenSlots = []
    gkeys = list(currentGrid.keys())
    for i in currentGrid:#Checks the grid for any vertical connections
        if len(TokenSlots) < 4:
            TokenSlots = []
        for j in range(len(currentGrid[i])):
            if len(TokenSlots) > 3:#If there have been more than 3 consecutive vertical tokens a player has won
                if previousToken == playerSymbols[0]:
                    print("Player 1 has won. The winning slots are: "+str(TokenSlots))
                else:
                    print("Player 2 has won. The winning slots are: "+str(TokenSlots))
                displayGrid(currentGrid)
                return True
            elif currentGrid[i][j] == previousToken:#If win condition has not been met and consecutive tokens have been found
                TokenSlots.append(i + str(j))
            else:#If current token is different from last token then the checking token variable changes to match current token
                TokenSlots = []
                if not currentGrid[i][j] == "*":
                    previousToken = currentGrid[i][j]
                    TokenSlots = [i+str(j)]
    for k in range(len(currentGrid["A"])):#Checks the grid for any horizontal connections
        if len(TokenSlots) < 4:
            TokenSlots = []
        for i in currentGrid:
            if len(TokenSlots) > 3:#If there have been more than 3 consecutive horizontal tokens a player has won
                if previousToken == playerSymbols[0]:
                    print("Player 1 has won. The winning slots are: "+str(TokenSlots))
                else:
                    print("Player 2 has won. The winning slots are: "+str(TokenSlots))
                displayGrid(currentGrid)
                return True
            elif currentGrid[i][k] == previousToken:#If win condition has not been met and consecutive tokens have been found
                TokenSlots.append(i+str(k))
            else:#If current token is different from last token then the checking token variable changes to match current token
                TokenSlots = []
                if not currentGrid[i][k] == "*":
                    previousToken = currentGrid[i][k]
                    TokenSlots = [i + str(k)]
    bonus = 0 #Needed in order for the loop to check diagonally
    for i in range(12):#Checks the grid for any left to right diagonal connections
        if len(TokenSlots) < 4:
            TokenSlots = []
        if i == 6:
            bonus = 0
        for f in range(6):
            if i < 6:
                a = f + bonus
                b = f
            else:
                a = f
                b = f + bonus
            if len(TokenSlots) > 3:#If there have been more than 3 consecutive diagonal tokens a player has won
                if previousToken == playerSymbols[0]:
                    print("Player 1 has won. The winning slots are: "+str(TokenSlots))
                else:
                    print("Player 2 has won. The winning slots are: "+str(TokenSlots))
                displayGrid(currentGrid)
                return True
            elif currentGrid[gkeys[a]][b] == previousToken:#If win condition has not been met and consecutive tokens have been found
                TokenSlots.append(gkeys[a] + str(b))
            else:#If current token is different from last token then the checking token variable changes to match current token
                TokenSlots = []
                if not currentGrid[gkeys[a]][b] == "*":
                    previousToken = currentGrid[gkeys[a]][b]
                    TokenSlots = [gkeys[a] + str(b)]
            if gkeys[a] == "F" or b > 4:
                break
        bonus += 1
    bonus = 6
    for i in range(12):#Checks the grid for any right to left diagonal connections
        if len(TokenSlots) < 4:
            TokenSlots = []
        if i == 6:
            bonus = 0
        for f in range(5, -1, -1):
            if i < 6:
                c = f - bonus
                d = 5 - f
            else:
                c = f
                d = 5 - f + bonus
            if len(TokenSlots) > 3:  # If there have been more than 3 consecutive diagonal tokens a player has won
                if previousToken == playerSymbols[0]:
                    print("Player 1 has won. The winning slots are: " + str(TokenSlots))
                else:
                    print("Player 2 has won. The winning slots are: " + str(TokenSlots))
                displayGrid(currentGrid)
                return True
            elif currentGrid[gkeys[c]][d] == previousToken:  # If win condition has not been met and consecutive tokens have been found
                TokenSlots.append(gkeys[c] + str(d))
            else:  # If current token is different from last token then the checking token variable changes to match current token
                TokenSlots = []
                if not currentGrid[gkeys[c]][d] == "*":
                    previousToken = currentGrid[gkeys[c]][d]
                    TokenSlots = [gkeys[c] + str(d)]
            if gkeys[c] == "A" or b > 4:
                break
        bonus += 1
    return False

#Displays the current grid. The grid is a dictionary consisting of lists, with each list being a column. Works for grids of all sizes as long as
#their columns are all of uniform size.
#currentGird parameter: The dictionary of lists representing the grid.
def displayGrid(currentGrid):
    for j in currentGrid:#First prints all the column names/keys
        print(" "+j+" ", end =",")
    print("")  # Adds a newline
    for k in range(len(currentGrid["A"])-1,-1,-1):#Then prints the columns, based on the first column's length
        for i in currentGrid:
            print(" "+currentGrid[i][k]+" ", end =",")
        print(k)  # Prints row number whilst adding a newline

#The main method, or the method that brings all the methods together
def main():
    playerTurn = 0
    playerSymbols = playerSymbolSelection()
    # The columns are sorted so the first ones in the list are actually at the bottom of the column
    grid = {
        "A": ["*", "*", "*", "*", "*", "*"],
        "B": ["*", "*", "*", "*", "*", "*"],
        "C": ["*", "*", "*", "*", "*", "*"],
        "D": ["*", "*", "*", "*", "*", "*"],
        "E": ["*", "*", "*", "*", "*", "*"],
        "F": ["*", "*", "*", "*", "*", "*"],
    }
    while(not checkGrid(grid,playerSymbols)):
        print("---------------------------------------------------------------------")
        print("Player "+str(playerTurn+1)+", it is currently your turn. Your symbol is "+playerSymbols[playerTurn]+".")
        displayGrid(grid)
        columnInput = input("Please indicate which column you'd like to insert your token by inputting the relevant letter.")
        grid[columnInput][grid[columnInput].index("*")] = playerSymbols[playerTurn]
        print("---------------------------------------------------------------------")
        if playerTurn == 1:
            playerTurn = 0
        else:
            playerTurn += 1

main()
