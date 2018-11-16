# 异常案例
# 给出提示信息
try:                              # 尝试某个操作, 可能会出现的代码
    num = int(input("Please input your number:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))

# 如果是多种error的情况
# 需要把越具体的错误, 往前面摆放
# 在异常类继承关系中, 越是子类的异常, 越要往前摆放
# 越是父类的异常, 越往后面摆放

# 在处理异常的时候,一旦拦截到某一个异常,则不会继续往下执行
# 代码之中有finally则执行finally语句, 不然则执行下一个大语句
except ZeroDivisionError as e:               # zerodivisionerror 相当于一个类.类的是实例化, 取自于异常中(异常属于一个类别)
    print("Error")                          # 第一个异常分类
    print(e)

except NameError as e:                      # 第二个异常分类
    print("名字起错了")
    print(e)

except AttributeError as e:                 # 第三个异常分类(至少要有一个except)
    print("属性问题")
    print(e)

# 借此可见上面3个类型都是取自某个父类之中
except Exception as e:            #父类型, 摆放在最后面, 用于拦截上述所归纳的类型中没出现的
    print("不清楚的类型")
    print(e)

except ValueError as e:        # valueerror 是exception的子类, 语句在exception之后,因此在执行过程之中不会执行
    print("NO~~~~~")

print("hahahahah")