#获取表格数据
import xlrd
def open_excel(file= 'file.xls'):
   # try:
        data = xlrd.open_workbook(file)
        return data
   # except Exception as e:
    #    print(str(e))

#excel_table_byname函数用于打开excel文件 return list
def excel_table_byname(file= r'C:\Users\baoyu\Desktop\装载问题测试1.xls',
                                 colnameindex = 0,
                                 by_name = 'Sheet2'):
                            #输入表格文件路径|第一行为表头|Sheet2
     data = open_excel(file)
                            #'''将整个文件放入data'''
     table = data.sheet_by_name(by_name) # 获得表格  '''获得表格2的数据放入table'''
     nrows = table.nrows  # 拿到总共行数    '''表二的总行数放入2, nrows = 23'''
     colnames = table.row_values(colnameindex)  # print = ['序号', '长', '宽','高']
     list = []      # '''一个空的列表list'''
     #global a
     #print(nrows)
    # print(len(colnames))
    #循环23次
     for rownum in range(1, nrows): #也就是从Excel第二行开始，第一行表头不算 '''rownum用于读取的参数'''
         row = table.row_values(rownum)  # row是一个列表 每一行的数据都变成列表的形式存放
         #print(type(row))
        # print(row)
        # print("*"*100)
        # a += 1      #循环22次
         app = []  #一个空的app列表
         for i in row:
             app.append(int(i))

         #for i in range(0,len(colnames)):    #0-4    # 每层双重数据,重复数据？？
         #    app.append(int(row[i]))
         list.append(app)
     return list


def Rearrange(ELRearrange):  # EL表格数据重排   ELrearrange = EL 即是装载这一个物体之后的所重新划分的三个剩余空间
#global EmptyTemp
	EmptyTemp = ELRearrange   # len(EmptyTemp) = 3

	for m in range(0, len(EmptyTemp)):   # 0 -- 3 共三次
		for n in range(1, len(EmptyTemp)):    # 第一步--将定位坐标 X:长度按照从小到大排序  || 三个数排序只需要进行两次
			if (EmptyTemp[n - 1][0][0] >= EmptyTemp[n][0][0]):   ##定位坐标的 x:长度,重新排序
				temp = EmptyTemp[n - 1]        ## 将定位坐标中 x:长度,较大的存放到temp中
				EmptyTemp[n - 1] = EmptyTemp[n]
				EmptyTemp[n] = temp

	for m in range(0, len(EmptyTemp)):
		for n in range(1, len(EmptyTemp)):   #  第二部--在满足第一步的前提下将定位坐标 Y:宽度 按照从小到大排序||同理第一步
			if (((EmptyTemp[n - 1][0][0]) >= (EmptyTemp[n][0][0])) and (
					(EmptyTemp[n - 1][0][1]) >= (EmptyTemp[n][0][1]))):
				temp = EmptyTemp[n - 1]
				EmptyTemp[n - 1] = EmptyTemp[n]
				EmptyTemp[n] = temp

	for m in range(0, len(EmptyTemp)):
		for n in range(1, len(EmptyTemp)):   # 第三部--在满足第一步和第二步的前提下,对定位坐标Z:高度进行排序
			if (((EmptyTemp[n - 1][0][0]) >= (EmptyTemp[n][0][0])) and (
					(EmptyTemp[n - 1][0][1]) >= (EmptyTemp[n][0][1]))
					and ((EmptyTemp[n - 1][0][2]) >= (EmptyTemp[n][0][2]))):
				temp = EmptyTemp[n - 1]
				EmptyTemp[n - 1] = EmptyTemp[n]
				EmptyTemp[n] = temp

# XYZ按照大小进行排序
# 猜测是多个物体摆放之后所需要考略的内容---未解决√ 剩余空间合并（空间可以合并时的情况）怪怪的
	for m in range(0, len(ELRearrange)):  # len(ELRearrange) = 3  3次循环   就是EL
		for n in range(1, len(EmptyTemp)):
			if ((int(EmptyTemp[n - 1][0][1]) == int(EmptyTemp[n][0][1])) and (    # Y，Z + W长度
					int(EmptyTemp[n - 1][0][2]) == int(EmptyTemp[n][0][2]))
					and (int(EmptyTemp[n - 1][2]) == int(EmptyTemp[n][2]))):  # 条件够了么？z方向的高度
				temp0 = []
				temp0 = [
					[EmptyTemp[n - 1][0][0], EmptyTemp[n - 1][0][1], EmptyTemp[n - 1][0][2]],
					EmptyTemp[n - 1][1] + EmptyTemp[m][1], EmptyTemp[n - 1][2], EmptyTemp[n - 1][3]]  # 其假设z上高度相同？
                # 已经进行排序min又存在的必要么？？？一定是前面的小或者相同----->删除了min
				# 当两块剩余空间满足条件时,将其合并成一个空间temp0  基于X轴:长度上空间剩余的合并
				EmptyTemp.append(temp0)
				del EmptyTemp[n - 1]
				del EmptyTemp[n]
				break # 此时的m已进行合并跳出
			if ((int(EmptyTemp[n - 1][0][0]) == int(EmptyTemp[n][0][0])) and (
					int(EmptyTemp[n - 1][0][2]) == int(EmptyTemp[n][0][2]))
					and (int(EmptyTemp[n - 1][1]) == int(EmptyTemp[n][1]))):   # X,Z + L长度
				temp0 = []
				temp0 = [
					[EmptyTemp[n - 1][0][0], min(EmptyTemp[n - 1][0][1], EmptyTemp[n][0][1]), EmptyTemp[n - 1][0][2]],
					EmptyTemp[n - 1][1],EmptyTemp[n - 1][2] + EmptyTemp[n][2], EmptyTemp[n - 1][3]]
				# 基于 Y轴:宽度上空间剩余的合并
				EmptyTemp.append(temp0)   # 添加在最后面跟对于之前的数据不会有影响,便于删除
			#	EmptyTemp.append(temp0)     # 有疑问问什么会有俩个??append 删除后其输出量不会改变
				del EmptyTemp[n - 1]
				del EmptyTemp[n]           # 疑问不用考虑第三种情况么，Y方向的？？
				break
	# EmptyTemp 1.如果进行过合并那么为两个空间  2.没合并就是3个空间??凑出来的值   进一步排序按照底面积大小排序（原因）？ 第二部操作
	for m in range(0, len(EmptyTemp)):  # 三个空间排序
		for n in range(1, len(EmptyTemp)):  # 将 剩余空间按 长*宽计算 将较大的空间摆放在下面 底面XOY面先放
			if ((int(EmptyTemp[n][1]) * int(EmptyTemp[n][2])) <= (int(EmptyTemp[n - 1][1]) * int(EmptyTemp[n - 1][2]))):
				temp4 = EmptyTemp[n - 1]
				EmptyTemp[n - 1] = EmptyTemp[n]
				EmptyTemp[n] = temp4

	return EmptyTemp

#OkStart函数用于计算三叉树
def OkStart():
    global EL
    tables = excel_table_byname()    # 此函数调用之后就是 tables = list ,list就是函数返回的列表值,list是二次嵌套列表
    nrows = len(tables)              # nrows = 22  数组个数 从1-22
   # VCargo = 0                       # 局部变量
    for rownum in range(1, nrows):   # 循环 1-22 总计21个,第一个为车厢大小,就是比较值  for循环:验证单个物体能满足放入空车子里面(以4个要素来判断长宽高+体积)
        if (tables[rownum][1] >= tables[0][1]) == True:
            print(str(int(rownum))+"号物品的长大于集装箱长度，无法载入，运行终止。")
            break
        if (tables[rownum][2] >= tables[0][2]) == True:
            print(str(int(rownum))+"号物品的宽大于集装箱宽度，无法载入，运行终止。")
            break
        if (tables[rownum][3] >= tables[0][3]) == True:
            print(str(int(rownum))+"号物品的高大于集装箱高度，无法载入，运行终止。")
            break
       #  VCargo = VCargo + (int(tables[rownum][1])*int(tables[rownum][2])*int(tables[rownum][3]))  # VCargo是物体的体积  (感觉多余代码删除)
       # if (VCargo >= (int(tables[0][1])*int(tables[0][2])*int(tables[0][3]))) == True:        # 用于判断某个物体没用充满整个车厢
          #  print("所载物品总体积大于集装箱体积，无法载入，运行终止。")
        #    break
    L = int(tables[0][1])           #   空车时     L:长  , W:宽  , H:高
    W = int(tables[0][2])
    H = int(tables[0][3])
    EL = [[[0,0,0],L,W,H]]   #EmptyList = EL
    FL = []                   #FullList = FL
    LFP = []                  #List just For Plot = LFP
    #print(len(EL))
    for rownum in range(1, nrows):   # nrows = 22  1-22
        for i in range(0, len(EL)):   #len(EL) = 1
                if(EL[i][1] == 0 or EL[i][2] == 0 or EL[i][3] == 0):  # 验证剩余空间中的W,H,L不等于零
                    del EL[i]
                if ((tables[rownum][1] <= EL[i][1]) and (tables[rownum][2] <= EL[i][2]) and (tables[rownum][3] <= EL[i][3])) == True:
					# 需要满足的4个条件 ——————>此处删除了底面积的限制(tables[rownum][1]*tables[rownum][2]) <= (EL[i][1]*EL[i][2])
	                # 1.物体的长*宽 <= 车厢的长*宽
	                # 2.物体的长 <= 剩余空间的长
	                # 3.物体的宽 <= 剩余空间的宽
	                # 4.物体的高 <= 剩余空间的高
                    temp0 = [str(int(rownum))+"号物品左前下角置于" + "("+str(EL[i][0][0]) +","+ str(EL[i][0][1]) +","+ str(EL[i][0][2])+")"]
					# ['X 号物品左前下角置于(a,b,c)']    第一个物体以(0,0,0)未开始起点   开始放物体
					# rownum = 1-22(总物体)       i = 0, 1
                    FL = FL + temp0       # 将列表['XX']放入FL
                    temp00 = [[EL[i][0][0],EL[i][0][1],EL[i][0][2]],tables[rownum][1],tables[rownum][2],tables[rownum][3]]
                    # 新listtemp00 = [[0,0,0],600,300,200]
					# tables : 指的是物体的长宽高占位  temp00 物体所占的空间
                    LFP.append(temp00)
					# 将物体数据存入新表LFP

					# temp1,2,3:将一个物体放入车厢之后.人为的划分成三个空间的剩余空间有列表表示出来  第二次之后要用排序之后的第一空间去减
                    temp1 = [[(EL[i][0][0]+tables[rownum][1]),EL[i][0][1],EL[i][0][2]],(EL[i][1]-tables[rownum][1]),EL[i][2],EL[i][3]]
                    # temp = [[x1,y1,z1],x2,y2,z2]形式      [x1,y1,z1]:目的是确定定位点  x2,y2,z2是对于剩余空间的划分1/6中自选一种
					# x1:物体的长度+0                  x2: 空余的长度即车厢长度(15000)-第一个物体的长度(600)
					# y1:0                            y2: 车厢的宽度
					# z1:0                            z2: 车厢的高度
					#定位点给予x轴变换,即是长度上的
                    temp2 = [[EL[i][0][0],(EL[i][0][1]+tables[rownum][2]),EL[i][0][2]],tables[rownum][1],(EL[i][2]-tables[rownum][2]),EL[i][3]]
					# 定位点考虑在宽度上
                    temp3 = [[EL[i][0][0],EL[i][0][1],(EL[i][0][2]+tables[rownum][3])],tables[rownum][1],tables[rownum][2],(EL[i][3]-tables[rownum][3])]
					# 定位点考虑在高度上

                    EL.append(temp1)
                    EL.append(temp2)
                    EL.append(temp3)
					# 将由此生成的新的三个空间存入EL剩余空间里面,放在末端   len(EL) = 4 ，第一轮之后要排除XYZ方向为0的划分空间
                    del EL[i]
					# 打碎原有空间,一分为三   len(EL) = 3


                    EL = Rearrange(EL)  # 返回 EL = EmptyTemp 就是对剩余空间的重新排列其中len = 2 or 3
                    #print(FL)
                    break
        '''
                elif (((tables[rownum][1]*tables[rownum][2]) <= (EL[i][1]*EL[i][2])) and (tables[rownum][1] <= EL[i][2])
                and(tables[rownum][2] <= EL[i][1]) and (tables[rownum][3] <= EL[i][3])) == True:
	                # 与前面的if一致 出发点是当竖着放不下是就横过来放
                    temp0 = [str(int(rownum))+"号物品旋转90度后左前下角置于" + "("+str(EL[i][0][0]) +","+ str(EL[i][0][1]) +","+ str(EL[i][0][2])+")"]
	                # 一致
                    FL = FL + temp0
                    temp00 = [[EL[i][0][0],EL[i][0][1],EL[i][0][2]],tables[rownum][2],tables[rownum][1],tables[rownum][3]]
	                # 长宽换位的放入其中
                    LFP.append(temp00)
                    temp1 = [[(EL[i][0][0]+tables[rownum][2]),EL[i][0][1],EL[i][0][2]],(EL[i][1]-tables[rownum][2]),EL[i][2],EL[i][3]]
                    temp2 = [[EL[i][0][0],(EL[i][0][1]+tables[rownum][1]),EL[i][0][2]],tables[rownum][2],(EL[i][2]-tables[rownum][1]),EL[i][3]]
                    temp3 = [[EL[i][0][0],EL[i][0][1],(EL[i][0][2]+tables[rownum][3])],tables[rownum][2],tables[rownum][1],(EL[i][3]-tables[rownum][3])]
	                # 对剩余空间的划分
                    EL.append(temp1)
                    EL.append(temp2)
                    EL.append(temp3)
                    del EL[i]
                    EL = Rearrange(EL)
                    #print(FL)
                    break
'''

    #return EL
    return LFP       #List just For Plot = LFP
    #return FL        #FullList


# EasyWatch函数用于给出装载顺序，为工人服务
def EasyWatch(LFP):       # 将tables传入 ,LFP = OkStart所返回的物体放入时的位置列表
	LFP = LFP
	for i in range(0, len(LFP)):   # len(LFP) = 21
		a = int(i + 1)
		LFP[i].append(a)          # 按顺序表即物体1-21标记
	for m in range(0, len(LFP)):   # 多余???
		for n in range(4, len(LFP)):   # 排序 4-21 按照物体的定位坐标 X: 长度有小到大排序
			if (LFP[n - 1][0][0] >= LFP[n][0][0]):
				temp = LFP[n - 1]
				LFP[n - 1] = LFP[n]
				LFP[n] = temp

	for m in range(0, len(LFP)):
		for n in range(4, len(LFP)):   # 在满足1的条件下在对Y进行排序
			if (((LFP[n - 1][0][0]) >= (LFP[n][0][0])) and ((LFP[n - 1][0][1]) >= (LFP[n][0][1]))):
				temp = LFP[n - 1]
				LFP[n - 1] = LFP[n]
				LFP[n] = temp

	for m in range(0, len(LFP)):
		for n in range(4, len(LFP)):  # 在满足1,2的条件下对Z进行排序
			if (((LFP[n - 1][0][0]) >= (LFP[n][0][0])) and ((LFP[n - 1][0][1]) >= (LFP[n][0][1])) and (
					(LFP[n - 1][0][2]) >= (LFP[n][0][2]))):
				temp = LFP[n - 1]
				LFP[n - 1] = LFP[n]
				LFP[n] = temp
	return LFP

#EasyWatch的文字输出版本，用文字列表输出EasyWatch
def EasyWord(LFP):
    LFP = EasyWatch(LFP)        # 就是简单的EasyWatch标记之后所返回的list,在对其进行赋值给LFP
    tables = excel_table_byname()    # 打开list列表
    FL = []
    for row in range(0,len(LFP)):    # len(LFP)=21
        if((tables[LFP[row][4]][1]) == (LFP[row][1])):
	        #  EasyWatch中的标号      物体的长度
            temp0 = [str(int(LFP[row][4]))+"号物品左前下角置于" + "("+str(LFP[row][0][0]) +","+ str(LFP[row][0][1]) +","+ str(LFP[row][0][2])+")"]
            #  ['几号物品左前角置于(X,Y,Z)']   (X,Y,Z)就是物体的定位坐标
            FL = FL + temp0
        elif((tables[LFP[row][4]][1]) != (LFP[row][1])):
            temp0 = [str(int(LFP[row][4]))+"号物品旋转90度后左前下角置于" + "("+str(LFP[row][0][0]) +","
                         + str(LFP[row][0][1]) +","+ str(LFP[row][0][2])+")"]
            FL = FL + temp0
    return FL

#列表调用的验证----已完成
print(excel_table_byname())   # 以列表的形式输出了sheet2
#print(a)


print("--"*300)
#三叉树验证---完成至Rearrange函数调取之中
#OkStart()
# Rearrange函数验证完毕,单不是非常的明确


#main函数 用于启动的主函数
def main():
    #输出结果文字版本
    tables = OkStart()   # 物体放入的列表
    tables = EasyWatch(tables)
    #print(tables)
    for row in tables:
        print(row)
    print(len(tables))

    # 画图输出
    import numpy as np
    import mpl_toolkits.mplot3d
    import matplotlib.pyplot as plt
    import random
    tables = OkStart()
    tables = EasyWatch(tables)

    # 用于撑开空间
    Homelist = excel_table_byname()
    L = int(Homelist[0][1])
    W = int(Homelist[0][2])
    H = int(Homelist[0][3])
    tables.insert(0, [[0, 0, 0], L, W, H, 0])
    print(tables)

    # 用于画图
    ax = plt.subplot(111, projection='3d')
    for row in range(0, len(tables)):
        point = tables[row][0]
        size = [tables[row][1], tables[row][2], tables[row][3]]
        # color=plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
        if (row <= 0):
            color = "black"
        else:
            color = ["red", "orange", "black", "green", "cyan", "blue", "violet", "indianred", "darkorange",
                     "yellowgreen"]
            color = color[row % 2]
        ax.plot((point[0], point[0]), (point[1], point[1]), (point[2], point[2] + size[2]), color=color)  # 1 1-2
        ax.plot((point[0], point[0] + size[0]), (point[1], point[1]), (point[2], point[2]), color=color)  # 2 1-3
        # ax.plot((point[0],point[0]),(point[1],point[1]+size[1]),(point[2],point[2]),color=color)#3 1-5
        ax.plot((point[0], point[0] + size[0]), (point[1], point[1]), (point[2] + size[2], point[2] + size[2]),
                color=color)  # 4 2-4
        ax.plot((point[0], point[0]), (point[1], point[1] + size[1]), (point[2] + size[2], point[2] + size[2]),
                color=color)  # 5 2-6
        ax.plot((point[0] + size[0], point[0] + size[0]), (point[1], point[1]), (point[2], point[2] + size[2]),
                color=color)  # 6 3-4
        ax.plot((point[0] + size[0], point[0] + size[0]), (point[1], point[1] + size[1]), (point[2], point[2]),
                color=color)  # 7 3-7
        ax.plot((point[0] + size[0], point[0] + size[0]), (point[1], point[1] + size[1]),
                (point[2] + size[2], point[2] + size[2]), color=color)  # 8 4-8
        # ax.plot((point[0],point[0]),(point[1]+size[1],point[1]+size[1]),(point[2],point[2]+size[2]),color=color[row % 10])#9 5-6
        # ax.plot((point[0],point[0]+size[0]),(point[1]+size[1],point[1]+size[1]),(point[2],point[2]),color=color[row % 10])#10 5-7
        ax.plot((point[0], point[0] + size[0]), (point[1] + size[1], point[1] + size[1]),
                (point[2] + size[2], point[2] + size[2]), color=color)  # 11 6-8
        ax.plot((point[0] + size[0], point[0] + size[0]), (point[1] + size[1], point[1] + size[1]),
                (point[2], point[2] + size[2]), color=color)  # 12 7-8
        ax.set_zlabel('H')
        ax.set_ylabel('W')
        ax.set_xlabel('L')
        # 中间被注解的三行为物体背面的三条线
        # if(row == 10):
        plt.savefig(str(int(row) + 1) + ".png")
    plt.show()


if __name__ == '__main__':
	main()

'''
1.运行OkStart函数, 调取sheet2变成列表  返回 list列表 且将list列表赋值给tables参数
2.按照OkStart函数将货物装箱      返回 LFP:表示物体所占的位置[[x1,y1,z1],x2,y2,z2]表示
      [[x1,y1,z1],x2,y2,z2]来定位
	1)Rearrange函数对剩余空间进行新的规划,空间合并   返回EmptyTemp列表
	2)EasyWatch函数  就是给物体放入时的顺序标记
	3)EasyWord函数

'''


