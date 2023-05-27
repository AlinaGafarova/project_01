# Задача 2.4.

# Пункт А.

def remove_exclamation_marks(s):
    return s.replace('!', '')


print(remove_exclamation_marks('Hi! Hello!!!'))

# Пункт Б.


def remove_last_em(s):
    return s[:-1]


print(remove_last_em('!Hi!'))

# Вариант 2.

def remove_last_em_2(s):
    return s.removesuffix('!')


print(remove_last_em_2('!Hi!'))
