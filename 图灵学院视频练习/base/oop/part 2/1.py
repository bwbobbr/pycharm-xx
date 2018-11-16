#继承的语法
class Person():                         # Person是父类
	name = "Noname"
	age = 18
	__score = 0
	_petname = "sec"

	def sleep(self):
		print("ZZZZZZ")

	def work(self):
		print("make some money")


class Teacher(Person):                  # Teacher是子类,其父类为Person
	teacher_id = "9527"
	name = "Dana"

	def make_text(self):
		print("attention")

	# 调用父类中的work函数
	def work(self):
		super().work()          # 方法二 Person.work(self)
		super().sleep()         # super代表从父类中调取函数
		self.make_text()

t = Teacher()
t.work()

print(type(super))