import numpy as np
t = np.array(range(0, 18)).reshape((3, 6))
print(t)
print("*" * 50)
print(" " * 50)
# 以下三种方式都可以实现转置
print(t.transpose())
print("*" * 50)
print(" " * 50)
print(t.swapaxes(1, 0))
print("*" * 50)
print(" " * 50)
print(t.T)
