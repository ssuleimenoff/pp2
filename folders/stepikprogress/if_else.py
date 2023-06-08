# a = int(input())
# b = int(input())
# h = int(input())
# if b >= h >= a:
#     print('Это нормально')
# elif h >= b:
#     print('Пересып')
# elif h <= b:
#     print('Недосып')

a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Високосный")
else:
    print("Обычный")