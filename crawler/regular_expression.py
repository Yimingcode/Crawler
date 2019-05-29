# import re
# result = re.match('.', ', hi, python')
# print(result.group())
#
# ret = re.match("神州\d号","神州3号发射成功")
# print(ret.group())
#
# # 下面这个正则不能够匹配到数字4，因此ret为None
# ret = re.match("[0-35-9]Hello Python","4Hello Python")
# # print(ret.group())
#
# ret1 = re.match("[a-z]*[A-Z]?","mnnMJm")
# print(ret1.group())
#
# names = ["name1", "_name", "2_name", "__name__"]
#
# for name in names:
#     ret = re.match("[a-zA-Z_]+[\w]*", name)
#     if ret:
#         print("变量名 %s 符合要求" % ret.group())
#     else:
#         print("变量名 %s 非法" % name)

import sys
# n = int(input())
# ans = 0
# number_list = []
# for i in range(n):
#     line = input(
# print(line)
# dict1 = {}
# m = 0
# for c in line:
#     dict1[c] = m
#     m += 1
# for c in dict1.keys():
#     for i in dict1.keys():
#         if dict1[i] > dict1[c] and int(i) + int(c) + dict1[c] - dict1[i] >= ans:
#             ans = int(i) + int(c) + dict1[c] - dict1[i]
# print(ans)
# def numIslands(grid):
#     if not grid:
#         return None
#     m = len(grid)
#     if m == 0:
#         return 0
#     n = len(grid[0])
#     if n == 0:
#         return 0
#     res = 0
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == '1':
#                 res += 1
#                 intozero(grid, i, j)
#     return res
#
#
# def intozero(grid, i, j):
#     grid[i][j] = '0'
#
#     if i > 0 and grid[i - 1][j] == '1':
#         intozero(grid, i - 1, j)
#
#     if j > 0 and grid[i][j - 1] == '1':
#         intozero(grid, i, j - 1)
#
#     if i < len(grid) - 1 and grid[i + 1][j] == '1':
#         intozero(grid, i + 1, j)
#
#     if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
#         intozero(grid, i, j + 1)
#
# a = [
#     [1,1,1,0],
#     [1,0,0,0],
#     [1,0,0,1],
# ]
# print(len(a[0]))
# print(numIslands(a))

a = input()
num = int(a[0])
