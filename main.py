import math
import random

print "Welcome to Parcheesi Simulator"

colors = ["r","g","b","y"]

StateArray = []

class Piece:
	def __init__(self,color, memberNumber, position, finished):
		self.c = color
		self.m = memberNumber
		self.p = position
		self.f = finished
		
def game_setup():
	for i in colors:
		for j in range(4):
			tempP = Piece(i,j,0, False)
			StateArray.append(tempP)
			
def roll_dice():
	A = math.ceil(random.random()*6)
	B = math.ceil(random.random()*6)
	return A, B

def pretty_print_state():
	for i in range(len(StateArray)):
		print "Color = {0.c} Member = {0.m} Position = {0.p}".format(StateArray[i])
		
def pick_turn(maxin, turns_after_first):
	ind = (maxin + turns_after_first) % 4
	col = colors[ind]
	return col
		
def move_piece(col):
	#define which member we want to move, for now chose a random member
	memberpick = math.floor(random.random()*5)
	for i in StateArray:
		if i.c == col:
			if i.m == memberpick:
				A, B = roll_dice()
				if i.p == 0:	
					if A == 5 or B == 5:
						i.p += 1
				elif i.p >= 68:
					i.f = True
				else:
					i.p +=  A+B
	

def play_game():
	#beginning step is to move one piece to starting position, i.e. all membernumber 0s
	"""for element in StateArray:
		if element.m == 0:
			element.p = 1
	"""
	#choose first player
	firstcolArr = []
	for col in colors:
		firstcolArr.append(math.ceil(random.random()*6))
	maxin = firstcolArr.index(max(firstcolArr))
	#play game in a loop until you meet the finishing criteria
	turns_after_first = 0
	while is_game_won(StateArray) == False:
		print "New Round"
		col = pick_turn(maxin, turns_after_first)
		move_piece(col)
		pretty_print_state()
		turns_after_first += 1
		
		
	print "Game Over!"
		
def is_pie_finished(p):
	if p.p >= 68:
		return True
	return False
		
	
					
def is_game_won(StateArray):
	
	for co in colors:
		win_count = 0
		for pie in StateArray:
			if pie.c == co:
				if is_pie_finished(pie):
					win_count += 1
			if win_count == 4:
				return co
	else:
		return False




game_setup()
play_game()





