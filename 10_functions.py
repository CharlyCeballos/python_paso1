import os
os.system('cls')

### Functions ###

'''
def my_function1 ():
  print("Esto es una función")
  my_function2 ()

def my_function2 ():
  print("La PTM cambiando términos")

my_function1 ()
'''

# '''
def sum_two_values (first_value, second_value):
  print("first_value + second_value =", first_value + second_value)

sum_two_values(first_value = float(input("Primer valor flotante: ")), second_value = float(input("Segundo valor flotante: ")))
sum_two_values(first_value = input("Primer valor: "), second_value = input("Segundo valor: "))
sum_two_values(5, 7)
# '''

'''
def sum_two_values_with_return(first_value, second_value):
  return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print("my_result ==>", my_result)
'''

'''
def print_name(name, surname):
  print(f"{name} {surname}")

print_name(surname='Ceballos', name='Carlos' )
'''

'''
def print_name_with_default(name, surname, alias = '"Sin alias"'):
  print(f"{name} {surname} {alias}")

print_name_with_default("Carlos", "Ceballos")
print_name_with_default("Carlos", "Ceballos", "Charly")
'''

'''
def print_texts(*text):
  print(text)

print_texts('Buenas tardes', 'Buongiorno', 'Good afternoon')
print_texts('Buenas tardes', 'Buongiorno')
print_texts('Buongiorno') # No sé porqué pone coma al final
'''
