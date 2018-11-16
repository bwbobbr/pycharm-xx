#九九乘法表
for i in range(1,10):
	i=int(i)
	for j in range (1,i+1):
		print('{0}*{1}={2}'.format(j,i,i*j),end="   ")
	print(' ')