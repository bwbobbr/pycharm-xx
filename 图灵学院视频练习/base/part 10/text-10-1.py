##集合 {} 内容无序,不能索引和排序,排除重复值
s = {1,1,1,2,3,4}
print(s)                #过滤重复的元素
s1 = {(1,2,3),('I','love','you'),(4,5,6)}
for i, j, k in s1:
	print(i, '-', j, '-', k)
print('-'*20)
s2 = {1,1,2,3,4,5,2,1,2,3,4,5,222,12312,23124,354353,656,2272}
print(s2)
ss = {i for i in s2}
print(ss)
sss = {i for i in s2 if i % 2 == 0}  #类似于list函数[i for i in s if i % 2 == 0]
print(sss)                             #添加条件给予限制嵌套函数注意list是[],集合是用{}
print('-'*50)
s1 = {1,2,3,4}
s2 = {"i", "love", "wangxiaojing"}
s = {m*n for m in s2 for n in s1}
print(s)
s = {m*n for m in s2 for n in s1 if n == 2}
print(s)               #将s2里面的元素扩大s1里面的n倍