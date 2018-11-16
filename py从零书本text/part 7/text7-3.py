def personinfo1(arg,*vart):
	print(arg)
	for var in vart:
		print('可变参数：',var)
	return
personinfo1('小美','123','3456')

other={'城市':'北京','爱好':'编程'}
def personinfo2(name,number,**kw):
	print('名称:',name,'学号:',number,'其他:',kw)
personinfo2('小智','1002',城市=other['城市'],爱好=other['爱好'])
#方法二
print('\n')
other={'城市':'北京','爱好':'编程'}
person=('小智','1002')
def personinfo3(name,number,**kw):
	print('名字:',name,'number:'.number,'其他:',kw)
personinfo2(*person,**other)
