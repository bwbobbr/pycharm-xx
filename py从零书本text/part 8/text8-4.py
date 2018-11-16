class Student(object):
	def __init__(self):
		pass

	def __foo(self):
		print("这是私有方法")

	def foo(self):
		print("这是共有方法")
		print("共有方法调用私有方法")
		self.__foo()
		print("公共方法调用私有方法结束")


sb = Student()
sb.foo()
#sb.__foo     # 外部调用时会直接报错