#example1
mytuple = ("apple", "banana", "cherry")

#example2
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#example3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#example4
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#example5
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#example6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#example7
tuple1 = ("abc", 34, True, 40, "male")

#example8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#example9
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#example10
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#example11
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#example12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#example13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#example14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


#example15
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#example16
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#example17
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#example18
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#example19
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#example20
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#example21
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#example22
fruits = ("apple", "banana", "cherry")

#example23
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#example24
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#example25
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#example26
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#example27
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#example28
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#example29
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#example30
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#exercises1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#exercises2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#exercises3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#exercises4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
