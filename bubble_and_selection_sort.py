import random
import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr_100 = [random.randint(1, 1000) for _ in range(100)]
print(f"Список из 100 чисел:",arr_100)

original_data = arr_100.copy()

print(f"Сортировка пузырьком:",bubble_sort(original_data.copy()))
print(f"Сортировка выбором:",selection_sort(original_data.copy()))

time_bubble = timeit.timeit(lambda: bubble_sort(original_data.copy()), number=1000)
time_selection = timeit.timeit(lambda: selection_sort(original_data.copy()), number=1000)

print(f"Время сортировки пузырьком:",time_bubble)
print(f"Время сортировки выбором:",time_selection)
