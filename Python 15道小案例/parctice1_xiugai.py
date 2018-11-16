sum = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                sum += 1
                print(i,j,k)