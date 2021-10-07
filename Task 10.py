def common_words():
    str1 = input("Enter string: ")
    str2 = input("Enter string: ")
    s1 = set(str1)
    s2 = set(str2)
    lst = list(s1 & s2)
    print("Common letter: {}" .format(lst))

common_words()