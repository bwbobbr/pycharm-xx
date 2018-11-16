#字符串格式化符号
print('I love %s'%'you')
s = 'I love %s'
print (s%'wangmeili')
s='I am %d years old'
print (s % 18)
print("-"*70)
##方法一
s='I am %s , I am %s years old'
print(s%('bob',18))
##方法二--用format函数   用大括号标号和format函数来进行操作（常用法则）
s='I am {0},I am {1} years old,yes I am {0} and I am {1} years old.'
print (s.format('bob',18))
#运算符
print(9/4)
a=3**4
b=a==80
print (b)
#逻辑运算
a=2
b=3
print(a and b)
a=True
b=0
#a=a or (b=9) and 6 #短路案例，a=Ture后面不执行