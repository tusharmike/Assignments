def swap(num):
    num[0], num[1] = num[1], num[0]


numList = list(input().split())
print(f'Before swapping: {numList[0]} {numList[1]}')
swap(numList)
print(f'After swapping: {numList[0]} {numList[1]}')
