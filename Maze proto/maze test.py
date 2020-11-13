import queue
import sys
import os
import msvcrt
from random import *


matrix = [[0 for cols in range(12)]for rows in range(12)]
matrixtest = [[0 for cols in range(12)]for rows in range(12)]
# matrix = 	[[1,1,1,1,1,1,1,1,1,1,1,1],
 
# 	        [1,0,0,0,0,0,1,1,1,1,1,1],

# 	        [1,1,1,1,1,0,0,0,0,1,1,1],

# 	        [1,1,1,1,1,0,1,1,1,1,1,1],

# 	        [1,1,1,1,1,0,1,1,1,1,1,1],

# 	        [1,1,1,1,0,0,1,1,1,1,1,1],

# 	        [1,1,1,1,0,1,1,1,1,1,1,1],

# 	        [1,1,1,1,0,0,0,0,0,0,0,1],

# 	        [1,1,1,1,1,1,1,1,1,1,0,1],

# 	        [1,1,1,1,1,1,1,1,1,1,0,1],

# 	        [1,1,1,1,1,1,1,1,1,1,0,0],

# 	        [1,1,1,1,1,1,1,1,1,1,1,1]]


player = {"x":1,"y":1}

stack = queue.LifoQueue()
q = queue.Queue()

# sys.setrecursionlimit(5000)

def creatmatrix():
	for i in range(12):
		for j in range(12):
			if i == 0 or i == 11:
				matrix[i][j] = 1
				continue
			if (i == 1 and j == 1) or (i == 10 and j == 11) or (i == 10 and j == 10):
				matrix[i][j] = 0
				continue
			if j == 0 or j == 11:
				matrix[i][j] = 1
				continue

			matrix[i][j] = randrange(2)
	matrixtest = matrix

def drawmatrix():
	for i in range(12):
		for j in range(12):
			if (player["x"] == i) and (player["y"] == j):
				print("★",end='')
			elif matrixtest[i][j] == 1:
				print("■",end='')
			else :
				print("□",end='')
			#print(matrix[i][j],end='')
		print()

def searchroute(x,y):
	matrix[x][y] = 1

	if matrix[x-1][y] == 0:
		q.put([x-1,y])

	if matrix[x][y+1] == 0:
		q.put([x,y+1])

	if matrix[x+1][y] == 0:
		q.put([x+1,y])

	if matrix[x][y-1] == 0:
		q.put([x,y-1])

creatmatrix()
drawmatrix()
# searchroute(player["x"],player["y"])

def check():
	q.put([player["x"],player["y"]])
	route = q.get()

	while route != [10,11]:
		searchroute(route[0],route[1])
		if q.empty() :
			return False
			# print("fail")
			# sys.exit(0)
		route = q.get()
	# print("success")
	return True

def move(key):
	if key == 'w'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrixtest[player["x"]-1][player["y"]] == 0 :
			player["x"] -= 1
	elif key == 's'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrixtest[player["x"]+1][player["y"]] == 0 :
			player["x"] += 1
	elif key == 'a'.encode():
		if (player["x"] == 1) and (player["y"] == 0) :
			return
		if matrixtest[player["x"]][player["y"]-1] == 0 :
			player["y"] -= 1
	elif key == 'd'.encode():
		if matrixtest[player["x"]][player["y"]+1] == 0 :
			player["y"] += 1
	elif  key == b'\x03':
		sys.exit(0)

	if (player["x"] == 10) and (player["y"] == 11) :
		os.system('cls')
		print("Victory!!!")
		msvcrt.getch()
		sys.exit(0)

while True:
	if check():
		print("success")
		break
	else :
		print("Fail")
		creatmatrix()
		drawmatrix()

while True:
	move(msvcrt.getch())
	os.system('cls')
	drawmatrix()