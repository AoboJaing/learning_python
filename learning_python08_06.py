# -!- coding:utf-8 -!-

import re

# Learning Python 008 正则表达式-007 匹配的字符串模板中如果只有前面有字符串，而后面没有字符串时，这个匹配模板要怎么写 --- 2017年2月20日 星期一
# 博文的链接地址：http://www.aobosir.com/blog/2017/02/21/python-regular-expression-match-string-no-string-in-behind/

# 这个程序的功能：获取'.\data\2017-2-19-3D-printer-hot-bed.markdown'文件里面所有的图片链接的地址。

# 这个demo 程序使用了两次正则表达式的方式，成功的将所有的图片链接地址都获取了出来。（其中有："![Alt text](./1485166773479.png)"这种形式的，还是"![Alt text | 240x0](./1485166756931.png)"这种形式的。）

file = open(r'.\data\2017-2-19-3D-printer-hot-bed.markdown', 'rt', encoding='utf-8')
data = file.read()
print(data)

image_local_path_step1 = re.findall('!\[Alt text(.*?)\)', data, re.S)
for i in range(len(image_local_path_step1)):
    print(image_local_path_step1[i])
    pass

for i in range(len(image_local_path_step1)):
    image_local_path_step1_this = image_local_path_step1[i]
    image_local_path_step2 = re.findall(']\((.*?)\Z', image_local_path_step1_this, re.S)
    print(image_local_path_step2[0])
    pass


file.close()

