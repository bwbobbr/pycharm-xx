def fun1 (*args):
	print('进行自我介绍:')
	print(type(args))
	for cash in args:
		print(cash)
fun1('zhou','18','beijing','running')

print('')
def fun2 (**kwargs):
	print(type(kwargs))
	for v,k in kwargs.items():         #item函数将kwargs变成元祖返回
		print(v,'---',k)
fun2(name='john',age=18,home='beijing',hobby='running')
#	print(kwargs,'\n')                #kwargs他是一个字典的形式输出是一个整体
#fun2(name='john',age=18,home='beijing',hobby='running')