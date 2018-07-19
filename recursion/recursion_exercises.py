# Exercises from grokking algorithms

# Write a recursive function for the sum function

# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum(arr))



# Write a recursive function to count the number of items in a list
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count(arr))



# Find the maximum number in a list

def find_maximum(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    elif arr[0] <= arr[-1] and len(arr) > 2:
        return find_maximum(arr[1::])
    else:
        return find_maximum(arr[0:-2:])

print("Result of find_maximum is {}".format(find_maximum(arr)))
print("Result of find_maximum is {}".format(find_maximum([1])))
print("Result of find_maximum is {}".format(find_maximum([1, 2])))
print("Result of find_maximum is {}".format(find_maximum([])))
print("Result of find_maximum is {}".format(find_maximum([3, 2, 1])))
print("Result of find_maximum is {}".format(find_maximum([3, 2, 1, 1, 2, 5, 13, -3, 7])))



# Can you come up with the base case and recursive case for binary search?

num = 7

def recursive_binary_search(arr, num):
    minimum = arr[0]
    maximum = arr[-1]

    middle = (minimum + maximum) // 2
    if num > middle:
        return recursive_binary_search(arr[len(arr)//2:-1:], num)
    elif num == middle:
        return num
    else:
        return recursive_binary_search(arr[0::len(arr)//2], num)

print(recursive_binary_search(arr, num))