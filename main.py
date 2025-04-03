# Created by Lucius Coriglione



def print_board(board):
  print("|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|")
  print("|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|")
  print("|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|")

def check_for_win_x(board):
  if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
    print(board[0][0], "wins")
    return True
  elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
    print(board[1][0], "wins")
    return True
  elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
    print(board[2][0], "wins")
    return True
  elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
    print(board[0][0], "wins")
    return True
  elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
    print(board[0][1], "wins")
    return True
  elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
    print(board[0][2], "wins")
    return True
  elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
    print(board[0][0], "wins")
    return True
  elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
    print(board[0][2], "wins")
    return True
  elif board[0][0] != "_" and board[0][1] != "_" and board[0][2] != "_" and board[1][0] != "_" and board[1][1] != "_" and board[1][2] != "_" and board[2][0] != "_" and board[2][1] != "_" and board[2][2] != "_":
    print("Tie")
    return True
  else:
    return False

def check_for_win_o(board):
  if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
    print(board[0][0], "wins")
    return True
  elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
    print(board[1][0], "wins")
    return True
  elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
    print(board[2][0], "wins")
    return True
  elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
    print(board[0][0], "wins")
    return True
  elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
    print(board[0][1], "wins")
    return True
  elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
    print(board[0][2], "wins")
    return True
  elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
    print(board[0][0], "wins")
    return True
  elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
    print(board[0][2], "wins")
    return True
  elif board[0][0] != "_" and board[0][1] != "_" and board[0][2] != "_" and board[1][0] != "_" and   board[1][1] != "_" and board[1][2] != "_" and board[2][0] != "_" and board[2][1] != "_" and board[2][2] != "_":
    print("Tie")
    return True
  else:
    return False
gameOver = False
turn = 1
accepted = False
tictactoe = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
print_board(tictactoe)
while True:
  if not gameOver:
    if turn == 1:
      while not accepted:
        xInput= int(input("enter row you want to place your X: "))-1
        if xInput > 2:
          while xInput > 2:
            xInput -= 2
        yInput= int(input("enter column you want to place your X: "))-1
        if yInput > 2:
          while yInput > 2:
            yInput -= 2
        if tictactoe[xInput][yInput] != "_":
          print("try again you can place here!")
          accepted = False
        else:
          tictactoe[xInput][yInput] = "X"
          accepted = True
      print_board(tictactoe)
      gameOver = check_for_win_x(tictactoe)
      turn = 2
      accepted = False
    else:
      while not accepted:
        xInput= int(input("enter row you want to place your O: "))-1
        yInput= int(input("enter column you want to place your O: "))-1
        if tictactoe[xInput][yInput] != "_":
          print("try again you can place here!")
          accepted = False
        else:
          tictactoe[xInput][yInput] = "O"
          accepted = True
      print_board(tictactoe)
      gameOver = check_for_win_o(tictactoe)
      turn = 1
      accepted = False
  else:
    print("game over")
    break
      
