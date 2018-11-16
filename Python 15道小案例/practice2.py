a1,a2,a3,a4,a5,a6 = 0.1,0.075,0.05,0.03,0.015,0.01
profit = int(input("当月利润为："))
if profit <= 100000:
    money = profit * 0.1
elif profit > 100000 and profit <= 200000:
    money = 100000 * a1 + (profit -100000) * a2
elif profit > 200000 and profit <= 400000:
    money = 100000 * a1 + 100000 * a2 + (profit - 200000) * a3
elif profit > 400000 and profit <= 600000:
    money = 100000 * a1 + 100000 * a2 + 200000 * a3 +  (profit - 400000) * a4
elif profit > 600000 and profit <= 1000000:
    money = 100000 * a1 + 100000 * a2 + 200000 * a3 +  200000 * a4 + (profit - 600000) * a5
elif profit > 1000000:
    money = 100000 * a1 + 100000 * a2 + 200000 * a3 +  200000 * a4 + 400000 * a5 + (profit - 1000000) * a5
print(money)
# 写的真差劲！！！