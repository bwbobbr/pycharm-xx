# 自己组装一个类
class A():
	pass

def say(self):
	print("hello...")

class B():
	def say(self):
		print("hello...")

a = A()    # a的实例化
A.say =say   # 函数名当做变量名使用 相当于将say变成是A类中的一个方法
a.say()
print("-"*20)
b = B()
b.say()
