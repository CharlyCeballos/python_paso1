import os
os.system('cls')

### Dictionaries ###

my_dict = dict()
my_other_dict = {}

my_other_dict = { 'Nombre': 'Carlos', 'Apellido': 'Ceballos', "Edad": 29 }
# print("my_other_dict ==>", my_other_dict)

my_dict = {
  'Nombre': 'Carlos',
  'Apellido': 'Ceballos',
  "Edad": 29,
  "Lenguajes": { "JavaScript", 'C++', "Python" },
  "Idiomas": [ "Español", "Ingles" ],
  1: 1.65
  }
# print("my_dict ==>", my_dict)
'''
print("my_dict['Nombre'] ==>", my_dict['Nombre'])
print("my_dict['Idiomas'] ==>", my_dict['Idiomas'])

my_dict['Mascota'] = "Larregui"
print("my_dict ==>", my_dict)

del my_dict['Idiomas']
print("my_dict ==>", my_dict)

print("'Carlos' in my_dict ==>", "Carlos" in my_dict)
print("'Nombre' in my_dict ==>", "Nombre" in my_dict)
'''

# print("my_dict.items() ==>>", my_dict.items())
# print("my_dict.keys() ==>>", my_dict.keys())
# print("my_dict.values() ==>>", my_dict.values())

my_new_dict = dict.fromkeys(my_dict)
print("my_new_dict ==>", my_new_dict)

# my_second_dict = dict.fromkeys(my_dict, ['Carlos', 'Ceballos'])
# print("my_second_dict ==>", my_second_dict)

print("list(my_new_dict) ==>", list(my_new_dict))
print("tuple(my_new_dict) ==>", tuple(my_new_dict))
print("set(my_new_dict) ==>", set(my_new_dict))

my_values = my_dict.values()
print("my_values ==>", my_values)
