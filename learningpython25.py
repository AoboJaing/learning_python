# -*- coding: utf-8 -*-

# path = r'D:\WorkSpace\test_ws\Git(GitHub) 002 如何在GitHub For Windows 软件上为代码库创建一个版本标签 — Ongoing — 2016年12月1日 星期四\Git(GitHub) 002 如何在GitHub For Windows 软件上为代码库创建一个版本标签 — Ongoing — 2016年12月1日 星期四.md'
# path2 = r'D:\WorkSpace\test_ws\Git(GitHub) 002 如何在GitHub For Windows 软件上为代码库创建一个版本标签 — Ongoing — 2016年12月1日 星期四.md'
#
# l1 = path.split('\\')
# # l1 = path2.split('\\')
# # print(l1)
# # print(l1[-1])
# print(l1[-2])
# l2 = l1[-1].split('.')
# # print(l2)
# print(l2[0])
#
# same = l1[-2]==l2[0]
# print(same)


str = r'D:\WorkSpace\test_ws\Git(GitHub)'
l = str.split('\\')
print(l)
print(str.split('\\', 1))