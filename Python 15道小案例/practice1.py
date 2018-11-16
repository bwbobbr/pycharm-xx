sum = 0
for i in range(1,5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            a = [i,j, k]
            for n in range(0,3):
                for m in range(0,3):
                    for o in range(0,3):
                        if n != m and n!= o and m != o:
                            sum +=1
                            print(a[n],a[m],a[o])

#            sum += 6
#            print(i,j,k,"-",i,k,j,"-",j,i,k,"-",j,k,i,"-",k,i,j,"-",k,j,i)

print(sum)
# 多次一举，前5行是多余代码，直接用后面的思想就能直接得出答案