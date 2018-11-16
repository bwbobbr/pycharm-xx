class A():
	name = "liuying"
	age = 18

	def __init__(self):     #留个疑问__init__?首先调用 ---构建函数
		self.name = "aaa"
		self.age = 2

	def b(self):
		print("My name is:{0}".format(self.name))
		print("My age is:{0}".format(self.age))


class B():
	name = "xiaoming"
	age = 666
sb = A()

#此时,系统会默认把a作为第一个参数传入函数,就是传入__init__里面
sb.b()  #sb是A()里面的一个对象 故可以()??

#A.b()   类提取,此式子里面缺少(参数),因为上文代码中有b(self)这个参数
A.b(sb)    #sb.b() ==A.b(sb)

A.b(A)  #提取A类
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.b(B)  #提取B类