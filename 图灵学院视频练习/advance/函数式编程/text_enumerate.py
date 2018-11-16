# enumerate功能和zip类似
# 就是给所迭代的对象里,配上一个索引,然后索引和内容构建成tuple类型
l1 = [11,22,33,44,55]
em = enumerate(l1, start = 100)
print(type(em))
# for i in em:
#    print(i)      每行输出()形式
# 记住这个写法
l2 = [j for j in em]   # 输出形式[(),()]  类同zip当执行6,7,8语句时,该9,10语句输出为空[]
print(l2)