L = [5, 6, 10, 2, 4, 5]

L[1:5:2] #[6, 2]

L[:5:2]
L[::2]
L[0:5:2]
# [5, 10, 4]

L[::-1] # reverses the list

# we are not CHANGING L. This is creating some other list, but not storing it anywhere (but you can, see below)

L1 = L[1:5]
L.append(99) # returns None
# mistake: L = L.append(99), which makes L return None

L = [5, 6, 10, 2, 4, 5]

L.insert(1, "new") # puts "new" before index 1
L.insert(0, "newnew")
L.insert(len(L), "end")
print(L)

# incorrect: L = L.insert(...) makes L have return None

L.index(6) # the location of the first occurence of the argument
# 3

# if try to index an element not in the list, then there is an error

e = 6
e in L # True
99 not in L # True
10 not in L # False
# not in is a special thing that does the same as not(10 in L)

print(e in L, 99 not in L, 10 not in L)

e = 10
if e in L:
    print("The first occurence of", e, "in L is at index", L.index(e))
else:
    print("The element is not in L")

# extend
L1 = [1, 2, 3]
L2 = [7, 8]
L1.extend(L2)
# [1, 2, 3, 7, 8]
# different from append
L1.append(L2)
# [1, 2, 3, 7, 8, [7, 8]]

def my_extend(L1, L2):
    for e in L2:
        L1.append(e)

L = [1, 2, 3] + [5, 6] # adding lists just concatenates them together
# L is [1, 2, 3, 5, 6]
L = L + [7, 8] # subtly different, TBD

L += [10, 11] # same as .extend

L = [5, 6, 7, 10]
L[1:2] = [34, 56]
# L = [5, 34, 56, 7, 10]
# replace 6 with 34, 56
L[2:2] = [9, 9, 9]
# L = [5, 34, 9, 9, 9, 56, 7, 10]

L.sort() # L is now sorted from smallest to greatest
# all of these above functions don't return anything
sorted(L) # does not change L, returns a sorted version of L

Lnum = ["z", "a", "AAA", "abc", "zzz"]
sorted(Lnum)
# can't sort strings and integers in the same list, as they are not comparable
# .sort changes the contents of L so that it is sorted, sorted() does not change L, returns a new list that has the elements of L sorted
sorted(Lnum, reverse = True) # sorts in descending order

# everything you do with list you can do with string, except.sort, .appnend, .extend
# strings in python are unmutable, so you can't modify the contents of the string
# you can make a new string that does it, something like a = a + 5. s = s[1:], which python sees as ok
# string is like a list of characters

s = "Hello Engsci"
s[0]
s[1:] #"ello Engsci"