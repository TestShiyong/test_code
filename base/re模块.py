import re

"""
常用表达式
    #匹配数字：[0-9]
    #仅匹配字母：'[a-z]+
    #匹配字母+_：\w+
"""

def re_search():
    """
    search匹配
    仅第一个匹配
    匹配对象或None
    若有分组，返回分组元组列表；否则返回完整匹配列表
    """

    str1 = "sp_cabernet_#86010d#*2x"
    #匹配数字
    res=re.search('[0-9]+', str1).group(0)
    print(res) # 86010

    #匹配字母

    str2 = "{sp_cabernet}_#86010d#*2x"
    #匹配字母 被下划线阻隔
    res=re.search('[a-z]+', str2).group(0)
    print(res) # sp


    str3 = "sp_cabernet_#86010d#*2x"
    #匹配花括号内包含下划线的字母
    res=re.search(r'{\w+}', str2).group(0)
    print(res) # {sp_cabernet}


def re_findall():
    """
    查找字符串中所有非重叠的匹配项
    固定返回列表数据
    :return:
    """
    #
    str1 = "sp_cabernet_#86010d#*2x"
    matches1='#(.*?)#'
    print(re.findall(matches1,str1)) #['86010d']


    str2 = "sp_{cabernet}_86010d#*2x"
    matches2=r'{\w+}'
    print(re.findall(matches2,str2)) # ['{cabernet}']



re_findall()