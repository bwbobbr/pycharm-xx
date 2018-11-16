# 异常处理
try:                                                # 尝试某个操作, 可能会出现的代码
    num = int(input("please input number:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
except:                                             # 归类异常(第一个类别),可能不止一个
    print("程序出错!!!")
    #exit就是退出程序的意思
    exit()
'''
至少要有一个except 语句用于归类所出错的

else:
    XXXXX无异常时所执行的语句

finally:
    XXXXX有无异常都会执行的语句

else与finally 语句不一定有,可选择
'''
