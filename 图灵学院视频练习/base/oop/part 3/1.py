#继承的例子
class Animal():
	def __init__(self,name):
		self.name = name

	def moving(self):
		print("I can move...")

class Personal(Animal):
	def __init__(self,name):
		self.name = name

	def running(self):
		print("I can run...")

class Bird(Animal):
	def __init__(self,name):
		self.name = name
		print(self.name)

	def flying(self):
		print("I can fly")

class maque(Bird,Animal):
	#def fuction(self):
	#	print("You know mine.")
	pass


yueyue = maque("yueyue")
#yueyue.flying()
#yueyue.moving()