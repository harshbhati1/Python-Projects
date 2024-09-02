# Welcome code
print("Welcome to Tic Tac Toe Game")
print("Player 1: X")
print("Player 2: O")
print("To place your character you'll have to enter row and column number.")
print("For example: ")
print("Player 1:- Enter row: 0")
print("Player 1:- Enter col: 1")

print("   | X |   ")
print("-----------")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("\n \n -------- Game Starts Now -------- \n \n ")


#program code
storage = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   '],
]


#storage printing 
def output(storage):
    ans = f"{storage[0][0]}|{storage[0][1]}|{storage[0][2]}\n-----------\n{storage[1][0]}|{storage[1][1]}|{storage[1][2]}\n-----------\n{storage[2][0]}|{storage[2][1]}|{storage[2][2]}"
    return ans
    
#winning function
def winning(storage):
    for i in range(3):
        if storage[i][0] == storage[i][1] == storage[i][2] == ' X ' or storage[0][i] == storage[1][i] == storage[2][i] == ' X ':
            return 'X'
        elif storage[i][0] == storage[i][1] == storage[i][2] == ' O ' or storage[0][i] == storage[1][i] == storage[2][i] == ' O ':
            return 'O'
    if storage[0][0] == storage[1][1] == storage[2][2] == ' X ' or storage[0][2] == storage[1][1] == storage[2][0] == ' X ':
        return'X'
    elif storage[0][0] == storage[1][1] == storage[2][2] == ' O ' or storage[0][2] == storage[1][1] == storage[2][0] == ' O ': 
        return 'O'
    return 'Z'

# isOver function
def isOver(storage):
    if winning(storage) == 'X':
        return 'X wins'
    elif winning(storage) == 'O':
        return 'O wins'
    elif '   ' not in storage[0] and '   ' not in storage[1] and '   ' not in storage[2]:
        return 'No one wins'
    
    return 'c'

#user input function
def userInput(storage,player):
    row = int(input(f"Player {player} :- Enter the row number: "))
    col = int(input(f"Player {player} :- Enter the col number: "))
    
    if (storage[row][col] != '   '):
        print("Please make sure the field is empty")
        userInput(storage,player)
    else:
        storage[row][col] = " X " if player == 1 else " O "
# actual game 
p1 = False
p2 = False

while True:
    print(output(storage))
    if isOver(storage) != 'c':
            print(isOver(storage))
            break
    if p1 == False:
        p1 = True
        p2 = False
        userInput(storage,1)
    else:
        p2 = True
        p1 = False
        userInput(storage,2)