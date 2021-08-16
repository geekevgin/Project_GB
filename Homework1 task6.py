first_day = int(input('Расстояние в первый день тренировок:'))
last_day = int(input('Конечная цель:'))
days = 1
while first_day < last_day:
    first_day *= 1.1
    days += 1
    print(f'Требуемое количество дней для достижения цели:{days}')



