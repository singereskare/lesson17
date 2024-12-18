# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Объяснение кода:
# Функция с параметрами по умолчанию:
# Функция print_params принимает три параметра: a, b и c с значениями по умолчанию.
# Функция выводит значения этих параметров.

# Вызовы функции с различным количеством аргументов
print_params()  # Вывод: 1 строка True
print_params(42)  # Вывод: 42 строка True
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# Объяснение кода:
# Вызовы функции:
# Мы вызываем print_params с различными наборами аргументов, включая вызовы без аргументов и с именованными аргументами.
# Это демонстрирует гибкость функции и использование параметров по умолчанию.

# 2. Распаковка параметров
values_list = [3.14, 'hello', False]
values_dict = {'a': 100, 'b': 'dict_string', 'c': None}

# Передаем распакованные параметры в функцию
print_params(*values_list)  # Вывод: 3.14 hello False
print_params(**values_dict)  # Вывод: 100 dict_string None

# Объяснение кода:
# Распаковка параметров:
# Мы создаем список values_list и словарь values_dict с элементами различных типов.
# Используя * для распаковки списка и ** для распаковки словаря, передаем их в функцию print_params.

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42

# Объяснение кода:
# Распаковка + отдельные параметры:
# Создаем список values_list_2 с двумя элементами.
# Вызываем print_params, распаковывая элементы списка и добавляя еще один аргумент (42).
