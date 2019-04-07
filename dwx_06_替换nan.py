import numpy as np


def fill_ndarray(t):
    for i in range(t.shape[1]):
        temp_col = t[:, i]  # 遍历当前一列
        nan_num = np.count_nonzero(temp_col != temp_col)  # 计算数组中nan的个数
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列中不为nan的元素
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  # 将当前列中不为nan的元素的平均值赋给nan
    return t


t1 = np.arange(12).reshape((3, 4)).astype("float")
t1[1, 2:] = np.nan
print(t1)
print(" " * 50)
print(fill_ndarray(t1))
