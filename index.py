import datetime

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def format_date_with_asterisks(day, month, year):
    return f"{str(day).zfill(2).replace('0', '*')} {str(month).zfill(2).replace('0', '*')} {str(year).replace('0', '*')}"

def main():
    day = int(input("Введите день вашего рождения: "))
    month = int(input("Введите месяц вашего рождения: "))
    year = int(input("Введите год вашего рождения: "))

    birth_date = datetime.date(year, month, day)

    day_of_week = get_day_of_week(day, month, year)
    print(f"День недели на дату {day:02d}-{month:02d}-{year}: {day_of_week}")

    leap_year = is_leap_year(year)
    print(f"Год {year} {'високосный' if leap_year else 'не високосный'}")

    age = calculate_age(birth_date)
    print(f"Вам сейчас {age} лет")

    formatted_date = format_date_with_asterisks(day, month, year)
    print(f"Ваша дата рождения в формате *: {formatted_date}")

if __name__ == "__main__":
    main()
