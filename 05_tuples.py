import os
os.system('cls')

### Tuples ###
# Note: La diferencia entre TUPLA y LISTA es que las TUPLAS SON INMUTABLES

my_tuple = tuple()
my_other_tuple = ()
# print('my_tuple ==>', my_tuple)
# print('my_tuple type ==>', type(my_tuple))
# print('my_other_tuple ==>', my_other_tuple)
# print('my_other_tuple type ==>', type(my_other_tuple))

my_tuple = (35, 1.77, "Carlos", 'Ceballos', 'Ceballos')
# print('my_tuple[0] ==>', my_tuple[0])
# print('my_tuple[-1] ==>', my_tuple[-1])

# print('my_tuple.count("Ceballos") ==>', my_tuple.count("Ceballos"))
# print('my_tuple.index("Ceballos") ==>', my_tuple.index("Ceballos"))

# my_other_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment
# print('my_tuple ==>', my_tuple)

my_family_tuple = ('ANDY', 'Ranfi', 'Levi')
my_sum_tuple = my_tuple + my_family_tuple
print('my_tuple ==>', my_tuple)
print('my_family_tuple ==>', my_family_tuple)
print('my_sum_tuple ==>', my_sum_tuple)

print('my_sum_tuple[3:6] ==>', my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print('my_tuple ==>', my_tuple)
my_tuple.remove('Ceballos')
my_tuple[1] = 1.81
print('my_tuple ==>', my_tuple)
