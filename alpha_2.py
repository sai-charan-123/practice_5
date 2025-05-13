def alpha():
	for i in range(7):
		for j in range(4):
			if i==6 or i==0 or j==0 or i==3 or j==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
alpha()