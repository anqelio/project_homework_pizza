from datetime import datetime, timedelta
try:
    date_order = datetime.strptime(input('Введите вашу дату (гггг-мм-дд): '),'%Y-%m-%d')
    if date_order.weekday() == 5 and date_order.weekday() == 6:
        print('Мы доставим вам пиццу сегодня')
    else:
        print('Доставляем пиццу только в выходные')
        print(f'Сможем выполнить доставку только на следующие выходные')
except ValueError as e:
    print('Некорректный ввод даты')