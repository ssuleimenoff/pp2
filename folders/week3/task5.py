def counting():
    ert = list(map(lambda i: isinstance(i, float), list1))
    result = len([e for e ert if e])
    return result


list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print("Original list:")
print(list1)
