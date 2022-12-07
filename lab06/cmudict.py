def make_dict_1():
    text1 = open("cmudict.txt", "r")
    lines1 = text1.readlines()
    dict1 = {}
    for i in range(127, len(lines1)):
        splitted1 = lines1[i].split()
        dict1[splitted1[0]] = []
        for j in range(1, len(splitted1)):
            dict1[splitted1[0]].append(splitted1[j])
    return dict1

def make_dict_2():
    text2 = open("cmuvowels.txt", "r")
    lines2 = text2.readlines()
    dict2 = {}
    for i in range(len(lines2)):
        splitted2 = lines2[i].split()
        dict2[splitted2[0]] = splitted2[1]
    return dict2

def number_of_vowels(word, dict1, dict2):
    count = 0
    for key1 in dict1:
        if key1 == word:
            print(key1)
            for key2 in dict2:
                for j in dict1[key1]:
                    if not j.isalpha():
                        j = j[:-1]
                    if j == key2 and dict2[key2] == 'vowel':
                        count += 1
    return count

def num_syllables(word, dict1, dict2):
    vowels = number_of_vowels(word, dict1, dict2)
    '''if there are two consecutive vowelphones, count them as 1'''
    count = 0
    vowels = []
    for key1 in dict1:
        if key1 == word:
            print(key1)
            for key2 in dict2:
                for j in dict1[key1]:
                    if not j.isalpha():
                        j = j[:-1]
                    if j == key2:
                        vowels.append(dict2[key2])
                        if dict2[key2] == 'vowel':           
                            count += 1
    vowelphones = 0
    print(vowels)
    for i in range(len(vowels)-1):
        if vowels[i] == 'vowel' and not vowels[i+1] == 'vowel':
            vowelphones += 1
    return vowelphones

def readability(text):
    syllables = num_syllables(text, dict1, dict2)
    print(syllables)
    words = text.split(" ")
    print(len(words))
    sentences = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            sentences += 1
    print(sentences)
    #grade = 0.39(len(words)/sentences) + 11.8(syllables/len(words)) - 15.59
    #return grade

dict1 = make_dict_1()
dict2 = make_dict_2()
print(num_syllables("AEOLUS AEQUITRON", dict1, dict2))
#print(readability("AEOLUS AEQUITRON"))