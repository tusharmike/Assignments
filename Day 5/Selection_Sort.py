def selection_sort(arr):
    for x in range(len(arr)):
        mini = x
        for y in range(x + 1, len(arr)):
            if arr[mini] > arr[y]:
                mini = y
        arr[x], arr[mini] = arr[mini], arr[x]
    return arr


list1 = [34, 23, 1, 67, 4]
print(selection_sort(list1))
