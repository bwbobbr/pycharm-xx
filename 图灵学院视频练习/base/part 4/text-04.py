age = 17
if age<18:
	print('去叫家长吧，孩纸')
	print('我们不带你玩')
	print('滚球的')

age = 19
if age<18:
	print('去叫家长吧，孩纸')
	print('我们不带你玩')
	print('滚球的')
print('\n快上车')
print('今天学习for循环了')
gender='男'
if gender == '女':
	print('来，叔叔给你糖吃')
print('学习')
print('\n')
gender2=input('输入你的性别:')
'{0}'.format(gender2)  #format的用法 前面必须是字符串形式
if gender2=='man':
	print('练习写代码')
else:
	print('发糖吃')
print('\n')
#成绩的划分
#90优秀/80-90良/70-80中/60-70平/60差
score=input('输入学生的成绩：')
score = int(score)    #字符的转换 用于比较的是数字计算，所输入的是字符串，需要进行转化
print('分数：{0}'.format(score))
if score >= 90:
	print('优秀')
elif 80 <= score <90:  #第二种写法 score>=80 and score<=90
	print('良')
elif 70 <= score <80:
	print('中')
elif 60<= score <70:
	print('平')
elif score < 60:
	print('我没有你这种学生')