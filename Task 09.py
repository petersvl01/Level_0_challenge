#Task 0.9

def vowels_only():
    word = "Olivia"
    list_vowels = ("a", "e", "i", "o", "u")
    for i in word:
        if i not in list_vowels:
            word = word.replace(i, " ")
    print(word)

vowels_only()