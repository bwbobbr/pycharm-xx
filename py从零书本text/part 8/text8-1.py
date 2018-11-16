class Myclass():
	i = 123
	
	def f(self):
		return"Hello,world!"


use_class = Myclass()    #这称之为类的实例化,即创建一个类的实例,叫做use_class是Myclass的实例化
print("我是类属性的调用",use_class.i)
print("我是类方法的调用",use_class.f())