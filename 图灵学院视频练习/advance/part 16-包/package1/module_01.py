# 倒入一个包的实例,这是包里面的一个模块
class Student():
	def __init__(self,name = "yueyue",age = 18):
		self.name = name
		self.age = age

	def speak(self):
		print("My name is {0},I am {1} years old.".format(self.name,self.age))

def talk():
	print("I am walking")

if __name__ == '__main__':
	print("Say goodbye")