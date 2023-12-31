import os
os.system('cls')

# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

'''
my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)
'''

# Formateo
'''
name, surname, age = "Carlos", "Ceballos", 29
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #MY forma preferida
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
'''

# Desempaquetado de variables

language = "Python"
'''
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''

# División
"""
language_slice = language[1:2]
print(language_slice)

language_slice = language[1:1]
print(language_slice)

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:5]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)
"""

#reverse
'''
reversed_language = language[::-1]
print(reversed_language)
'''

# Funciones

print('capitalize ==>', language.capitalize())
print('upper ==>', language.upper())
print('count ==>', language.count('y'))
print('isnumeric ==>', language.isnumeric())
print('lower ==>', language.lower())
print('upper.isupper ==>', language.upper().isupper())
print('lower.isupper ==>', language.lower().isupper())
print('startswith "Py" ==>', language.startswith('Py'))
print('startswith "py" ==>', language.startswith('py'))
