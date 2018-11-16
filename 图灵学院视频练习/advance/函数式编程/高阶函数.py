def fun1(n):
    return n * 100

def fun2(n):
    return fun1(n)*3
print(fun2(9))

def fun3(n, f):
    return f(n)*3
print(fun3(9, fun1))   # 这里传入的是一个函数 相当于f = fun1

def fun4(n):
    return n * 10
print(fun3(9,fun4))   # 扩大30倍