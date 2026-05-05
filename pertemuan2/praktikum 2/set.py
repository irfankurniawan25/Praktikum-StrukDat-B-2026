thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, False, 0, 1, 2}
print(thisset)

set1 = {"abc", 34, True, 40, "male"}

thisset = set(("apple", "banana", "cherry")) 
print(thisset)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
set1 = {"a", "b", "c"}
set2 = (1, 2, 3)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) #atau juga dapat menggunakan tanda | sebagai pengganti union
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y) # union dapat menggabungkan set dengan iterabel lain, tetapi tanda | tidak dapat melakukannnya
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) 
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) # bisa juga dengan menggunkan tanda & sebagai pengganti intersection
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

