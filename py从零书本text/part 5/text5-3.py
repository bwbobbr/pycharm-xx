student ={'小明':'1001','小红':'1002','小智':'1003','小芳':'1004'}
student['小红']='1005'
student['小张']='1006'
print ('各位学生的学号',student)
print ('小明的学号是:',student['小明'])
print ('小红的学号是：%(小红)s'%student)
x={}
y=x
x['key']='value'
print(y)
people=student
print(people)

seq=('abc','def','hij')
st=dict.fromkeys(seq)
print(st)