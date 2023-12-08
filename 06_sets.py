import os
os.system('cls')

### Sets ###

my_set = set()
my_other_set = {}
'''
# print('my_set ==>', my_set)
# print('my_other_set ==>', my_other_set)

my_other_set = { 'Carlos', 'Ceballos', 29 }
# print('my_other_set ==>', my_other_set)

# print('len(my_other_set) ==>', len(my_other_set))
# print('my_other_set[1] ==>', my_other_set[1]) #TypeError: 'set' object is not subscriptable

my_other_set.add('Charly')
print('my_other_set ==>', my_other_set)

my_other_set.add('Andy')
print('my_other_set ==>', my_other_set)

# my_other_set.add('Andy')
# my_other_set.add('Andy')
# my_other_set.add('Andy')
# my_other_set.add('Andy')
# my_other_set.add('Andy')
# my_other_set.add('Andy')
# print('my_other_set ==>', my_other_set)

print("'Charly' in my_other_set ==>", 'Charly' in my_other_set)
print("'Charlie' in my_other_set ==>", 'Charlie' in my_other_set)

my_set = my_other_set.copy()
print('my_set ==>', my_set)
del my_set # del elimina totalmente el registo de la variable
# print('my_set ==>', my_set) #NameError: name 'my_set' is not defined

my_other_set.clear() # clear() conserva la variable pero sin valores.
print('clearing my_other_set ==>', my_other_set)
'''

my_set = { 'Carlos', 'Ceballos', 29 }
my_other_set = { 'JavaScript', 'C++', 'Python' }
my_new_set = my_set.union(my_other_set)
print('my_set ==>', my_set)
print('my_other_set ==>', my_other_set)
print('my_new_set ==>', my_new_set)

# Su diferencia es my_other_set
print('my_new_set.difference(my_set) ==>', my_new_set.difference(my_set))

# Su diferencia es my_set
print('my_new_set.difference(my_other_set) ==>', my_new_set.difference(my_other_set))

# No tiene diferencia porque el union de ambos
print('my_set.difference(my_new_set) ==>', my_set.difference(my_new_set))
