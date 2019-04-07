import numpy as np
import random

# 使用numpy，生成ndarray的类型
t1 = np.array([1, 2, 3])
print(t1)
# t1的数据类型是numpy中数组类型
print(type(t1))

t2 = np.array(range(5))
print(t2)

t3 = np.arange(5)
# 可以看出t2和t3的输出效果一样，两种语法等价
print(t3)

t4 = np.arange(4, 10, 2)
# 和range的语法类似，可以设置始末值和步长
print(t4)
# 输出数组中元素的类型
print(t4.dtype)
print("+" * 50)

# 指定numpy中的数据类型
t5 = np.array(range(1, 4), dtype="float32")
print(t5)
print(t5.dtype)
t6 = np.array([1, 1, 0, 1, 0, 0], dtype="bool")
print(t6)
print(t6.dtype)

# 调整数据类型
t7 = t6.astype("int8")  # 数据类型转换
print(t7)
print(t7.dtype)

# numpy生成浮点数
t8 = np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)
print(round(3.24, 1))
print(random.uniform(0, 5))
# numpy中保留固定位数的小数
print(np.round(t8, 3))

# 数组（矩阵）,shape可以确定数组是几维的
s = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(s.shape)
s1 = np.array([[1, 2, 3], [4, 5, 6]])
print(s1.shape)
s2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(s2)
print(s2.shape)

# 修改数组的形状
s3 = np.reshape(s, (2, 4))  # reshape的修改维度必须是元祖形式
print(s3)
s4 = np.arange(24).reshape((2, 3, 4))  # (2, 3, 4)分别代表块数、行数、列数
print(s4)
print(s4.reshape((4, 6)))  # reshape并不会导致被重组数组本身变化
print(s4)
print(s4.reshape((24,)))
print(s4.reshape((1, 24)))  # 注意这两种输出不一样，第二个他的本质还是二维数组
# 在不清楚数组的元素个数的情况下将其转换成一维的,前提是你得知道维度,
# shape[num]中的num分别从0、1、2表示该维的数值
# print(s4.reshape((s4.shape[0] * s4.shape[1]) * s4.shape[2],))
# flatten不需要知道数组的行数和列数，直接转换成一维数组
print(s2.flatten())

