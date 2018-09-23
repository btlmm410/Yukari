for i in range(9,0,-1):
	for j in range(1,i+1):
		a='{0:1}x{1:1}={2:<2}'.format(i,j,i*j)
		print(a,end=' ')
	
	print()
