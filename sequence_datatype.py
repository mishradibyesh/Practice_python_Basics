"""
to learn the sequence data types like
list , tuple , string
"""

"""
tuple : A tuple in Python is similar to a list.
The difference between the two is that we cannot change the elements of a tuple once
 it is assigned whereas we can change the elements of a list.
"""
my_tuple = (2, 3, 4, 5, 6)

# my_tuple.add(15)
# You can't add elements to a tuple because of their immutable property.
print(my_tuple)
# my_tuple[2] = 3 we can not mutate the existing elements of a tuple
# initializing an empty tuple
empty_tuple = tuple()
# we can print the built-in functions od any data type by using syntax
print(dir(tuple))
"""
List : The list is one of the most widely used data types in Python.
A Python List can be easily identified by square brackets [ ]. 
Lists are used to store the data items where each data item is separated by a comma (,).
A Python List can have data items of any data type, be it an integer type or a boolean type.
"""
my_list = [12 , 344 , 55 , "hello" , True]
my_list.append(24)
print(type(my_list))
print(len(my_list))
print(my_list[2])
# print(dir(my_list))
my_list.extend([84 , 33])
my_list.insert(2 , 3000)
check = my_list.__contains__(3000)
print(check)
list2 = [2222,3333]
list2.remove(3333)
my_list.__add__(list2)
print(my_list)
print(list2)
# slice in list
print(my_list[-4:-1])
print(my_list[-4:])
print(my_list[:-1])

"""
string :String is a collection of alphabets, words or other characters.
It is one of the primitive data structures and are the building blocks for data manipulation.
Python has a built-in string class named str . 
Python strings are "immutable" which means they cannot be changed after they are created
"""
my_string = "manoj"
my_string2 = "manoj is a good boy"
print(type(my_string2))
print(type(my_string))
print(my_string2[2])
print(my_string + "   "+  my_string2)
my_string3 = """Strings can be created by enclosing characters inside a single quote or double-quotes.
Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings."""
print(my_string3)
# slicing in string
print(my_string3[0:22])



