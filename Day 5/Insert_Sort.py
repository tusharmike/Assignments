def insertion_sort(arr):
    for x in range(1, len(arr)):
        k = arr[x]
        j = x - 1
        while j >= 0 and k < arr[j]:
            # for desc order sort change k>a[j]
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = k
    return arr


list1 = [24, 56, 1, 50, 17]
print(insertion_sort(list1))
