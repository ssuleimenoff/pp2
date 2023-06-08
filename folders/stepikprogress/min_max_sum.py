def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr[:-1])
    maxSum = sum(arr[1:])
    return minSum, maxSum


minSum, maxSum = miniMaxSum([1, 3, 5, 7, 9])
print(f'Minimum sum is {minSum}\nMaximum sum is {maxSum}')
