def dj(s):
	k=s
	w=k[-5:-2:1]
	e=k[-6::5]
	return w,e
k=dj("Django")
print(k)
	
	