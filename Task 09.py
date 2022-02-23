def vowels_only(word):
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    find_vowels = []
    for char in word:
        if char in list_vowels and char not in find_vowels:
                find_vowels.append(char)
                newstr = ', '.join(find_vowels)
    print("Vowels: ",newstr)

vowels_only("Airbase")
