import os
os.system('cls')

### Loops ###

# While
'''
my_condition = 0

while my_condition < 10:
  print("my_condition 1 ==>", my_condition)
  my_condition += 2
else:
  print("my_condition es igual o mayor a diez")

while my_condition < 20:
  print("my_condition 2 ==>", my_condition)
  my_condition += 2
  if my_condition == 13:
    print("Mi condición es igual a 13")
    break

print("La ejecución continúa")
'''

# For

my_list = [35, 24, 62, 52, 30, 30, 17]
print()
for lista in my_list:
  print("lista ==>", lista)

my_tuple = (35, 1.77, "Carlos", 'Ceballos', 'Ceballos')
print()
for tupla in my_tuple:
  print("tupla ==>", tupla)

my_set = { 'Carlos', 'Ceballos', 29 }
print()
for set in my_set:
  print("set ==>", set)

my_dict = {
  'Nombre': 'Carlos',
  'Apellido': 'Ceballos',
  "Edad": 29,
  "Lenguajes": { "JavaScript", 'C++', "Python" },
  "Idiomas": [ "Español", "Ingles" ],
  1: 1.65
  }
print()
for keys in my_dict:
  print("keys ==>", keys)
  if keys == "Apellido":
    print("for keys break -----------------------------")
    break
else:
  print("El bucle for para keys ha finalizado")
for values in my_dict.values():
  if values == "Ceballos":
    print("Continue SE SALTA el registro")
    continue
  if values == [ "Español", "Ingles" ]:
    print("for values break -----------------------------")
    break
  print("values ==>", values)
else:
  print("El bucle for para values ha finalizado")
