import time
import math
def del_string(n, ms):
    print(time.time())
    time.sleep(ms / 1000)
    print(f'Square root of {n} after {ms} milliseconds is {math.sqrt(n)}')
    print(time.time())


newn = int(input())
news = int(input())
print(del_string(newn, news))