for i in range (1,10000):
	ls=[]
	sum= 0
	for j in range(1,i):
		if i%j==0:
			ls.append(j)
	for item in ls:
		sum += item
	if sum == i:
		print(i)
			
	