#example1
myset = {"apple", "banana", "cherry"}

#example2
thisset = {"apple", "banana", "cherry"}
print(thisset)

#example3
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#example4
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#example5
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#example6
set1 = {"abc", 34, True, 40, "male"}


#example7
myset = {"apple", "banana", "cherry"}
print(type(myset))


#example8
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#example9
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example10
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#example11
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#example12
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#example13
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#example14
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#example15
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


#example16
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#example17
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example18
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#example19
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example20
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#example21
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#example22
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#example23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#example24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#example25
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#exercises1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruits!")

#exercises2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#exercises3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#exercises4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#exercises5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

