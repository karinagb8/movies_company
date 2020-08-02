romans = {
    1000: {
        'type_1': 'M',
        'type_5': None,
        'type_10': None
    },
    100: {
        'type_1': 'C',
        'type_5': 'D',
        'type_10': 'M'
    },
    10: {
        'type_1': 'X',
        'type_5': 'L',
        'type_10': 'C'
    },
    1: {
        'type_1': 'I',
        'type_5': 'V',
        'type_10': 'X'
    }
}


def convert(number, position=1000, roman=''):
    if number > 3999: # can't be converted
        return None

    value = int(number/position)
    
    type_10 = romans[position]['type_10']
    type_5 = romans[position]['type_5']
    type_1 = romans[position]['type_1']

    if value == 1:
        roman += type_1
    if value == 2:
        roman += type_1 + type_1
    if value == 3:
        roman += type_1 + type_1 + type_1
    if value == 4:
        roman += type_1 + type_5
    if value == 5:
        roman += type_5
    if value == 6:
        roman += type_5 + type_1
    if value == 7:
        roman += type_5 + type_1 + type_1
    if value == 8:
        roman += type_5 + type_1 + type_1 + type_1
    if value == 9:
        roman += type_1 + type_10

    if position == 1:
        return roman

    new_number = number - value*position
    new_position = position/10

    return convert(new_number, new_position, roman)

def int_to_roman(number):
    return convert(number)
