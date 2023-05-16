 Задача 1
# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print('Задача №1. Вариант 1.')
print('Первый трек:', my_favorite_songs[:14])
print('Последний трек:', my_favorite_songs[64:77])
print('Второй трек:', my_favorite_songs[16:-47])
print('Второйм трек с конца:', my_favorite_songs[51:-15])

print('Вариант 2.\n' +
      'Первый трек:', my_favorite_songs[:14] + '\n'
      'Последний трек:', my_favorite_songs[64:77] + '\n'
      'Второй трек:', my_favorite_songs[16:-47] + '\n'
      'Второйм трек с конца:', my_favorite_songs[51:-15])
