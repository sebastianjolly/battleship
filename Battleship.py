# To run the code, go to Coding Folder -> Python Practice -> Double click -> open with Python ()
# Click on Run on the top -> Click on Run Module
# To write in the Python app, open up Python -> Click on File -> Click on New File

# Battleship game
from random import randint

print("Welcome to the game! You have eight turns, so use them wisely!")

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(9):
  print("Turn: ", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )

    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      if turn == 7:
        print("Game Over")
        print("The correct corrdinates were:")
        print(ship_row)
        print(ship_col)
        break
    print_board(board)
