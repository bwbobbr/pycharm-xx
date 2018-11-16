x = 100
y = 200
z1 = x+y
z2 =eval('x+y')

print(z1)
print(z2)
print('*'*20)

z3=exec('x+y')
print(z3)
print('-'*20)

z4=exec('print("x+y=",x+y)')   #比较z3与z4发现输出的有所不同
print(z4)