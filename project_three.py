from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите вашу дату (гггг-мм-дд): '),'%Y-%m-%d')
    christmas = datetime.strptime('2024-12-31', '%Y-%m-%d')
    day_football = datetime.strptime('2024-12-10', '%Y-%m-%d')
    knowledge_day = datetime.strptime('2024-09-1', '%Y-%m-%d')
    programmer_day = datetime.strptime('2024-09-12', '%Y-%m-%d')
    birthday = datetime.strptime('2024-11-15', '%Y-%m-%d')
    if date_order == christmas:
        print('С Новым годом! Специальная пицца со скидкой для вас!')
    elif date_order == day_football:
        print('С днём футбола! Специальная пицца со скидкой для вас!')
    elif date_order == knowledge_day:
        print('С днём знаний! Специальная пицца со скидкой для вас!')
    elif date_order == programmer_day:
        print('С днём программиста! Специальная пицца со скидкой для вас!')
    elif date_order == birthday:
        print('С днём рождения! Специальная пицца со скидкой для вас!')
    else:
        print('Это не праздничная дата.')
except ValueError as e:
    print('Некорректный ввод даты')