import re
import os
import time
# re.match ;用户匹配字符串开头：如果不是起始位置匹配成功的话，match()就返回none
# re.search:re.search 扫描整个字符串并返回第一个成功的匹配
# re.match与re.search的区别:re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
# 参数1:匹配的正则表达式,参数2：要匹配的字符串，标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配(非必填)
# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
# group(num=0)匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
# groups()返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项
# re.compile 函数 ompile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
# findall:在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# re.finditer：findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# re 模块提供了re.sub用于替换字符串中的匹配项,re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
# re.split:split 方法按照能够匹配的子串将字符串分割后返回列表
# 模式   描述
# ^    匹配字符串的开头
# $    匹配字符串的末尾。
# .    匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]   不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*  匹配0个或多个的表达式。
# re+  匹配1个或多个的表达式。
# re?  匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}   精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
# re{ n,}  匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
# re{ n, m}    匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b 匹配a或b
# (re) 匹配括号内的表达式，也表示一个组
# (?imx)   正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)  正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)  类似 (...), 但是不表示一个组
# (?imx: re)   在括号中使用i, m, 或 x 可选标志
# (?-imx: re)  在括号中不使用i, m, 或 x 可选标志
# (?#...)  注释.
# (?= re)  前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)  前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
# (?> re)  匹配的独立模式，省去回溯。
# \w   匹配字母数字及下划线
# \W   匹配非字母数字及下划线
# \s   匹配任意空白字符，等价于 [\t\n\r\f].
# \S   匹配任意非空字符
# \d   匹配任意数字，等价于 [0-9].
# \D   匹配任意非数字
# \A   匹配字符串开始
# \Z   匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z   匹配字符串结束
# \G   匹配最后匹配完成的位置。
# \b   匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B   匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等.   匹配一个换行符。匹配一个制表符。等
# \1...\9  匹配第n个分组的内容。
# \10  匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
# path=r'E:\音乐\Kacey Musgraves - Pageant Material - 2015[FLAC]'
path=r'G:\简爱跑步十二周'
file_path=path+'/'
for a in os.listdir(file_path):
    str_list=re.sub('【.*?】',"",a)
    print(str_list)
#time.sleep(5)
    # # print(re.compile(r'^\d ?',a))
    # # print(str_list)
    os.rename(file_path+a,file_path+str_list)