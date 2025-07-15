def century(year):
    century_number = year // 100 + 1

    if century_number // 100 == 0:
        century_number -= 1

    suffix = century_suffix(century_number)
    return f'{century_number}{century_suffix}'


def century_suffix(century_number):
    last_two = century_number % 100
    last_digit = century_number % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'
        
    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'