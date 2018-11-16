# 二维图像单图像生成曲线
import matplotlib.pyplot as plt
import numpy as np
#help(np.arange)

t = np.arange(0.0,2.0,0.01)  # x轴的坐标
s = np.sin(2*np.pi*t)   # y轴上的值绘制sin函数
plt.plot(t,s)         # plot(x,y坐标)
help(plt.plot)

plt.grid(True)  #生成网格

#plt.show()