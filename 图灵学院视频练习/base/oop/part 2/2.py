class Animal(object):

	def __init__(self):
		print("小弱鸡")


class Dog(Animal):
	pass

class HappyDog(Dog):
	pass

huahua = HappyDog()             #构造函数取接近的一个,子类可以往父类上面取