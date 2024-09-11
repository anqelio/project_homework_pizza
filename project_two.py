from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите вашу дату рождения (гггг-мм-дд): '),'%Y-%m-%d')
    birthday = datetime.strptime('2007-11-15', '%Y-%m-%d')
    if date_order == birthday:
        print('С днём рождения! Вы получаете скидку 20% на пиццу!')
    else:
        print('Сегодня не ваш день рождения')
except ValueError as e:
    print('Неверный формат даты. Введите дату в формате гггг-мм-дд.')