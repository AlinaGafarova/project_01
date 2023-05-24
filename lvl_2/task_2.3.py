# Задача 2.3.
# Вариант 1.

def switch_it_up(number):
    match number:
        case 0:
            return 'Zero'
        case 1:
            return 'One'
        case 2:
            return 'Two'
        case 3:
            return 'Three'
        case 4:
            return 'Four'
        case 5:
            return 'Five'
        case 6:
            return 'Six'
        case 7:
            return 'Seven'
        case 8:
            return 'Eight'
        case 9:
            return 'Nine'
        case _:
            return 'None'


chislo = int(input('Введите цифру от 0 до 9: '))
rezultat = switch_it_up(chislo)
print(rezultat)

# Вариант 2.

def switch_it_up_2(number_2):
    number_2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return number_2


chislo_2 = int(input('Введите цифру от 0 до 9: '))
print(switch_it_up_2(0)[chislo_2])
