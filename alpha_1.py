def alpha():
	for i in range(10):
		for j in range(9):
			if i+j==4 and j<5 or j-i==4 and j>4 or i==3 and 0<j<7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
alpha()
	