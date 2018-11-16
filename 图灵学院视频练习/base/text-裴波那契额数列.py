n = input('请输入n的值:')
n= int (n)
def fun (n):
	global i
	i=1
	i=int (i)
	while i <=2 and i >=1:
		if i<=n:
			z=1
			print('{0}'.format(z),end=' ')
			i+=1
	else:
		z = fun(n-1)+ fun(n-2)
		print('{1}'.format(z),end=' ')
fun(n)
