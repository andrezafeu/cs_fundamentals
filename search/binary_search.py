import math

# logarithmic time
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = low + high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7))
print(binary_search(my_list, -1))


# Exercises from grokking algorithms:
# Suppose you have a sorted list of 128 names, and you're searching through it using binary search.
# What's the maximum number of steps it would take?

# Answer:
# For any list of n, binary search will take log2 n steps to run in the worst case.
print(math.log2(128))

# Suppose you double the size of the list. What's the maximum number os steps now?
print(math.log2(128*2))