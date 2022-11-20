a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a_list[1])
# [4, 5, 6]

print(a_list[1][1])
# 5

for row in a_list:
  i = 0

  while i < len(row):
    print(row[i])
    i += 1
"""
1
2
3
4
5
6
7
8
9
"""

for x in a_list:
  print(x)
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
"""

for y in a_list:
  count = len(y)
  print(count)
"""
3
3
3
"""