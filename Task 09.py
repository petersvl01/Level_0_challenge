#Task 0.9

def vowels_only(word):
    LIST_VOWELS = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    find_vowels = []
    for char in word:
        if char in LIST_VOWELS:
            if char not in find_vowels:
                find_vowels.append(char)
                newstr = ', '.join(find_vowels)
    print("Vowels: ",newstr)

vowels_only("Airbase")
