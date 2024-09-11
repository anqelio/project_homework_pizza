from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите дату заказа (гггг-мм-дд): '),'%Y-%m-%d')
    if date_order.weekday() != 5 and date_order.weekday() != 6:
        print('Ваш заказ принят!')
    else:
        print('Пицца не доставляется в выходные!')
except ValueError as e:
    print('Некорректный ввод даты')