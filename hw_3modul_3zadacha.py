import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)

    # Перевірка, чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо так, перевіряємо, чи має міжнародний код '+38'
        if not cleaned_number.startswith('+38'):
            cleaned_number = '+38' + cleaned_number[1:]
    else:
        # Якщо немає '+', додаємо '+38'
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

# Приклад використання
phone_number = "    +38(050)123-32-34"
normalized_number = normalize_phone(phone_number)
print(f"Нормалізований номер: {normalized_number}")
