# reduce 归并，缩减
from functools import reduce
def fun(x,y):
    return x + y
a = reduce(fun,[1,2,3,4,5,6])   # reduce(functiom, list(参数))
# reduce([1,2,3,4,5,6]) == f(f(f(f(f(1,2),3),4),5),6)
print(a)