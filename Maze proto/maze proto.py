from random import *
import msvcrt
import os
import sys
import queue

matrix = [[0 for cols in range(12)]for rows in range(12)]
matrixtest = [[0 for cols in range(12)]for rows in range(12)]




player = {"x":1,"y":1}

q = queue.Queue()

def creatmatrix():
	# for i in range(12):
	# 	for j in range(12):
	# 		if i == 0 or i == 11:
	# 			matrix[i][j] = 1
	# 			continue
	# 		if (i == 1 and j == 1) or (i == 10 and j == 11) or (i == 10 and j == 10):
	# 			matrix[i][j] = 0
	# 			continue
	# 		if j == 0 or j == 11:
	# 			matrix[i][j] = 1
	# 			continue

	# 		matrix[i][j] = randrange(2)

	for i in range(12):
		for j in range(12):
			if i == 0 or i == 11:
				matrix[i][j] = 1
				matrixtest[i][j] = matrix[i][j]
				continue
			if (i == 1 and j == 1) or (i == 10 and j == 11) or (i == 10 and j == 10):
				matrix[i][j] = 0
				matrixtest[i][j] = matrix[i][j]
				continue
			if j == 0 or j == 11:
				matrix[i][j] = 1
				matrixtest[i][j] = matrix[i][j]
				continue

			matrix[i][j] = randrange(2)
			matrixtest[i][j] = matrix[i][j]

	# matrix[10][10] = randrange(2)
	# matrixtest = list(matrix)



def drawmatrix():
	for i in range(12):
		for j in range(12):
			if (player["x"] == i) and (player["y"] == j):
				print("★",end='')
			elif matrix[i][j] == 1:
				print("■",end='')
			else :
				print("□",end='')
			#print(matrix[i][j],end='')
		print()

def move(key):
	if key == 'w'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrix[player["x"]-1][player["y"]] == 0 :
			player["x"] -= 1
	elif key == 's'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrix[player["x"]+1][player["y"]] == 0 :
			player["x"] += 1
	elif key == 'a'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrix[player["x"]][player["y"]-1] == 0 :
			player["y"] -= 1
	elif key == 'd'.encode():
		if matrix[player["x"]][player["y"]+1] == 0 :
			player["y"] += 1
	elif  key == b'\x03':
		sys.exit(0)

	if (player["x"] == 10) and (player["y"] == 11) :
		os.system('cls')
		print("Victory!!!")
		msvcrt.getch()
		sys.exit(0)


def searchroute(x,y):
	matrixtest[x][y] = 1

	if matrixtest[x-1][y] == 0:
		q.put([x-1,y])

	if matrixtest[x][y+1] == 0:
		q.put([x,y+1])

	if matrixtest[x+1][y] == 0:
		q.put([x+1,y])

	if matrixtest[x][y-1] == 0:
		q.put([x,y-1])

def check():
	q.put([player["x"],player["y"]])
	route = q.get()

	while route != [10,11]:
		searchroute(route[0],route[1])
		if q.empty() :
			return False
		route = q.get()
	return True


creatmatrix()
os.system('cls')
drawmatrix()
while True:
	if check():
		drawmatrix()
		break
	else:	
	# print(check())
		print("Fail")
		drawmatrix()
		creatmatrix()

# print(check())

while True:
	move(msvcrt.getch())
	os.system('cls')
	drawmatrix()