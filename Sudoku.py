import time

JsonMap = {}

Map = [['0','5','8', '0','0','2', '4','0','0'],
	   ['7','0','0', '0','0','0', '1','0','0'],
	   ['0','9','1', '0','0','4', '0','3','0'],

	   ['0','0','0', '0','0','0', '3','4','0'],
	   ['8','0','5', '0','3','9', '0','2','0'],
	   ['0','0','7', '0','2','6', '8','0','0'],

	   ['0','0','4', '1','0','0', '6','0','7'],
	   ['0','0','0', '0','6','3', '0','0','4'],
	   ['0','0','6', '0','0','0', '0','1','0']]

Map1 = list(map(list, Map))


def CreateJson():
	for x in range(9):
		for y in range(9):
			JsonMap[str(x)+'x'+str(y)] = {1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6 : False, 7 : False, 8 : False, 9 : False}

CreateJson()

def CheckLineColun():
	for y in range(9):
		for x in range(9):
			if int(Map[y][x]) != 0:
				for i in range(1,10):
					JsonMap[str(y)+'x'+str(x)][i] = True

				for i in range(9):
					JsonMap[str(y)+'x'+str(i)][int(Map[y][x])] = True
					JsonMap[str(i)+'x'+str(x)][int(Map[y][x])] = True

def CheckBlock():
	for y in range(9):
		for x in range(9):
			if int(Map[y][x]) != 0:
				xblock = int(x / 3)
				yblock = int(y / 3)
				for YBlo in range(3):
					for XBlo in range(3):
						JsonMap[str(YBlo + yblock * 3)+'x'+str(XBlo + xblock * 3)][int(Map[y][x])] = True


def ChangeValues():
	for y in range(9):
		for x in range(9):
			Soma = 0
			for i in range(1,10):
				if JsonMap[str(y)+'x'+str(x)][i] == True:
					Soma = Soma + 1
			if Soma == 8:
				for i in range(1,10):
					if JsonMap[str(y)+'x'+str(x)][i] == False:
						Map[y][x] = i

def ChangeBlockValues():
	for i in range(1,10):
		for yblock in range(3):
			for xblock in range(3):
				Soma = 0
				for y in range(3):
					for x in range(3):
						if JsonMap[str(y+yblock*3)+'x'+str(x+xblock*3)][i] == True:
							Soma = Soma + 1
						if Soma == 8:
							for yblo in range(3):
								for xblo in range(3):
									if JsonMap[str(yblo+yblock*3)+'x'+str(xblo+xblock*3)][i] == False:
										Map[yblo+yblock*3][xblo+xblock*3] = i

def PrintSudo():
	print('----------------------')
	for y in range(9):
		for x in range(9):
			if x % 3 == 0:
				print('|'+str(Map[y][x])+ ' ', end='')
			else:
				print(str(Map[y][x])+ ' ', end='')
		print('|')
		if (y+1) % 3 == 0 and y != 0:
			print('----------------------')
	print('\n')

def Verifi():
	for y in range(9):
		for x in range(9):
			if int(Map[y][x]) == 0:
				return 1
	print('Sudoku Done')
	return 0

def CheckIgual():
	global Map1
	for y in range(9):
		for x in range(9):
			if Map1[y][x] != Map[y][x]:
				Map1 = list(map(list, Map))
				return 1
	print('Impossible to Continue')
	return 0
	

Run = 1
PrintSudo()
while Run:
	CheckLineColun()
	CheckBlock()
	ChangeValues()
	ChangeBlockValues()
	PrintSudo()
	Run = Verifi()
	if Run:
		Run = CheckIgual()
	