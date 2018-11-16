number=88
i=input('输入的数值：')
i=int(i)
j=0
while True:
	if i <88:
		print('数值过小')
		j+=1
	elif i> 88:
		print('数值过大')
		j+=1
	else:
		j+=1
		break
	i=input('再次输入值：')
	i=int(i)
print('恭喜猜对了就是%d'%number)
print('所用的次数：%d'%j)