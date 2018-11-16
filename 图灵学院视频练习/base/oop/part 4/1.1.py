class Person():
	def __init__(self):
		self.name = "bob"

	def fget(self):
		print("读取了fget")
		return self._name     # 当变成print(self.name)时,会多一行None

	def fset(self,name):
		print("读取了fset")
		self._name = name + " 正在学习python"

	def fdel(self):
		pass

	name = property(fget,fset,fdel,"调用之")

yueyue = Person()
print(yueyue.name)

#遗留问题property用法还是很不明确????