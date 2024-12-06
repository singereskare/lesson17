# 1.
def print_params(a = 1, b = 'строка', c = True): # 1.1
    print(a, b, c) # 1.2
print_params() # 1.3
print_params(b = 25)
print_params(c = [1, 2, 3]) # 1.4
# 2
values_list = [2, 'распаковка', False] # 2.1
values_dict = {'a': 3, 'b': 'параметр', 'c': None} #2.2
print_params(*values_list)
print_params(**values_dict)  # 2.3
# 3.
values_list_2 = [54.32, 'Строка'] # 3.1
print_params(*values_list_2, 42)  # 3.2