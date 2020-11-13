import sys
import msvcrt


while True:
	#s1 = sys.stdin.read(1)
	s1 = msvcrt.getch()
	# print(s1)

	if s1 == 'a'.encode():
		print("push a")
	elif  s1 == b'\x03':
		break
	else :
		print("else")


# for x in range(1,10):
# 	print(x)
# 	msvcrt.getch()