def personinfo(age,name):
	print('年龄:',age)
	print('名字:',name)
	return
personinfo(name='小美',age=21)

def defaultparam(name,age=13):
	print('age:',age)
	print('name:',name)
defaultparam('小美',19)