# #example1
# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)

# #example2
# a = int(input())
# if (-15 < a <= 12) or (14 < a < 17) or (19 <= a):
#     print('True')
# else:
#     print('False')

# example3
# x, y, s = float(input()), float(input()), input()
# try:
#     if s == '+':
#         print(x + y)
#     elif s == '-':
#         print(x - y)
#     elif s == '/':
#         print(x / y)
#     elif s == "*":
#         print(x * y)
#     elif s == 'mod':
#         print(x % y)
#     elif s == 'pow':
#         print(x ** y)
#     elif s == 'div':
#         print(x // y)
# except ZeroDivisionError:
#     print("Деление на 0!")

# example4
# figure = input()
# S = 0
# if figure == ('треугольник'):
#     a, b, c = int(input()), int(input()), int(input())
#     p = ((a + b + c) / 2)
#     S = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif figure == ('круг'):
#     r = int(input())
#     S = 3.14 * (r ** 2)
# elif figure == ('прямоугольник'):
#     a, b = int(input()), int(input())
#     S = (a * b)
# print(S)

# # example5
# a, b, c = int(input()), int(input()), int(input())
# max = max(a, b, c)
# min = min(a, b, c)
# third = (a + b + c) - (max + min)
# print(max, min, third, sep='\n')

# # example6
# s = int (input())
# n1 =" программистов"
# n2 =" программист"
# n3 =" программиста"
# if  s>=0:
#   if s==0:
#     print(str(s) + n1)
#   elif s%100>=10 and s%100<=20:
#     print(str(s) + n1)
#   elif s%10==1:
#     print(str(s) + n2)
#   elif s%10>=2 and s%10<=4:
#     print(str(s) + n3)
#   else:
#     print(str(s) + n1)


# #example7
# a = input()
# sum1 = int(a[0]) + int(a[1]) + int(a[2])
# sum2 = int(a[3]) + int(a[4]) + int(a[5])
# if sum1 == sum2:
#     print('Счастливый')
# else:
#     print('Обычный')
