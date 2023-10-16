from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)

    today = datetime.today().date()
    next_week_start = today + timedelta(days=(7 - today.weekday()))

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")

        if today <= birthday_this_year <= next_week_start:
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"

            birthday_dict[birthday_weekday].append(name)

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


test_users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "John Doe", "birthday": datetime(1990, 10, 18)},
    {"name": "Alice Johnson", "birthday": datetime(1985, 7, 8)},
]

get_birthdays_per_week(test_users)
