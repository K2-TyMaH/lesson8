from datetime import datetime, timedelta


DAY_DICT = {'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []}


def get_birthdays_per_week(users):
    current_date = datetime.now()
    end_date = current_date + timedelta(days=7)
    for name, date in users.items():
        date = date.replace(year=current_date.year)
        if date > current_date and date <= end_date:
            if date.weekday() == 0 or date.weekday() == 5 or date.weekday() == 6:
                DAY_DICT['Monday'].append(name)
            elif date.weekday() == 1:
                DAY_DICT['Tuesday'].append(name)
            elif date.weekday() == 2:
                DAY_DICT['Wednesday'].append(name)
            elif date.weekday() == 3:
                DAY_DICT['Thursday'].append(name)
            elif date.weekday() == 4:
                DAY_DICT['Friday'].append(name)

    for day, names in DAY_DICT.items():
        names_list = ""
        for name in names:
            names_list += f'{name}, '
        if DAY_DICT[day]:
            print(f'{day}: {names_list[0:-2]}')


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
