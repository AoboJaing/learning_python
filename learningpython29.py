import re

str = 'fdfgdrthxxi--gdfgexxlove--dsdfwesdxxyou--dfgdf'
pattam_str = 'xx(.*?)--'
# result = re.compile(pattam_str).findall(str)
result = re.findall(pattam_str, str)
print(result)