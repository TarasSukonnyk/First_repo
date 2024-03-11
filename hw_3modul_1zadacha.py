from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f"Помилка: неправильний формат дати - {date}")
        return None

    current_date = datetime.today()

    days_difference = (current_date - target_date).days

    return days_difference

target_date = '2024-03-12'
result = get_days_from_today(target_date)


if result is not None:
    print(f"Різниця у днях між {target_date} та сьогодні {result} днів.")
else:
    print("Не вдалося розрахуватирізницю у днях")