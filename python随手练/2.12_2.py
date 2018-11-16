n = input("n = ")
if int(n) > 1:
    cost_one = 24.95*0.6+3
    sum = cost_one*int(n) + 0.75*int(n)
    print(sum)
else:
    print(24.95*0.6+3)