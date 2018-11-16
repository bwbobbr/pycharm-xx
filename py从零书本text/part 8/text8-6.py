# 封装:不用关心对象是如何构建的
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score =score

	def info(self):
		print("姓名:{0},分数:{1}".format(self.name,self.score))
		#print("姓名:%s ,分数:%s" % (self.name,self.score))
stu = Student("小明",99)
stu.info()