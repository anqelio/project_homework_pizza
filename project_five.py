from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите вашу дату заказа (гггг-мм-дд): '),'%Y-%m-%d')
    day_today = datetime.now()
    if date_order >= day_today:
        print('Ваш заказ принят!')
    else:
        print('Ошибка: Вы не можете заказать пиццу на прошедшую дату.')
except ValueError as e:
    print('Некорректная дата, либо формат даты')