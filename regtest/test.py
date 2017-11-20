#_*_ coding: utf-8 _*_
_author_="wangyh"
import re
line = "boobby123"
regex_str1 = "^b.*" # ^表示必须以 b 为开头,.号表示任何字符
regex_str2 = "^b.*3$" # $表示必须以 3 为结尾
regex_str3 = ".*(b.*b).*" # 从右反向匹配，贪婪匹配
regex_str4 = ".*?(b.*b).*" # ？非贪婪匹配，从左开始遇到第一个，注意第二个 b 之前没有问号，表示第二个 b 还是贪婪匹配
regex_str5 = ".*?(b.*?b).*" # ？非贪婪匹配，从左开始遇到第一个
regex_str6 = ".*(b.+b).*" # +表示至少出现一次，*表示任意次数（0）
regex_str7 = ".*(b.{2,5}b).*" # {2,5}表示2到5次，从右往左
regex_str8 = "（(bobby|boobby)123）" # |表示或的意思 括号的顺序为从外到内 group(1)=boobby123 group(2)=boobby
regex_str9 = "([abcd]oobby123)" #[] 表示括号内任意一个都行,[^1]中^表示反的意思，不等于1.在[.*]中，.*没有特殊含义。
regex_str10 = "(你\s好）"  # \s 表示空格,\S 表示非空格，\w 表示任意字符[A-Za-z0-9_],\W 表示相反
regex_str11 = ".*?([\u4E00-\u9FA5]+大学)" #[\u4E00-\u9FA5]表示提取汉字
regex_str12 = ".*?(\d+)年" # \d表示任意数字
match_obj = re.match(regex_str4,line)
print(match_obj.group(1))# 提取第一个括号内
if ( re.match(regex_str2,line) ):
    print("yes")