# quicksort (Divide & Conquer algorithm)
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([]))
print(quicksort([10]))
print(quicksort([10, 5, 2, 3]))
print(quicksort([10, 5, 2, 3, -5, 20, 13, 14, 50, -19, 0]))

