class Student(object):

	def __init__(self,name,score):
		self.__name = name                     # 类属性的私人调用
		self.__score = score

	def info(self):
		print("name:%s,score:%s" % (self.__name,self.__score))

	def get_score(self):                       # 貌似不一定要用get_score函数,经试验发现其他定义的函数也能实现该过程???
		return self.__score

	def set_score(self,score):      # (有俩个,定义是要有一个参数)
		if 0 <= score <= 100:
			self.__score = score
		else:
			print("请输入0-100的数值")


stu = Student("小美",98)
#print("修改前的score:",stu.get_score())
print("修改分数之前:",stu.get_score())
stu.info()
stu.set_score(88)
print("修改分数之后:",stu.get_score())
stu.info()