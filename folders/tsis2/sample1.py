n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz,", end="")
    elif i % 3 == 0:
        print("Fizz,", end="")
    elif i % 5 == 0:
        print("Buzz,", end="")
    else:
        print(str(i) + ',', end="")
    if i % 10 == 0:
        print()
    if i % 15 == 0 and i % n == 0:
        print("FizzBuzz" + '.')
    if i % 3 == 0 and i % n == 0:
        print("Fizz" + '.')
        break
    if i % 5 == 0 and i % n == 0:
        print("Buzz" + '.')
        break