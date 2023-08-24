numbers = [23, 11, 3, 6, 8, 15, 4, 5, 44, 1]

def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for number in range(0, n - i - 1):
            if num[number] > num[number + 1]:
                num[number], num[number + 1] = num[number + 1], num[number]
    return num

sorted_numbers = bubble_sort(numbers)


ResultOk = False
pos = -1

def binary_search(n, val):
    global ResultOk, pos
    first = 0
    last = len(n) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if val == n[mid]:
            ResultOk = True
            pos = mid
            break
        elif val > n[mid]:
            first = mid + 1
        else:
            last = mid - 1

target_number = 8
binary_search(sorted_numbers, target_number)

if ResultOk == True:
    print(f"Element {target_number} found at index {pos}")
elif ResultOk == False:
    print(f"Element {target_number} not found.")
