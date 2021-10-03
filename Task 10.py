def common_words():
    str1 = "house"
    str2 = "computer"
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2
    print(lst)

common_words()