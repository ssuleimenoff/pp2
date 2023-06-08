# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i +

# sum = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     sum += num
# print(sum)

a = int(input())
b = int(input())


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


lcm = a * b // gcd(a, b)
print(lcm)
