def common_letters(word_1, word_2):
    set_1 = set(word_1.lower())
    set_2 = set(word_2.lower())
    list = (set_1 & set_2)
    for char in list:
        char = ', '.join(list)
    print("Common characters:",char)
   
common_letters("Never", "Ever")
