class Teacher():
	name = "bob"
	age = 18

	def do(self):
		self.name = "sam"
		self.age = 163
		print("My name is:{0}".format(self.name))
		print("My age is:{0}".format(self.age))

	def does():
		# 调用类的成员变量需要用 __class__
		print("My name is:{0}".format(__class__.name))
		print("My age is:{0}".format(__class__.age))
		print("Hello,world")

yueyue = Teacher()
yueyue.do()
#yueyue.does()
# 调用绑定类函数使用类名    does()里面没参数
Teacher.does()