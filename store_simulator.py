class Product:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight

    def show(self):
        return f"{self.name}, категория - {self.category}, стоимость {self.price} руб, вес {self.weight} грамм"

product1 = Product("Телевизор", "Электроника", 30000, 12000)
product2 = Product("Смартфон", "Электроника", 15000, 200)
product3 = Product("Видеокарта", "Комплектующие ПК", 35000, 550)
product4 = Product("Холодильник", "Бытовая техника", 43000, 80000)
product5 = Product("Портативная консоль", "Консоли", 55000, 640)

all_products = [product1, product2, product3, product4, product5]

cart = []

def show_products():
    print("Доступные товары:")
    number = 1
    for product in all_products:
        print(f"{number}. {product.show()}")
        number += 1

def show_cart():
    if len(cart) == 0:
        print("В корзине пусто")
        return

    print("В корзине:")
    total = 0
    for i in range(len(cart)):
        print(f"{i + 1}. {cart[i].show()}")
        total += cart[i].price
    print(f"Общая стоимость: {total} руб")

def add_to_cart():
    show_products()
    choice = int(input("Укажите номер товара для добавления в корзину: "))
    if choice >= 1 and choice <= len(all_products):
        cart.append(all_products[choice - 1])
        print(f"{all_products[choice - 1].name} добавлен в корзину")
    else:
        print("Укажите корректный номер товара")


def remove_from_cart():
    if len(cart) == 0:
        print("В корзине пусто")
        return
    show_cart()
    choice = int(input("Укажите номер товара для удаления из корзины: "))
    if choice >= 1 and choice <= len(cart):
        removed = cart.pop(choice - 1)
        print(f"{removed.name} удален из корзины")
    else:
        print("Укажите корректный номер товара")


def bubble_sort_by_price():
    n = len(cart)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cart[j].price > cart[j + 1].price:
                temp = cart[j]
                cart[j] = cart[j + 1]
                cart[j + 1] = temp


def bubble_sort_by_weight():
    n = len(cart)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cart[j].weight > cart[j + 1].weight:
                temp = cart[j]
                cart[j] = cart[j + 1]
                cart[j + 1] = temp

def insertion_sort_by_price():
    for i in range(1, len(cart)):
        current = cart[i]
        j = i - 1
        while j >= 0 and cart[j].price > current.price:
            cart[j + 1] = cart[j]
            j -= 1
        cart[j + 1] = current

def insertion_sort_by_weight():
    for i in range(1, len(cart)):
        current = cart[i]
        j = i - 1
        while j >= 0 and cart[j].weight > current.weight:
            cart[j + 1] = cart[j]
            j -= 1
        cart[j + 1] = current

def quick_sort_by_price(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = []
    right = []
    middle = []
    for item in items:
        if item.price < pivot.price:
            left.append(item)
        elif item.price == pivot.price:
            middle.append(item)
        else:
            right.append(item)
    return quick_sort_by_price(left) + middle + quick_sort_by_price(right)


def quick_sort_by_weight(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = []
    right = []
    middle = []
    for item in items:
        if item.weight < pivot.weight:
            left.append(item)
        elif item.weight == pivot.weight:
            middle.append(item)
        else:
            right.append(item)
    return quick_sort_by_weight(left) + middle + quick_sort_by_weight(right)

def merge_sort_by_price(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left_sorted = merge_sort_by_price(left)
    right_sorted = merge_sort_by_price(right)
    return merge_by_price(left_sorted, right_sorted)


def merge_by_price(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].price <= right[j].price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_by_weight(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left_sorted = merge_sort_by_weight(left)
    right_sorted = merge_sort_by_weight(right)
    return merge_by_weight(left_sorted, right_sorted)


def merge_by_weight(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].weight <= right[j].weight:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_cart():
    if len(cart) == 0:
        print("В корзине пусто")
        return

    print("Выберите сортировку?")
    print("1 - по цене")
    print("2 - по весу")


    choice1 = input("Выберите 1 или 2: ")

    print("Выберите вариант сортировки")
    print("1 - пузырьковая сортировка")
    print("2 - сортировка вставками")
    print("3 - быстрая сортировка")
    print("4 - сортировка слиянием")

    choice2 = input("Выберите от 1 до 4: ")

    if choice1 == "1" and choice2 == "1":
        bubble_sort_by_price()
        print("Сортировка пузырьком - цена")
    elif choice1 == "1" and choice2 == "2":
        insertion_sort_by_price()
        print("Сортировка вставками - цена")
    elif choice1 == "1" and choice2 == "3":
        sorted_cart = quick_sort_by_price(cart)
        cart.clear()
        cart.extend(sorted_cart)
        print("Быстрая сортировка - цена")
    elif choice1 == "1" and choice2 == "4":
        sorted_cart = merge_sort_by_price(cart)
        cart.clear()
        cart.extend(sorted_cart)
        print("Сортировка слиянием - цена")
    elif choice1 == "2" and choice2 == "1":
        bubble_sort_by_weight()
        print("Сортировка пузырьком - вес")
    elif choice1 == "2" and choice2 == "2":
        insertion_sort_by_weight()
        print("Сортировка вставками - вес")
    elif choice1 == "2" and choice2 == "3":
        sorted_cart = quick_sort_by_weight(cart)
        cart.clear()
        cart.extend(sorted_cart)
        print("Быстрая сортировка - вес")
    elif choice1 == "2" and choice2 == "4":
        sorted_cart = merge_sort_by_weight(cart)
        cart.clear()
        cart.extend(sorted_cart)
        print("Сортировка слиянием - вес")
    else:
        print("Укажите корректную сортировку")
        return

    show_cart()

def main():
    print("Добро пожаловать!")

    while True:
        print("\nВыбирите один из вариантов")
        print("1 - посмотреть товары")
        print("2 - посмотреть корзину")
        print("3 - добавить товар в корзину")
        print("4 - убрать товар из корзины")
        print("5 - отсортировать корзину")
        print("6 - выйти")

        choice = input("Укажите номер: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            show_cart()
        elif choice == "3":
            add_to_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            sort_cart()
        elif choice == "6":
            print("Спасибо!")
            break
        else:
            print("Укажите корректный номер")


if __name__ == "__main__":
    main()