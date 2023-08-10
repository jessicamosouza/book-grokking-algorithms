#  Binary Search Leetcode Exercise: https://leetcode.com/problems/search-insert-position/
def binary_search(arr, item):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return low


print("Posição: ", binary_search([1, 3, 5, 6, 10, 17, 24, 50, 87], 4))
