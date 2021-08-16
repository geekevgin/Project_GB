a = int(input('Введите значение выручки:'))
b = int(input('Введите значение издержек:'))

if a > b:
    print('Прибыль.')
    profit = (a - b) / a
    print(f'Рентабельность:{profit}')
    employees = int(input('Введите численность сотрудников фирмы:'))
    profit_employee = (a - b) / employees
    print(f'Прибыль фирмы в расчете на одного сотрудника:{profit_employee}')
elif a < b:
    print('Убыток.')
elif a == b:
    print('Финансовый результат 0')


