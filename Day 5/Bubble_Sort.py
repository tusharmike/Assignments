def bubble_sort(arr):
    size = len(arr) - 1
    for x in range(size):
        for y in range(size - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr


list1 = [2, 4, 1, 7]
print(bubble_sort(list1))
