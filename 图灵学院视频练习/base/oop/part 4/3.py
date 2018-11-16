class Person():
	def __init__(self,name):
		self.name = name

	def __gt__(self, other):    # 进行大小比较的时候触发
		print("{0}会比{1}大么".format(self.name,other.name))   # 注意!!!format后面是self.name!!!
		return self.name >other.name

stu1 = Person("one")
stu2 = Person("two")
print(stu1 > stu2)