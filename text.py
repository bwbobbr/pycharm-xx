class Student():

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def info(self):
		print("name:",self.__name,"score:",self.__score)

	def score(self):
		return self.__score


		if 0 <= score <= 100:
			self.__score = score
		else:
			print("请输入0-100的数值")


stu = Student("小美",98)
#print("修改前的score:",stu.get_score())
print("修改分数之前:",stu.score())
stu.info()
#stu.set_score(-10)