#example1
mylist = ["apple", "banana", "cherry"]

#example2
thislist = ["apple", "banana", "cherry"]
print(thislist)

#example3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#example4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#example5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#example6
list1 = ["abc", 34, True, 40, "male"]

#example7
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#example8
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#example9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#example10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#example11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#example13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#example14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#example15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#example17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#example19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#example20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#example22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#example24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#example25
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#example26
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example27
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example28
thislist = ["apple", "banana", "cherry"]
del thislist

#example29
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#example30
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#example31
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#example32
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#example33
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#example34
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#example36
newlist = [x for x in fruits if x != "apple"]

#example37
newlist = [x for x in fruits]

#example38
newlist = [x for x in range(10)]

#example39
newlist = [x for x in range(10) if x < 5]

#example40
newlist = [x.upper() for x in fruits]

#example41
newlist = ['hello' for x in fruits]

#example42
newlist = [x if x != "banana" else "orange" for x in fruits]

#example43
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example44
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#example45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#example46
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#example47
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#example48
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#example49
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#example50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#example51
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#example52
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#example53
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#example54
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#example55
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#exercises1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#exercises2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#exercises3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#exercises4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#exercises5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#exercises6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#exercises7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#exercises8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))






