from collections import Counter
res = []
for _ in range(int(input())):
    i = input().split()
    key, value = i[0], i[1]
    if key == "str":
        res.append(value)
    elif key == "bool":
        res.sort(reverse = not(eval(value)))
    elif key == "int" and int(value) < len(res):
        res = res[int(value):]
    elif key == "set":
        res.append(value)
        res = list(Counter(res))
    else:
        res.insert(0, key)
        res.append(value)
print(res)