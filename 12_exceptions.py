import os
import math
os.system('cls')

### Exceptions Handling ###

# try except
number_one, number_two = 5, 1
try:
  print("Todo bien??????????")
  print(number_one + number_two)
  print("Después de la ejección del código")
except:
  print("Se ha producido un error")

# try except else
print("--------------------------------------")
number_one, number_two = 5, "1"
try:
  print("Todo bien??????????")
  print(number_one + number_two)
  print("Después de la ejección del código")
except:
  print("Se ha producido un error")
else: # optional
  print("La ejecución continúa correctamente")

# try except else finally
print("--------------------------------------")
number_one, number_two = 5, 1
try:
  print("Todo bien??????????")
  print(number_one + number_two)
  print("Después de la ejección del código")
except:
  print("Se ha producido un error")
else: # optional
  print("La ejecución continúa correctamente")
finally: # optional
  # siempre se ejecuta
  print("Lo que sucede después")

# except por tipo de error
print("--------------------------------------")
number_one, number_two = 5, "1"
try:
  print("Todo bien??????????")
  number_two = math.sqrt(-100) # ValueError
  # print(number_one + number_two) # TypeError
  print("Después de la ejección del código")
except TypeError:
  print("Se ha producido un error 'TypeError'")
except KeyError:
  print("Se ha producido un error 'KeyError'")
except ValueError:
  print("Se ha producido un error 'ValueError'")

# captura de la información del error
print("--------------------------------------")
number_one, number_two = 5, "1"
try:
  print("Todo bien??????????")
  print(number_one + number_two)
  print("Después de la ejección del código")
except Exception as something:
  print(f"Se ha producido el error: {something}")
  print(f"Y es de tipo: {something.__class__}")
