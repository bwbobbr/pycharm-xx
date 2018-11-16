profit = int(input("请输入利润:"))
money = 0
a = [1000000,600000,400000,200000,100000,0]
b = [0.01,0.015,0.03,0.05,0.075,0.1]
for i in range(0,len(a)):
    if profit > a[i]:
        money += (profit-a[i]) * b[i]
        profit = a[i]

print(money)