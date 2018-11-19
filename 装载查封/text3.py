#OkStart函数用于计算三叉树
def OkStart():
    tables = excel_table_byname()
    nrows = len(tables)
    VCargo = 0
    for rownum in range(1, nrows):
        if (tables[rownum][1] >= tables[0][1]) == True:
            print(str(int(rownum))+"号物品的长大于集装箱长度，无法载入，运行终止。")
            break
        if (tables[rownum][2] >= tables[0][2]) == True:
            print(str(int(rownum))+"号物品的宽大于集装箱宽度，无法载入，运行终止。")
            break
        if (tables[rownum][3] >= tables[0][3]) == True:
            print(str(int(rownum))+"号物品的高大于集装箱高度，无法载入，运行终止。")
            break
        VCargo = VCargo + (int(tables[rownum][1])*int(tables[rownum][2])*int(tables[rownum][3]))
        if (VCargo >= (int(tables[0][1])*int(tables[0][2])*int(tables[0][3]))) == True:
            print("所载物品总体积大于集装箱体积，无法载入，运行终止。")
            break
    L = int(tables[0][1])
    W = int(tables[0][2])
    H = int(tables[0][3])
    EL = [[[0,0,0],L,W,H]]    #EmptyList = EL
    FL = []                   #FullList = FL
    LFP = []                  #List just For Plot = LFP
    for rownum in range(1, nrows):
        for i in range(0, len(EL)):
                if((int(EL[i][1]) == 0) or (int(EL[i][2]) == 0) or (int(EL[i][3]) == 0)):
                    del EL[i]
                if (((tables[rownum][1]*tables[rownum][2]) <= (EL[i][1]*EL[i][2])) and (tables[rownum][1] <= EL[i][1])
                and (tables[rownum][2] <= EL[i][2]) and (tables[rownum][3] <= EL[i][3])) == True:
                    temp0 = [str(int(rownum))+"号物品左前下角置于" + "("+str(EL[i][0][0]) +","+ str(EL[i][0][1]) +","+ str(EL[i][0][2])+")"]
                    FL = FL + temp0
                    temp00 = [[EL[i][0][0],EL[i][0][1],EL[i][0][2]],tables[rownum][1],tables[rownum][2],tables[rownum][3]]
                    LFP.append(temp00)
                    temp1 = [[(EL[i][0][0]+tables[rownum][1]),EL[i][0][1],EL[i][0][2]],(EL[i][1]-tables[rownum][1]),EL[i][2],EL[i][3]]
                    temp2 = [[EL[i][0][0],(EL[i][0][1]+tables[rownum][2]),EL[i][0][2]],tables[rownum][1],(EL[i][2]-tables[rownum][2]),EL[i][3]]
                    temp3 = [[EL[i][0][0],EL[i][0][1],(EL[i][0][2]+tables[rownum][3])],tables[rownum][1],tables[rownum][2],(EL[i][3]-tables[rownum][3])]
                    EL.append(temp1)
                    EL.append(temp2)
                    EL.append(temp3)
                    del EL[i]
                    EL = Rearrange(EL)
                    #print(FL)
                    break
                elif (((tables[rownum][1]*tables[rownum][2]) <= (EL[i][1]*EL[i][2])) and (tables[rownum][1] <= EL[i][2])
                and(tables[rownum][2] <= EL[i][1]) and (tables[rownum][3] <= EL[i][3])) == True:
                    temp0 = [str(int(rownum))+"号物品旋转90度后左前下角置于" + "("+str(EL[i][0][0]) +","+ str(EL[i][0][1]) +","+ str(EL[i][0][2])+")"]
                    FL = FL + temp0
                    temp00 = [[EL[i][0][0],EL[i][0][1],EL[i][0][2]],tables[rownum][2],tables[rownum][1],tables[rownum][3]]
                    LFP.append(temp00)
                    temp1 = [[(EL[i][0][0]+tables[rownum][2]),EL[i][0][1],EL[i][0][2]],(EL[i][1]-tables[rownum][2]),EL[i][2],EL[i][3]]
                    temp2 = [[EL[i][0][0],(EL[i][0][1]+tables[rownum][1]),EL[i][0][2]],tables[rownum][2],(EL[i][2]-tables[rownum][1]),EL[i][3]]
                    temp3 = [[EL[i][0][0],EL[i][0][1],(EL[i][0][2]+tables[rownum][3])],tables[rownum][2],tables[rownum][1],(EL[i][3]-tables[rownum][3])]
                    EL.append(temp1)
                    EL.append(temp2)
                    EL.append(temp3)
                    del EL[i]
                    EL = Rearrange(EL)
                    #print(FL)
                    break

    #return EL
    return LFP       #List just For Plot = LFP
    #return FL        #FullList