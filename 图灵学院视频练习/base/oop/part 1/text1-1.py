class A():    #A称之为类
	name = "dana"
	age = 18
	# 注意say的写法,参数由一个self,里面的self不是关键字
	def say(self):
		self.name = "aaa"
		self.age = 200

#此时,A称为类实例
print(A.name)
print(A.age)

print("-"*60)
#借由id来鉴别一个变量和另一个变量是不是为用一个地址
print(id(A.name))
print(id(A.age))

a = A()        # a称之为对象
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
#由此例子可以看出这是出自同一个地址的