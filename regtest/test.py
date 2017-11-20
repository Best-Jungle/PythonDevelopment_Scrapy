#_*_ coding: utf-8 _*_
_author_="wangyh"
import re
line = "booooooooobby123"
regex_str1 = "^b.*" # ^表示必须以 b 为开头
regex_str2 = "^b.*3$" # $表示必须以 3 为结尾
regex_str3 = ".*(b.*b).*" # 从右反向匹配，贪婪匹配
regex_str4 = ".*?(b.*b).*" # ？非贪婪匹配，从左开始遇到第一个，注意第二个 b 之前没有问号，表示第二个 b 还是贪婪匹配
regex_str5 = ".*?(b.*?b).*" # ？非贪婪匹配，从左开始遇到第一个
match_obj = re.match(regex_str4,line)
print(match_obj.group(1))# 提取第一个括号内
if ( re.match(regex_str2,line) ):
    print("yes")