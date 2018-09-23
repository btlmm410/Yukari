for i in range(9,0,-1):
    for g in range(0,9-i):
	    print(end="                 ")
    for j in range( i,0,-1):
        a='{0}x{1}={2}'.format(i,j,i*j)
        print('%10s'%a,end=' ')

    print()
