class Person():
	#实例方法
	def fun1(self):
		print(self)
		print("a"*5)
	#类方法
	@classmethod
	def fun2(self):
		print(self)
		print("b"*5)
	#静态方法
	@staticmethod
	def fun3():
		print("c"*5)

yueyue = Person()
#实例的方法
yueyue.fun1()
#Person.fun1()   实例方法不能自己类调用方法?
#类方法
yueyue.fun2()
Person.fun2()
#静态的方法
yueyue.fun3()
Person.fun3()