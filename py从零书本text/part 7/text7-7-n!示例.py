def fact (n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
a=input('请输入n的值：')
a=int(a)
print('输入值的%s！=%s'%(a,fact(a)))