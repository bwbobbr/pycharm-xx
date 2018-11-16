# zip案例
l1 = ["小美","小明","小王","小智"]
l2 = [11,22,33,44]
z = zip(l1,l2)
print(type(z))
# for i in z:
#     print(i)
# print("-"*100)

# 当上述三条语句已经执行,再来执行下述语句时,为空[]Why?
l3 = [i for i in z]
#for i in l3:
#    print(i)
print(l3)