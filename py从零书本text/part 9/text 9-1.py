def fun(a,b):
    try:
        d = age  # 若是3,4行位置互换则except发生的不一样
        c = a/b
        return c
    #except ZeroDivisionError as e:
    #    print(e)     # 输出e称之为捕捉对象

    #except NameError as e:
    #    print(e)

    except (ZeroDivisionError,NameError) as e:
        print(e)

fun(1,0)
