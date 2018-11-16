from types import MethodType

class A():
	pass

def say(self):
	print("hello...")

a = A()                         #实例化
a.say = MethodType(say,A)       #相当于指定say为 A类的方法
a.say()