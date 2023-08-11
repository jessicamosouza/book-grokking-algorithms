def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot]
    larger = [i for i in arr[1:] if i > pivot]
    return quicksort(smaller) + [pivot] + quicksort(larger)


print(quicksort([42, 11, 85, 7, 33, 19, 58]))
