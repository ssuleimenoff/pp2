a = int(input())
b = int(input())
list = []

for i in range(a, b + 1):
    if i % 3 == 0:
        list.append(i)

res = 0
for x in list:
    res += x
print(res / len(list))