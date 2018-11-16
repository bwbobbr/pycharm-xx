#append,在末尾添加一个内容
a = [i for i in range(1,5)]
print(a)
a.append(50)
print(a)
print('*'*50)
# insert(index,data), 在某个位置添加内容
a.insert(3,666)
print(a)
print('--'*20)
#del 删除
#pop,从对位拿出一个元素,即默认是将最后一个元素取出来
b = a.pop(2)
print(a)
print(b)
print('--'*20)
#remove(data)删除指定的元素,仅移除第一个值
a.append(1)
print(a)
print(id(a))
a.remove(1)
print(a)
print(id(a))
print('--'*20)
# clear():清空内容
a.clear()
print(a)
#只是单纯的想清空列表其他方法但是地址会发生变化
#a = []
#a = list []
print(id(a))
a= []
print(id(a))
print('*'*20)
#reverse:翻转列表的内容,原地翻转
a = [1,2,3,4,5]
print(a)
a.reverse()
print(a)
#extend 将两个列表合并,第二个接在第一个后面
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)
print('-'*50)
#count:计数,查找列表中某元素的个数
a.append(666)
a.insert(1,666)   #前面的index的位置从0计数开始的
print(a)
a_666_number = a.count(666)
print(a_666_number)
print('*'*66)
# copy拷贝,浅拷贝 就是开辟新的空间从而拷贝到另一个list之中
#简而言之就是发生了地址的变化,不是同一个list
a = [1,2,3,4,5,6]
print(a)
b = a
b[2] = 666
print(id(a))
print(id(b))
print(b)
print(a)       #由此看出a,b 是同一个地址 b发生变化,从而a也发生变化
print('-'*20)
print(a)
print(id(a))
b = a.copy()
b[1] = 777
print(b)
print(id(b))
print('*'*20)
#嵌套列表的copy有所不同
#浅拷贝和深拷贝
a = [1,2,3,[4,5,6]]
b = a.copy()
print(id(a))
print(id(b))
b [3][0] = 666
print(a)
print(b)
print(id(a[3]))
print(id(b[3]))   #由此可以看出深层次的列表嵌套里面的地址是同一个的