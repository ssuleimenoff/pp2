def rev_gen(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())
for i in rev_gen(n):
    print(i)
