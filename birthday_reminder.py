from datetime import datetime, timedelta


DAY_DICT = {'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []}


def weekday_checker(name, date):
    weekday = date.strftime("%A")
    if weekday in ['Saturday', 'Sunday']:
        weekday = 'Monday'
    DAY_DICT[weekday].append(name)


def get_birthdays_per_week(users):
    current_date = datetime.now()
    end_date = current_date + timedelta(days=7)

    for name, date in users.items():
        date = date.replace(year=current_date.year)
        if current_date < date <= end_date:
            weekday_checker(name, date)

    for day, names in DAY_DICT.items():
        names_string = ', '.join(names)
        if DAY_DICT[day]:
            print(f'{day}: {names_string}')


# Створено для тестування роботи програми:

users_dict = {'Vasya': '23.10.1999',
    'Petro': '24.11.1999',
    'Cot': '22.11.2007',
    'Grisha': '28.11.1987',
    'Kiril': '23.11.1989',
    'Herman': '20.11.1998',
    'Tetyana': '21.11.1998',
    'Katya': '21.11.1999',
    'Dasha': '22.11.1999',
    'Kasha': '23.11.1999',
    'Marina': '24.11.1999',
    'Veronika': '25.11.1999',
    'Masha': '26.11.1998',
    'Sergey': '27.11.1985',
    'Nikilay': '28.11.1993'}

for name, date in users_dict.items():
    users_dict[name] = datetime.strptime(date, '%d.%m.%Y')


get_birthdays_per_week(users_dict)
