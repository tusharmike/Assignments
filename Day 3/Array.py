arr = []
for i in input("Enter values: ").split():
    arr.append(int(i))
print(f'Array before Deletion: {arr}')
arr.pop()
print(f'Array after Deletion: {arr}')
