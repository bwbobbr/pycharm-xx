class Student():

	def __init__(self,name,score):             # 在对a实例化时就执行了__init__语句构造函数
		self.name = name                        #调用函数是使用self.name
		self.score = score

	def  info(self):
		print("名字:",self.name,"分数:",self.score)   # 由此可见非构造函数可以调用类中的构造函数


a = Student("xiaoming",99)
a.info()

