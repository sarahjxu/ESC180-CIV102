for i in range(5):
    for j in range(3):
        print(i, j)
# print all the combinations of elements of the alphabet s, of length 3

s = "abcdef"

'''
 aaa
 aab
 ...
 cef
 ...
 fff
'''

for c in s:
    print(c)

for c1 in s:
    for c2 in s:
        for c3 in s:
            print(c1+c2+c3)