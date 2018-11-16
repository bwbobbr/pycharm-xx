#元组
a = 1,
print(type(a))
print(a)
b = (1,2,3,4)
print(b[0])
print('*'*50)
#研究俩个list函数相加是新的一个地址,还是是在原来的list上进行修改
c1 = [1,2,3,4]
c2 = [5,6,7,8]
print(id(c1))
print(c1)
c1 += c1 + c2
print(c1)
print(id(c1))
#由此可见其最后的变化是发生在list原来的地址之上的
#借此来看看tuple的类似list的具体情况
print('-'*50)
c1 = (1,2,3,4)
c2 = (5,6,7,8)
print(id(c1))
print(c1)
c1 += c1 + c2
print(c1)
print(id(c1))
#发现tuple形式和list的不同最终地址发生了变化,说明是出现新地址并赋予新值
#tuple元组拥有list的所有功能,但是不能进行修改,更变
#ep:c1[0] = 100 就会报错

#双层嵌套的打印
a = ((1,2,3),(4,5,6),('i','j','k'))
for i in a:
	print(i)
for i, j, k in a:
	print(i, '-', j, '-', 'k')    #嵌套内的元素必须是一一对应的,有几个都是包含有几个
	                             #((1,2,3,4)(1,2,3)(5,6,7,8,9))将会报错