import random


def test_board(board):
	print(" "*100) 
	print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
	print("----------")
	print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
	print("----------")
	print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")

def player_choice():
	marker="y"
	while marker!="X" and marker!="O":
		marker=input("player 1, choose your marker X or O: ").upper()
	player1=marker
	if player1=="X":
		return("X","O")
	else:
		return("O","X")
	
def make_board(board,mark,position):
	board[position]=mark

def win_check(board,mark):
	if board[1]==mark and board[2]==mark and board[3]==mark:
		return True
	elif board[4]==mark and board[5]==mark and board[6]==mark:
		return True
	elif board[7]==mark and board[8]==mark and board[9]==mark:
		return True
	elif board[1]==mark and board[4]==mark and board[7]==mark:
		return True
	elif board[2]==mark and board[5]==mark and board[8]==mark:
		return True
	elif board[9]==mark and board[6]==mark and board[9]==mark:
		return True
	elif board[1]==mark and board[5]==mark and board[9]==mark:
		return True
	elif board[3]==mark and board[5]==mark and board[7]==mark:
		return True
	else:
		return False

def play_ran():
	 flip=random.randint(0,1)
	 if flip==0:
	 	return "Player 1"
	 else:
	 	return 'Player 2'


def check_empty(board,position):
	if test_board1[position]==" ":
		return True
	else:
		return False

def full_empty_check(board):
	for i in range(1,10):
		if check_empty(test_board1,i):
			return True
	return False

def wrong_postion(board):
	position=0
	while position not in [1,2,3,4,5,6,7,8,9] or not check_empty(board,position):
		position=int(input("Enter position where you want to place your mark using (1-9): "))
	return position
def playagain():
	a=input("would you like to play again yes or no: ")
	if a=="yes":
		return True

print('WELCOME TO THE TIC TAC TOE GAME')
while True:
	the_board=['']*10
	player1,player2=player_choice()
	player_turn=play_ran()
	print (player_turn+' will go first')
	play_game=input("are you ready to play type yes or no: ").lower()
	if play_game=="yes":
		game_on=True
	else:
		game_on=False
	while game_on:
		if player_turn=="Player 1":
			test_board(the_board)
			position=wrong_postion(the_board)
			make_board(the_board,player1,position)
			if win_check(the_board,player1):
				test_board(the_board)
				print("wooh! Player 1 has won")
				game_on=False
			else:
				if full_empty_check(the_board)==False:
					test_board(the_board)
					print("it's a tie")
				else:
					player_turn="Player 2"
		else:
			if player_turn=="Player 2":
				test_board(the_board)
				position=wrong_postion(the_board)
				make_board(the_board,player2,position)
				if win_check(the_board,player2):
					test_board(the_board)
					print("wooh! Player 2 has won")
					game_on=False
				else:
					if full_empty_check(the_board)==False:
						test_board(the_board)
						print("it's a tie")
					else:
						player_turn="Player 1"
	if not playagain():
		break
