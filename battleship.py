from random import randint

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
    
board = []

for x in range(5):
    board.append(["O"] * 5)

print "Let's play Battleship!"
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn == 3:
            print "Game Over"
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
		    print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
		    print "You guessed that one already."
		else:
		    print "You missed my battleship!"
		    board[guess_row][guess_col] = "X"
