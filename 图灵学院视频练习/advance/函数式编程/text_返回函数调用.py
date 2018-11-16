def fun1( *args):
    def fun2():       # fun2 函数返回rst； fun1函数返回 函数fun2
        rst = 0
        for i in args:
            rst += i
        return rst
    return fun2

fun3 = fun1(1,2,3,4,5,6)
print(fun3())