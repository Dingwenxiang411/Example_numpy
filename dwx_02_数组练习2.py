import numpy as np

t1 = np.arange(24).reshape((4, 6))
print(t1)
print("*" * 50)
# 加减乘除都一样，都会让所有元素进行运算
print(t1 + 5)
print("*" * 50)
# 会让其和对应的所有行向量或者列向量进行运算
t2 = np.arange(6)
print(t1 - t2)
print("*" * 50)
t3 = np.arange(4).reshape((4, 1))
print(t1 - t3)
