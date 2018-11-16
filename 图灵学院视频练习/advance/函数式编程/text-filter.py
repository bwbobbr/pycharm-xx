# filter案例
# 对一个列表进行过滤，留下偶数，生成新列表
def fun(n):      # 定义的函数返回的是布尔值
    return n % 2 == 0
l = [1,2,3,4,5,6,7,8,9,11,23,22,34,213,123,4,124,52]  # 数据是一个可迭代对象
rst = filter(fun,l)
print(rst)
print([i for i in rst])