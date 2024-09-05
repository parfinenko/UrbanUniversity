# Работа со словарями:

my_dict = {'Igor': 1999, 'Roman':2000,'Denis':1998}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict['Roman']}")
print(my_dict.get('Alex','Ключ не найден'))
my_dict.update({"Maria":2001,'Artem':2002})
a = my_dict.pop('Denis')
print(f'Deleted value: {a}')
print(my_dict)

#Работа с множествами:

my_set = {1,2,3,4,5,1,2,3,4,5,"rrr","rrr",}
print(my_set)
my_set.update((1.3,1.4,1.3,1.4))
my_set.remove(1)
print(my_set)

