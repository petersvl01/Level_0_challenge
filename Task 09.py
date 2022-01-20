#Task 0.9

def vowels_only(word):
    list_vowels = ("a", "e", "i", "o", "u")
    for i in word:
        if i not in list_vowels:
            word = word.lower()
            word = word.replace(i, " , ")
    print(word)

vowels_only("Umuzi")

#or,

def vowels_only(word1):
    list_vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for j in word1:
        if j not in list_vowels:
           word1 = word1.replace(j, " , ")
    print(word1)

vowels_only("Olive")
