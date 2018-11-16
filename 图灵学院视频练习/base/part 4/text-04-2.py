for name in ['小张','小李','小王']:
	if name == '小王':
		print('I love %s'%name)
	else:
		print('{0}滚犊子'.format(name))

for i in range(1,11):
	print(i)
#continue的用法
for k in range(1,11):
	if k%2==1:
		continue
	else:
		print('%s是偶数'%k)
print('\n')
for i in range(1,11):
	if i%2 == 1:
		continue
	print('偶数{0}'.format(i))
#break的用法
for j in range(1,11):
	if j==5:
		print('找到值%s了'%j)
		break