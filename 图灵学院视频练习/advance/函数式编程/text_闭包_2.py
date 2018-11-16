def fun():
    def fun2(n):
        def g():
            return n*n
        return g
    fs = []
    for i in range(1,4):
        fs.append(fun2(i))
    return fs
f1, f2, f3 = fun()
print(f1(),"\n",f2(),"\n",f3())