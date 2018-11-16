from package1 import module_01  #不调用__init__里面的内容
#frome package1.module_01 import*   导入模块中的所有内容

stu = module_01.Student()
stu.speak()
module_01.talk()