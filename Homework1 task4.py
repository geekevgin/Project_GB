n = int(input('Введите число:'))
num_of_it = 0
div = 1
max_digit = 0
has_more_digits = 0
while num_of_it < 5:
    num_of_it += 1
    digit = (n // div) % 10
    div = div * 10
    has_more_digits = div * 10
    if max_digit < digit:
        max_digit = digit
    if has_more_digits != 0:
        has_more_digits = digit

print(max_digit)
