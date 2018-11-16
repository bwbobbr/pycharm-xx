a = [1,2,3,4,5]
#方法1
b = []
for i in a:
	b.append(i)
print(b)
#方法2
c = a[:]
print(c)
#方法3
d = [i for i in a]
print(d)

'''
过滤列表
i for i in a
'''
print('*'*20)
a = [1,2,3,4,5]
b = [i*10 for i in a]        #对a列表中的数值都乘以10传到b列表之中
print(b)
print('-'*50)
a = [i for i in range(1,35)] #生成1-35的a列表
print(a)
b = [j for j in a if j % 2 == 0]  #列表中的数值为a列表数值中的偶数值
print(b)
print('-'*100)
a = [i for i in range(1,5)]
b = [j for j in range(1,600) if j %100 == 0]  #列表需要满足的条件有从1-600的数值中能被100整除的组成列表b
print(a)
print(b)
c = [i +j for i in a for j in b]
d = [i +j for i in a for j in b if i+j < 400 ]  #多个循环和条件要求上的多重嵌套
print(c)
print(d)