import random
import timeit

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

def find_max_recursive(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    max_left = find_max_recursive(left_half)
    max_right = find_max_recursive(right_half)

    return max_left if max_left > max_right else max_right

nums = [1,2,4,7,8,11,3]
print(find_max_recursive(nums))

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

arr_10 = [random.randint(1, 1000) for _ in range(10)]
arr_100 = [random.randint(1, 1000) for _ in range(100)]
arr_1000 = [random.randint(1, 1000) for _ in range(1000)]

time_10 = (timeit.timeit(lambda: quicksort(arr_10.copy()), number=1000))
time_100 = (timeit.timeit(lambda: quicksort(arr_100.copy()), number=1000))
time_1000 = (timeit.timeit(lambda: quicksort(arr_1000.copy()), number=1000))

print(f"Время быстрой сортировки: 10 элементов - ",time_10)
print(f"Время быстрой сортировки: 100 элементов - ",time_100)
print(f"Время быстрой сортировки: 1000 элементов - ",time_1000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > n:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = n
    return arr

insertion_time_10 = (timeit.timeit(lambda: insertion_sort(arr_10.copy()), number=1000))
insertion_time_100 = (timeit.timeit(lambda: insertion_sort(arr_100.copy()), number=1000))
insertion_time_1000 = (timeit.timeit(lambda: insertion_sort(arr_1000.copy()), number=1000))

print(f"Время сортировки вставками: 10 элементов - ",insertion_time_10)
print(f"Время сортировки вставками: 100 элементов - ",insertion_time_100)
print(f"Время сортировки вставками: 1000 элементов - ",insertion_time_1000)

"""
На маленьких списках сортировка вставками быстрее, на больших быстрая сортировка более эффективна
"""