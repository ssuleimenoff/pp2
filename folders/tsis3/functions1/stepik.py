a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

print('\t', end='')
for i in range(c, d+1):
    print(i, '\t', end='')
print()

for i in range(a, b+1):
    print(i, '\t', end='')
    for j in range(c, d+1):
        print(i*j, '\t', end='')
    print()
