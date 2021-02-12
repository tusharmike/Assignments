def multi(arr):
    total = 1
    for i in arr:
        total *= i
    return total


list1 = list(map(int, input().split()))
print(multi(list1))
