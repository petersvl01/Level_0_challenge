def common_words(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    s1 = set(word_1)
    s2 = set(word_2)
    list = (s1 & s2)
    for char in list:
        char = char.lower()
        char = ', '.join(list)
    print("Common characters: ",char)
   
common_words("Never", "Ever")
