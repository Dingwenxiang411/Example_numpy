import numpy as np
t = np.arange(0, 24).reshape(4, 6)
print(t)
print(" " * 50)
t = t.astype(float)
t[3, 3:] = np.nan
print(t)
print(" " * 50)
t[:, 0] = 0
print(t)
print(" " * 50)
# 输出t中不等于0的元素个数
print(np.count_nonzero(t))
print(" " * 50)
# 利用np.nan!=np.nan的特性，找出nan的元素个数
print(np.count_nonzero(t != t))
print(t[t == t])
# # 下面这种判断形式也可以找出nan的个数
# print(np.isnan(t))
# print(np.count_nonzero(np.isnan(t)))
# print(" " * 50)
#
#
# # nan和任何数做运算都是nan
# print(np.sum(t))
# t1 = np.arange(12).reshape((3, 4))
# print(np.sum(t1, axis=0))  # axis=0计算的是行上的求和，即每一列的元素和
# print(np.sum(t1, axis=1))  # axis=1计算的是列上的求和，即每一行的元素和
# print(np.sum(t, axis=0))
