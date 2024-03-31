def caching_fibonacci():
    # Створення порожнього словника для кешування результатів обчислення
    cache = {}

    # Внутрішня функція fibonacci з рекурсивним обчисленням чисел Фібоначчі та кешуванням
    def fibonacci(n):
        # Перевірка, чи вже обчислено число Фібоначчі n
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі за допомогою рекурсії
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Збереження результату обчислення у кеші
        cache[n] = result
        return result
    
    # Повернення внутрішньої функції fibonacci
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Повинно вивести 55
print(fib(15))  # 610