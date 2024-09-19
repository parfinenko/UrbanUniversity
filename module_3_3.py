def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [5, False, 'строка']
values_dict = {'a': 3, 'b': 5, 'c': "строка"}
values_list_2 = [9, "apple"]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)