#property函数的使用
class Fun1():
#  对名字进行调整
	def fget1(self):
		return self._name

	def fset1(self,name):           # 在修改的时候需要输入参数,不单单是唯一的一个参数self,还要输入其他的参数变量
		self._name = name.upper()   # 并且在使用函数property时,在类的方法定义只用,参数前面需要添加下划线****

	def fdel1(self):
		self._name = "None"
#   对年龄进行调整
	def fget2(self):
		return self._age

	def fset2(self,age):
		self._age = int(age)

	def fdel2(self):
		self._age = "None"

	name = property(fget1, fset1, fdel1, "对姓名的格式进行调整")      # 定义fget:获取类, fset:修改类, fdel:修改类
	age = property(fget2, fset2, fdel2, "对年龄进行调整")

yueyue = Fun1()
yueyue.name = "yueyue"
yueyue.age = 16.22
print(yueyue.name)
print(yueyue.age)
