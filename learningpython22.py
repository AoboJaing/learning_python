# -*- coding: utf-8 -*-

import os

org_folder = r'F:\原文件夹'
res_folder = r'F:\目标文件夹'

# 构造命令字符串
copy_command = 'copy "' + org_folder + r'\*" "' + res_folder + r'\"'
copy_command = copy_command.decode('utf-8').encode('GB18030')
print(copy_command)
# 使用os.system()函数执行命令字符串
os.system(copy_command)