import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        print("Помилка: Некоректні вхідні параметри.")
        return []

    # Генерація унікальних випадкових чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))

    # Сортування та повернення результату
    result = sorted(list(numbers_set))
    return result

# Приклад використання
min_value = 1
max_value = 49
quantity_to_select = 6

lottery_numbers = get_numbers_ticket(min_value, max_value, quantity_to_select)
print(f"Ваш лотерейний білет: {lottery_numbers}")
