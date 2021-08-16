n = int(input('Введите число:'))
div = 1
max_digit = 0
num_of_it = 0

while num_of_it < 9:
    num_of_it += 1
    digit = (n // div) % 10
    div = div * 10
    if max_digit < digit:
        max_digit = digit
print(max_digit)
