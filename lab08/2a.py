words = open("text.txt", encoding="latin-1").read().split()

def word_count(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word]=1
        else:
            word_counts[word] += 1
    return word_counts

def top10(L):
    L.sort()
    return L[len(L)-10:]

def top10dic():
    word = open("pride.txt", encoding="latin-1").read().split()
    dic = word_count(word)
    dic_val_list = list(dic.values())
    dic_10 = top10(dic_val_list)
    dic_sorted = {}
    for occurence in dic:
        for i in dic_10:
            if dic[occurence] == i:
                dic_sorted[occurence] = i
                break
    return dic_sorted
    #inv_freq = {6: "the", 12: "a", 1:"hi"}
    #print(sorted(inv_freq.items()))

#print(top10([1, 3, 4, 5, 6, 7, 8, 5, 76, 78, 4, 6, 7, 8, 5, 6, 7, 56, 5, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 66, 7, 8, 4, 456, 456, 5675678, 345, 454785796, 2342342432424324234, 4568, 0]))
print(top10dic())