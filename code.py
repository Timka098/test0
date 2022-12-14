import os, json
def path(file_path):
    project_folder_path = os.path.abspath(__file__ + '/..')
    file_abs_path = os.path.join(project_folder_path, file_path)
    return file_abs_path

"""Відкрити файл game_library.json та перетворити його дані 
на звичайний словник. Вивести цей словник на екран."""
#//
with open(path('games_library.json'), 'r', encoding='utf-8') as file:
    js = json.load(file)
print(js)
#\\
"""Користувачеві пропонується  додати новий жанр.
Він може ввести «так» або «ні».
Якщо він ввів «так» - створюємо новий жанр у словнику.
Оскільки у нового жанра поки що немає ігор - цьому жанру буде відповідати 
порожній список. Виводимо оновлений словник на екран."""
#//
genre = input("додати новий жанр?\nвведіть «так» або «ні». ")
if genre == 'так':
    genre = input('Який жанр створюємо')
    if (genre in js) == False:
        js[genre] = []
        print(js)
#\\
""" Згодом користувачеві пропонується додати гру. 
Він може ввести «так» або «ні». Якщо він ввів «так» -
 в нього запитується, до якого жанру належить гра, і додаємо гру у список, 
 що відповідає заданому жанру. Якщо користувач ввів жанр, якого не існує - 
 сповіщаємо про помилку і запитуємо до того моменту, поки він не введе 
 правильний жанр (використовуємо цикл while).
Виводимо оновлений словник на екран."""
#//
game = input('додати гру? потрібно ввести «так» або «ні»')
if game == 'так':
    while True:
        genre = input('до якого жанру належить гра?')
        if genre in js: break
        else: print('помилка, такого жанру не існуе')
    game = input('яку гру додати до цього жанру?')

    js[genre].append(game)
print(js)
#\\
"""Після цього користувачеві пропонується видалити один жанр. 
Він може ввести «так» або «ні». 
Якщо він ввів «так» - видаляємо відповідний жанр зі словника. 
Якщо користувач ввів жанр, якого не існує - 
 сповіщаємо про помилку і запитуємо до того моменту,
  поки він не введе правильний жанр (використовуємо цикл while).
Виводимо оновлений словник на екран."""
#//
t = input('потрібно видалити якись жанр? так або ні')
if t == 'так':
    t = input('який потрібно видалити?')
    if t in js: del js[t]
    else: print("Такого жанру не існує")
print(js)
#\\
"""я потерял текст"""
#//
with open(path('games_library.json'), 'w', encoding='utf-8') as file:
    # Первторили словник на json-формат і зберегли у створений файл
    json.dump(js, file, indent=4, ensure_ascii=False)
#\\
input()