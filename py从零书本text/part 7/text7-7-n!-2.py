def fact (n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,product*num)
print('输出值%s'%fact(10))