def alpha():
	for i in range(6):
		for j in  range(5):
			if j==0 or i==0 and j<4 or j==4 and 0<i<5 or i==5 and j<4:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
alpha()