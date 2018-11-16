class Person(object):
	def __init__(self):
		self.name = "sb"
		self.age = 18
		self.fuction = "running"
		print("I am running")

	def fun1(self):
		print(self.name,"-"*6,self.fuction)

yueyue = Person()
yueyue.fun1()