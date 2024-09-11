try:
    first_pizza = int(input('Введите цену первой пиццы: '))
    second_pizza = int(input('Введите цену второй пиццы: '))
    if first_pizza < second_pizza:
        print('Первая пицца дешевле!')
    elif first_pizza > second_pizza:
        print('Вторая пицца дешевле!')
    elif first_pizza == second_pizza:
        print('Обе пиццы стоят одинаково!')
except ValueError as e:
    print('Введите корректные числовые значения для цен.')