def fun():
	global x
	x=100
	print('变量x:%s'%x)
fun()
print('函数之外的变量还有定义值么:%s'%x)
