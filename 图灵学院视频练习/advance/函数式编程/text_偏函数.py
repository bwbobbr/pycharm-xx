import functools
int16 = functools.partial(int,base = 16)      #这就是偏函数 ,参数是固定的就是里面的base参数
a = int16("1234a")
print(a)

# 此函数所实现的功能就是如下的代码
# int 就是一个类 int(XXX . base = 10) 默认是十进制的
b = int("1234a",base = 16)
print(b)