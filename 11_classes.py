import os
os.system('cls')

### Classes ###

'''
class MyEmptyPerson:
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())
'''
'''
class MyPerson:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname

my_person = MyPerson("Carlos", "Ceballos")
print(f'{my_person.name} {my_person.surname}')
print ("my_person.name ==>", my_person.name)
print ("my_person.surname ==>", my_person.surname)
'''

class MyPerson:
  def __init__(self, name, surname, alias = "Charly"):
    self.fullname = f'{name} ({alias}) {surname}'
  def walk (self):
    print(f'{self.fullname} está caminando')
  def play (self):
    print(f'{self.fullname} está jugando')

my_person = MyPerson(name="Carlos", surname="Ceballos")
print(my_person.fullname)
my_person.walk()
my_person.fullname = "Héctor (el chicharito) Hernández"
my_person.play()
