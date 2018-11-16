for i in range(1,100000000):
    for j in range(1,100000):
        if i + 100 == j*j:
            for k in range(1,1000000000):
                if i + 100 + 168 == k * k:
                    print(i)