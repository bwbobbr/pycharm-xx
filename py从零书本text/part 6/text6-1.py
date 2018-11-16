student=['小明','小红','小芳','小李']
number=[1001,1002,1003,1004]
for i in range(len(student)):
	print(student[i],'的学号是:',number[i])
for i,j in zip(student,number):
	print(i,j)
a=sorted([5,6,7,2,1,9,11,0,32])
print(a)
print(list(reversed('asdasd')))
print(' '.join(reversed('adfafd')))
afd=sorted('hello,world!')
print(afd)