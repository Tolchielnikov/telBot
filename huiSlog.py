
hui = ' ХУЙ'


def huislog(sentence):
    words = sentence.split()
    i = 0
    while i < len(words):
        if syllables(words[i]) > 1:
           print("БОЛЬШЕ ОДНОГ СЛОГАА !!!!")
           print(type(words[i]))
           print(deleteFirstSyllables(words[i])+'  !!!!!!')
           huiWords = (hui + deleteFirstSyllables(words[i]))

        else:

             huiWords = (hui + words[i])
             print('ОДИН СЛОГ !!!!'+huiWords)
#             print('ОДИН СЛОГ ТИП !!!!'+type(huiWords))

        i = i + 1

    return huiWords


def syllables(word):
    word = word.lower()
    if word.endswith('ru'):
        word = word[:-1]
    vowels = 'аоиеёэыуюя'
    in_vowel_group = False
    vowel_groups = 0
    for letter in word:
        if letter in vowels:
            if not in_vowel_group:
                in_vowel_group = True
                vowel_groups += 1
        else:
            in_vowel_group = False
    print('КОЛ-ВО СЛОГ')
    print(vowel_groups)
    return vowel_groups


def deleteFirstSyllables (word):
    word = word.lower()
    if word.endswith('ru'):
        word = word[:-1]
    vowels = 'аоиеёэыуюя'
    in_vowel_group = False
    for letter in word:
        if letter in vowels:
            word = word[1:]
            if not in_vowel_group:
                word = word[1:]
                break
    return word
