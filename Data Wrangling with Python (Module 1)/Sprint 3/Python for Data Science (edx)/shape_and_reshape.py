import numpy

user_input = input()

my_list = user_input.split(" ")

my_array = numpy.asarray(my_list, dtype=int)
my_array.shape = (3, 3)

my_array.reshape(my_array, 3, 2)

print(my_array)
