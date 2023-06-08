def iter_nums(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
for number in iter_nums(n):
    print(number)
