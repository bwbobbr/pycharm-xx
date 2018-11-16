class Grangfather():
	def __init__(self,name):
		self.name = name

class Father(Grangfather):
	def __init__(self,name):
		self.name = name
		print(self.name)
		print("I am your father")

class Son(Father,Grangfather):
	def __init__(self,name):
		#Father.__init__(self,name)          此语句有问题,及时类与类之间没有关系也能调用他的构造函数
		super(Son, self).__init__(name)
		print("{0} is my self".format(self.name))

son = Son("yueyue")
