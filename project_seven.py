try:
    human = int(input('Введите количество человек: '))
    quantity = (human * 2 + 6 - 1) // 6
    if quantity * 1:
        print('Вам нужно заказать',quantity,'пицц')
    else:
        print('Ошибка: Кол-во человек должно быть положительным.')
except ValueError as e:
    print('Некорректный ввод')