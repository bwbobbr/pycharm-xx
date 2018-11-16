class Student():
	def __init__(self,name = "Nonename",age = 18):
		self.name = name
		self.age = age

	def say(self):
		print("My name is {0},i am {1} years old.".format(self.name,self.age))

def function1():
	print("Good job!")

if __name__ == '__main__':
	print("Hello everyone!")