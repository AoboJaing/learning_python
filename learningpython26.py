# -!- coding: utf-8 -!-

# path = r'D:\WorkSpace\test_ws\Git(GitHub) 002 如何在GitHub For Windows 软件上为代码库创建一个版本标签 — Ongoing — 2016年12月1日 星期四\Git(GitHub) 002 如何在GitHub For Windows 软件上为代码库创建一个版本标签 — Ongoing — 2016年12月1日 星期四.md'
# delimiter = '\\'
#
# evernote_is_folder = True
# a = -1
# if evernote_is_folder:
#     a=-2
#
# mylist = path.split(delimiter)
# res = delimiter.join(mylist[:a])
# print(res)


path = r'D:\WorkSpace\test_ws\笔记\text.md'
delimiter = '\\'

mylist = path.split(delimiter)
res_path = delimiter.join(mylist[:-1])
res_path = res_path.decode('utf-8').encode('GB18030')
print(res_path)
