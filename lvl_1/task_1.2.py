import random
import math
import datetime

# Задача 2
# Задача 1.2.
# Пункт А.

# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

print('Задача 2.\nПункт А.')

player = my_favorite_songs[0][1], \
         my_favorite_songs[1][1], \
         my_favorite_songs[2][1], \
         my_favorite_songs[3][1], \
         my_favorite_songs[4][1], \
         my_favorite_songs[5][1], \
         my_favorite_songs[6][1], \
         my_favorite_songs[7][1], \
         my_favorite_songs[8][1]

song_1, song_2, song_3 = random.choice(player), random.choice(player), random.choice(player)

sum_3_songs = round(song_1 + song_2 + song_3, 2)

print('Три случайные песни звучат', (math.floor(sum_3_songs - (sum_3_songs % 1))), 'мин.',
      (math.floor(sum_3_songs * 1000) % 1000) // 10, 'сек.')

print('Три случайные песни звучат', round(sum_3_songs, 2), 'мин.')

print('Пункт В.')

values = list(my_favorite_songs_dict.values())
song_dict_1, song_dict_2, song_dict_3 = random.choice(values), random.choice(values), random.choice(values)
sum_songs_dict = song_dict_1 + song_dict_2 + song_dict_3

print('Три случайные песни звучат', (math.floor(sum_songs_dict - (sum_songs_dict % 1))), 'мин.',
      (math.floor(sum_songs_dict * 1000) % 1000) // 10, 'сек.')

print('Три случайные песни звучат', round(sum_songs_dict, 2), 'мин.')

print('Пункт С.')

ran_song_my_favorite_songs = random.choice(list(my_favorite_songs))
print('Случайная песня из пункта A:', ran_song_my_favorite_songs.pop(0))

ran_my_favorite_songs_dict = random.choice(list(my_favorite_songs_dict))
print('Случайная песня из пункта В:', ran_my_favorite_songs_dict)

print('Пункт D.')