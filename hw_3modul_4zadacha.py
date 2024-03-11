from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Перевірка, чи вже відбулося день народження цього року
        if birthday_this_year < today:
            # Якщо так, розглядаємо день народження на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначення різниці між днем народження та поточним днем
        days_until_birthday = (birthday_this_year - today).days

        # Перевірка, чи день народження відбувається впродовж наступного тижня
        if 0 <= days_until_birthday <= 7:
            # Перевірка, чи день народження припадає на вихідний
            if birthday_this_year.weekday() >= 5:
                # Якщо так, переносимо дату привітання на наступний понеділок
                monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": monday.strftime("%Y.%m.%d")})
            else:
                # Якщо немає вихідного, використовуємо дату народження
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John", "birthday": "1990.03.12"},
    {"name": "Alice", "birthday": "1992.03.19"},
    {"name": "Bob", "birthday": "1995.03.25"}
]

result = get_upcoming_birthdays(users)
print(result)
