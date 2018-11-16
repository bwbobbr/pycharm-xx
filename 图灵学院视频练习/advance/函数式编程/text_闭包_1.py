def fun():
    fs = []
    for i in range(1,4):
        # 定义一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = fun()
print(f1(),"\n",f2(),"\n",f3())