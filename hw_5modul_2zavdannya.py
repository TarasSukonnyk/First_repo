import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі дійсні числа у тексті за допомогою регулярних виразів
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    
    # Ітеруємося по знайденим числам і використовуємо конструкцію yield для створення генератора
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    # Викликаємо генератор generator_numbers, який повертає дійсні числа у тексті
    numbers_generator = func(text)
    
    # Обчислюємо загальну суму чисел з генератора
    total_sum = sum(numbers_generator)
    
    return total_sum

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
