def common_words(x, y):
    s1 = set(x)
    s2 = set(y)
    list = (s1 & s2)
    print("Common letter: {}" .format(list))

common_words("house", "computer")
common_words("House", "Hose")
