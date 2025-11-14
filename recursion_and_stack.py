def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))

def sum_list(arr):

    if not arr:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])

num_list = [1, 2, 3]
print(sum_list(num_list))

def binary_search_recursive(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, right, target)
        else:
            return binary_search_recursive(arr, left, mid - 1, target)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search_recursive(arr, 0, len(arr)-1, 5))

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стек пуст"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
print(f"Стек пуст:", stack.is_empty())
stack.push(5)
stack.push(15)
stack.push(25)
print(f"Верхний элемент стека:", stack.peek())
print(f"Размер стека:", stack.size())
print(f"Удаление верхнего элемента стека:", stack.pop())
print(f"Размер стека:", stack.size())
print(f"Стек пуст:", stack.is_empty())