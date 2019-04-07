import numpy as np
a = np.array(range(0, 12)).reshape((3, 4))
print(a)
print("*" * 50)
print(" " * 50)

# 取出数组的一行或者一列
print(a[0])
print(a[:, 2])
print("*" * 50)
print(" " * 50)

# 取出多行或者多列
print(a[1:3])  # 同样是一个前闭后开的区间
print(a[:, 2:4])
print(a[[0, 2]])  # 取不连续的多行，一定要用[]
print(a[0:2, 1:5])  # 去1到2行，2到4列之间交叉的元素
print("*" * 50)
print(" " * 50)

# 取出多个元素
print(a[[0, 2, 1], [0, 1, 3]])  # 取的元素的索引为（0，0）和（2，1）和（1，3）
print("*" * 50)
print(" " * 50)

# 数值的修改
a[:, 2:4] = 0
print(a)
# 对数组中满足一定条件的所有元素进行修改
a[a < 3] = 2
print(a)
# np.where(a <= 5, 1, 6)  # 如果这条语句之后再执行print(a)，a的值不会有变化 说明where不修改a的内容
print(np.where(a <= 5, 1, 6))  # 将a中<=5的替换成1，>5的替换成6
print(a.clip(4, 6))  # 将a小于4的替换成4，大于6的替换成6

# 将元素修改成nan（注意nan是一个float类型，而a是一个int类型）
a = a.astype(float)
a[0, 2] = np.nan
print(a)
