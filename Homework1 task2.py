seconds = int(input('Введите время в секундах:'))
hours = seconds // 3600
minutes = (seconds - hours*3600) // 60
sec = seconds % 60
seconds_formatted = f'{hours:00}:{minutes:00}:{sec:00}'
print(seconds_formatted)
