def res(x):
    if x > 0:
        result = res(x - 1) - x
    else:
        result = 0
        return result

print(res(3))