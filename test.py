# 作者:明月清风我
# 时间:2022/8/12 14:28
import numpy as np
# import time
from shapely.geometry import Polygon  # 多边形
# import scipy.io as io
#
#
# def Cal_area_2poly(data1, data2):
#     """
#     任意两个图形的相交面积的计算
#     :param data1: 当前物体
#     :param data2: 待比较的物体
#     :return: 当前物体与待比较的物体的面积交集
#     """
#
#     poly1 = Polygon(data1).convex_hull  # Polygon：多边形对象
#     poly2 = Polygon(data2).convex_hull
#
#     if not poly1.intersects(poly2):
#         inter_area = 0  # 如果两四边形不相交
#     else:
#         inter_area = poly1.intersection(poly2).area  # 相交面积
#     return inter_area
#
#
data1 = [[0.251201, 0.413986], [0.251162, 0.432383], [0.282256, 0.430981], [0.282085, 0.412531]]  # 带比较的第一个物体的顶点坐标
# data2 = [[0.251201, 0.413986], [0.251162, 0.432383], [0.282256, 0.430981], [0.282085, 0.412531]]  # 待比较的第二个物体的顶点坐标
# area = Cal_area_2poly(data1, data2)
print(Polygon(data1).convex_hull.area)
dataset_coord = []
dataset_coords = ['13 0.251201 0.413986 0.251162 0.432383 0.282256 0.430981 0.282085 0.412531']
a = np.zeros([2, 4])
a[0, 0] = 1
a[1, 1] = 2
a[0, 1] = 3
i = 0
print(dataset_coords[0].split()[1:9])
for index in range(len(dataset_coords)):
    dataset_coords[index] = [dataset_coords[index].split()[1:3],
                             dataset_coords[index].split()[3:5],
                             dataset_coords[index].split()[5:7],
                             dataset_coords[index].split()[7:9]]

a.tolist()
print(dataset_coords)
print(a[0, 1])
for i in range(5):
    print(i)
b = [[1, 2],
     [3, 4]]

print(a.argsort())
print(a)
print(divmod(np.argmax(a), a.shape[1]))
print(np.argmin(a, axis=0)) # 按每列求出最小值的索引
print(np.argmin(a, axis=1))
a[1, :] = 5
print(a.min())
d = {}
d['m'] = []
d['m'].append(1)
print(d)