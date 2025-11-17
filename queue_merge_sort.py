import random
import timeit

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



def queue_task():
    queue = Queue()
    tasks = [("Задача 1", 2), ("Задача 2", 1), ("Задача 3", 4), ("Задача 4", 3)]

    for task, time in tasks:
        queue.enqueue((task, time))

    while not queue.is_empty():
        task, time = queue.dequeue()
        print(f"Задача: {task}, завершена за {time}")

queue_task()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr_10 = [random.randint(1, 1000) for _ in range(10)]
arr_100 = [random.randint(1, 1000) for _ in range(100)]
arr_1000 = [random.randint(1, 1000) for _ in range(1000)]

time_10 = (timeit.timeit(lambda: merge_sort(arr_10.copy()), number=1000))
time_100 = (timeit.timeit(lambda: merge_sort(arr_100.copy()), number=1000))
time_1000 = (timeit.timeit(lambda: merge_sort(arr_1000.copy()), number=1000))

print(f"Время сортировки слиянием: 10 элементов - ",time_10)
print(f"Время сортировки слиянием: 100 элементов - ",time_100)
print(f"Время сортировки слиянием: 1000 элементов - ",time_1000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

bubble_time_10 = (timeit.timeit(lambda: bubble_sort(arr_10.copy()), number=1000))
bubble_time_100 = (timeit.timeit(lambda: bubble_sort(arr_100.copy()), number=1000))
bubble_time_1000 = (timeit.timeit(lambda: bubble_sort(arr_1000.copy()), number=1000))

print(f"Время сортировки пузырьком: 10 элементов - ",bubble_time_10)
print(f"Время сортировки пузырьком: 100 элементов - ",bubble_time_100)
print(f"Время сортировки пузырьком: 1000 элементов - ",bubble_time_1000)

"""
На больших списках сортировка слиянием быстрее чем сортировка пузырьком
"""