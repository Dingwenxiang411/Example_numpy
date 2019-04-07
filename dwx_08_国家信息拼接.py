import numpy as np

us_data = "./US_video_data_numbers.csv"
uk_data = "./GB_video_data_numbers.csv"

# 加载国家数据，delimiter表示以"，"分割数据，类型选择为整数类型，否则输出为科学计数法
us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)

# 添加国家信息
# 构造全为0和全为1的数据
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)
# python理解的水平拼接就是数据放到右侧，竖直就是放到下侧
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接两组数据
print(np.vstack((us_data, uk_data)))
