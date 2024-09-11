from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите вашу дату заказа (гггг-мм-дд): '),'%Y-%m-%d')
    day_today = datetime.now()
    X = date_order - day_today
    if day_today < date_order:
        print('До доставки вашей пиццы осталось',X,'дней.')
    else:
        print('Вы ввели прошедшую дату заказа.')
except ValueError as e:
    print('Некорректная дата, либо формат даты')