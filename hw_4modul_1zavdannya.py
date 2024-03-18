def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1

        if num_developers == 0:
            return 0, 0  # Якщо в файлі немає даних про розробників, повертаємо 0

        average_salary = total_salary / num_developers
        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print("Виникла помилка під час обробки файлу:", e)
        return None

# Приклад використання
total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна заробітна плата: {total}")
    print(f"Середня заробітна плата: {average}")
