  # Создаём переменную типа String.
name = 'Andrey'
print(type(name),'Привет меня зовут', name)

# Созаём переменную типа Integer
age = 35
print(type(age), 'Да да, мне', age, 'лет')

# Создаём переменную типа Float
age1 = 40.1
print(type(age1),'Пусть будет', age1, ' лет с хвостиком)))')

# Создать переменную типа Bytes
b = bytes(10)
print(type(b), 'То ещё значение получилось =)', b)

# Сщздать переменную типа List
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(a), a)

# Создаём переменную типа Tuple
c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(c), c)

# Создаём переменную типа Set
q = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(q), q)

# Создаём переменную типа Frozenset
w = frozenset ('qwerty')
print(type(w), w)

# Создаём переменную Dict
r = dict (name = 'Andrey')
print(type(r), r)

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
z = 'Hello'
x = 'Physics'
m = 'Hello' + 'Physics'
print(type(m), m)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
weather = 'Ну и жара'
temperature = 35
print(weather, temperature)
print('Что то очень жарко'",", 35, 'градусов сегодня')

#  Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(weather, "+", temperature)
print('Очень жарко ' "+", 35)

