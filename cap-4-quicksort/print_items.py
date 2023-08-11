from time import sleep

def print_items(arr):
    for item in arr:
        sleep(1)
        print(item)


print_items([42, 11, 85, 7, 33, 19, 58])