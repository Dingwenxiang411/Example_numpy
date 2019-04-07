import numpy as np

t = np.arange(12).reshape((2, 6))
t1 = np.arange(12, 24).reshape((2, 6))
print(t)
print(t1)
# 竖直拼接
print(np.vstack((t, t1)))
# 水平拼接
print(np.hstack((t, t1)))
print(" " * 50)
print("*" * 50)

# 行交换
t[[0, 1], :] = t[[1, 0], :]
print(t)
# 列交换
t[:, [1, 4]] = t[:, [4, 1]]
print(t)
