import os
os.system('cls')

### Lists ###

my_list = list()
my_other_list = []

# print('my_list', my_list)
# print('len my_list', len(my_list))
# print('my_other_list', my_other_list)
# print('len my_other_list', len(my_other_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
# print('my_list', my_list)
# print('len my_list', len(my_list))

my_other_list = [35, 1.77, "Carlos", 'Ceballos']
# print('my_other_list', my_other_list)

# print('type ==> my_list', type(my_list))
# print('type ==> my_other_list', type(my_other_list))

# print('my_other_list[0] ==>', my_other_list[0])
# print('my_other_list[1] ==>', my_other_list[1])
# print('my_other_list[-1] ==>', my_other_list[-1])
# print('my_other_list[len(my_other_list) - 1] ==>', my_other_list[len(my_other_list) - 1])
# print('my_other_list[-2] ==>', my_other_list[-2])

# age, height, name, surname = my_other_list
# print('name ==> ', name)

# print('my_list + my_other_list ==>', my_list + my_other_list)

# my_list = "Hola Python"
# print('my_list ==>', my_list)

my_other_list.append('Charly')
print('my_other_list ==>', my_other_list)

my_other_list.insert(1, "levi")
print('my_other_list ==>', my_other_list)

my_other_list[1] = 'Ranfi'
print('my_other_list ==>', my_other_list)

my_other_list.remove("Ranfi") # remove() elimina por valor
print('my_other_list ==>', my_other_list)

my_list.remove(30)
print('my_list ==>', my_list)

my_list.pop() # pop() retorna el elmento eliminado
print('my_list.pop()', my_list.pop())
print('my_list ==>', my_list)

my_pop_element = my_list.pop(2)
print('my_pop_element ==>', my_pop_element)
print('my_list ==>', my_list)

del my_list[2] # del elimina por indice
print('my_list ==>', my_list)

my_list.append(30)

my_new_list = my_list.copy()
my_list.clear()
print('my_list ==>', my_list)
print('my_new_list ==>', my_new_list)

my_new_list.reverse()
print('reversing my_new_list ==>', my_new_list)

my_new_list.sort()
print('sorting my_new_list ==>', my_new_list)

print(my_new_list[1:2])
